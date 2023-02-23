from flask import Flask

from .book_catalog_app.settings.extensions import db
from .book_catalog_app.settings.config import DevelopmentConfig


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    register_extentions(app)

    return app


def register_extentions(app):
    db.init_app(app)
