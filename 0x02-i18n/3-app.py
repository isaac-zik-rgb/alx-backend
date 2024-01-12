#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])



@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """The home/index page
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
