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


@babel.localeselector
def get_locale() -> str:
    """get_locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """index
    """
    return render_template('2-index.html')
