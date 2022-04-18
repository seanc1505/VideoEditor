from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "You made it"

@app.route("/hi")
def hi():
    return "who are you"


@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}"
    