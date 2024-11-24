from flask import Flask
import redis
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
    hits = int(redis_client.get(hits_id))
    return {"message": f"Hello! I'm {server_id}", "hits": hits}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

