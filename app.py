import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/workarea1')
def workarea1():
    return "workarea1"


if __name__ == "__main__":
    app.run(debug=True);
