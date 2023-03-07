"""
Application module setup
"""
import os
from flask import Flask

from .book_catalog_app.settings.config import TestingConfig, ProductionConfig
from .book_catalog_app.settings.extensions import db, migrate
from .book_catalog_app.service.cli import populate_db_command, db_drop_all_command


def create_app():
    """Create and configure the app"""
    app = Flask(__name__)
    if os.getenv("DEV") == "false":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(TestingConfig)

    register_extentions(app)
    register_cli_commands(app)

    return app


def register_extentions(app):
    """Register extentions for the Flask app"""
    db.init_app(app)
    migrate.init_app(app, db)


def register_cli_commands(app):
    """Register custom Flask CLI commands."""
    app.cli.add_command(populate_db_command)
    app.cli.add_command(db_drop_all_command)
