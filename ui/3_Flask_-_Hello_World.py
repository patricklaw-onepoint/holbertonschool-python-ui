#!/usr/bin/python3
"""Create a flask application to display a simple
‘Hello World!’ message as a webpage.
The hello world message should exist within a <H1> html tag."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Simple message"""
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
