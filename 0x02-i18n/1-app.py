#!/usr/bin/env python3
"""Instatiating babel in Flask app"""
from flask import Flask
from flask import render_template
from flask_babel import Babel
from flask import request

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """index
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True, threaded=True)
