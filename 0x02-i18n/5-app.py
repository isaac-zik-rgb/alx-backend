#!/usr/bin/env python3
"""
Flask app
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel



app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """get_locale
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id: int) -> dict:
    """get_user
    """
    if user_id in users:
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """before_request
    """
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        if user:
            g.user = user
    else:
        g.user = None


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ Handles / route
    """
    return render_template('5-index.html', user=g.user)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
