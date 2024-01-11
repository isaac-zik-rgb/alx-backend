#!/usr/bin/env python3
"""Instatiating babel in Flask app"""
from flask import Flask
from flask import render_template
from flask_babel import Babel
from flask import request
from flask import g

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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
    if request.args.get('locale'):
        return request.args.get('locale')
    if request.args.get('login_as'):
        locale = users.get(int(request.args.get('login_as'))).get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as: int) -> dict:
    """get_user
    """
    if login_as in users:
        return users.get(login_as)
    return None


@app.before_request
def before_request():
    """before_request
    """
    g.user = get_user(int(request.args.get('login_as')))


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """index
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")
