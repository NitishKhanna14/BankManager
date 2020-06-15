from flask import Flask


app = Flask(__name__)


@app.route("/")
def func_main():
    return "<h1>Project running successfully</h1>"