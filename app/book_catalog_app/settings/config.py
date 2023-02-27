import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB = os.getenv("DB")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DEV_DB_NAME = os.getenv("DEV_DB_NAME")
TEST_DB_NAME = os.getenv("TEST_DB_NAME")
PROD_DB_NAME = os.getenv("PROD_DB_NAME")


class Config:
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = (f"{DB}://" +
        f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DEV_DB_NAME}")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (f"{DB}://" +
        f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{PROD_DB_NAME}")