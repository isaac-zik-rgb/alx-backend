#!/usr/bin/env python3
""" implement a way to force a particular locale
by passing the locale=fr parameter to your app’s URLs.
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel, gettext
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
    requested_locale = request.args.get('locale')
    if requested_locale:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """index
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
