from flask import Flask, render_template, request, redirect, url_for
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def home():
	return render_template('index.html', posts=redis.lrange('posts', 0, -1))

@app.route("/statusupdate", methods=['POST'])
def status_update():
	status_update_text = request.form['text']
	redis.lpush('posts', status_update_text.encode('utf-8'))
	return redirect(url_for('home'))

@app.route("/adduser",methods=['POST'])
def adduser():
	username = request.form['username']	
	password = request.form['password']
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	redis.hmset("user:{}".format(username), {'password':password, 'firstname':firstname, 'lastname':lastname})
	return ""

if __name__ == "__main__":
	app.run()
