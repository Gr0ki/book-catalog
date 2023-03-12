# pylint: disable=unused-variable
"""
Application module setup
"""
import os
from flask import Flask, Blueprint
from flask_restful import Api

from .book_catalog_app.settings.config import TestingConfig, ProductionConfig
from .book_catalog_app.settings.extensions import db, migrate, ma
from .book_catalog_app.service.cli import populate_db_command, db_drop_all_command
from .book_catalog_app.rest.author_api import AuthorResource
from .book_catalog_app.rest.genre_api import GenreResource

from .book_catalog_app.rest.book_api import BookResource


api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)

api.add_resource(AuthorResource, "/authors", "/authors/<int:author_id>")
api.add_resource(GenreResource, "/genres", "/genres/<int:genre_id>")
api.add_resource(BookResource, "/books", "/books/<int:book_id>")


def create_app():
    """Create and configure the app"""
    app = Flask(__name__)
    if os.getenv("DEV") == "false":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(TestingConfig)

    register_extentions(app)
    register_cli_commands(app)

    app.register_blueprint(api_bp)

    return app


def register_extentions(app):
    """Register extentions for the Flask app"""
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


def register_cli_commands(app):
    """Register custom Flask CLI commands."""
    app.cli.add_command(populate_db_command)
    app.cli.add_command(db_drop_all_command)
