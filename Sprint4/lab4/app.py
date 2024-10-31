from flask import Flask, session, request, redirect, url_for
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route('/')
def index():
    if 'username' in session:
        return f'''
            <h1>Logged in as {session["username"]}</h1>
            <form name="logout" action="{url_for('logout')}" method="post">
                <input type=submit value=Logout>
            </form>
        '''
    return '''
        <h2>You are not logged in. <a href="{url_for('login')}">Login?</a></h2>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <h2>Please login</h2>
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
