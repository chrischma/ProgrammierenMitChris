#!/usr/bin/env python3.6

import os
from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)


@app.route("/")
def basic_redirect():
    return redirect("https://www.google.com")


@app.route("/2do/", methods=['GET'])
def index():
  message = "Hello, welcome to site '2do'!"
  return render_template('index.html', message=message)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=1024, debug=True)
