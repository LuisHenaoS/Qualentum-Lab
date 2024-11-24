from flask import Flask

import redis
import requests
import os
import uuid


server_id = uuid.uuid4().hex
hits_id = f"{server_id}_hits"
app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_client = redis.StrictRedis(host=redis_host, port=6379, db=0)

@app.route('/')
def hello():
    redis_client.incr(hits_id)
    
    app1_host = os.getenv('APP1_HOST', 'app1')
    app1_url = f'http://{app1_host}:5000/'
    app1_response = requests.get(app1_url)
    
    return {
        "message": f"Hello from {server_id}!", 
        "app1_message": app1_response.json()
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

