from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def home():
	count = redis.incr('hits')
	return "Hello World! I have been seen {} times".format(count)

if __name__ == "__main__":
	app.run()
