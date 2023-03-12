# pylint: skip-file
"""Configs for the Flask app."""
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB = os.getenv("DB")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_TEST_PORT = os.getenv("DB_TEST_PORT")
TEST_DB_NAME = os.getenv("TEST_DB_NAME")
DB_NAME = os.getenv("DB_NAME")


class Config:
    """Basic configs"""

    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Test settings."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"{DB}://" + f"{DB_USER}:{DB_PASSWORD}@mysql-test:{DB_PORT}/{TEST_DB_NAME}"
    )


class ProductionConfig(Config):
    """Production settings."""

    SQLALCHEMY_DATABASE_URI = (
        f"{DB}://" + f"{DB_USER}:{DB_PASSWORD}@db:{DB_PORT}/{DB_NAME}"
    )
