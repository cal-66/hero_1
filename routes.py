#__ routes.py
#import os


#port = int(os.environ.get('PORT', 5000))

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


if __name__ == '__main__':
	#app.run(debug = False, host='0.0.0.0', port=port)
	app.run(debug = False)