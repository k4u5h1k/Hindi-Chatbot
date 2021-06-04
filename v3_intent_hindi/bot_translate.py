from flask import Flask, render_template, request
import pyperclip
from bot import *

app = Flask(__name__)

c = Bot()

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/get")
def botresponse():
    userText = request.args.get("msg")
    y = str(c._translate(userText))
    pyperclip.copy(y)
    return y

if __name__ == "__main__":
    app.run(debug=True, port=8000)
