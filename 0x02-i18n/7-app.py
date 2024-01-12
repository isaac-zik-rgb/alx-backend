#!/usr/bin/env python3
"""Flask app
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from typing import (
    Dict,
    Union
)


class Config(object):
    """Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Returns a user dictionary or None if ID value can't be found
    or if 'login_as' URL parameter was not found
    """
    id = request.args.get('login_as', None)
    if id and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector

def get_locale():
    """Select and return best language match based on supported languages
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """Returns the timezone
    """
    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            return timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """The home page route
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
