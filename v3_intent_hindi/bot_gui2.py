from flask import Flask, render_template, request
from bot import *

app = Flask(__name__)

c = Bot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def botresponse():
    userText = request.args.get("msg")
    return str(c.reply(userText))

if __name__ == "__main__":
    app.run(debug=True)
