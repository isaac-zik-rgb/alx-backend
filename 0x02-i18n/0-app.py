#!/usr/bin/env python3
"""Simple message of welcoming"""
from flask import Flask
from flask import render_template, request, Response

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> Response:
    """index
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
