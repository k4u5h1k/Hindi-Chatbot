from flask import Flask, render_template, request
import pyttsx3
from bot import *
from time import sleep

app = Flask(__name__)
c = Bot()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def botresponse():
    userText = request.args.get("msg")
    reply = str(c.reply(userText))
    c.say_to_file(reply)
    return reply

@app.route("/translate")
def translate():
    userText = request.args.get("msg")
    return c._translate(userText)

if __name__ == "__main__":
    app.run(debug=True)
