import os
from flask import Flask
import redis

app = Flask(__name__)

# loads the welcome page
@app.route('/')
def welcome_message():
    return f'Welcome to this page!'

# increments and displays the visitor count
@app.route('/count')
def count():
    host = os.getenv("REDIS_HOST" , "redis")
    port = os.getenv("REDIS_PORT" , 6379)

    r = redis.Redis(host=host, port=port)
    incremented = r.incr('count')
    return f"The current count is: {incremented}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)