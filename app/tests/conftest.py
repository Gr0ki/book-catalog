# pylint: disable=redefined-outer-name
"""
Fixtures for pytest tests.
"""

import pytest
from faker import Faker

from ..manage import create_app
from ..src.settings.config import TestingConfig
from ..src.settings.extensions import db
from ..src.service.models import Book, Author, Genre


fake = Faker()


@pytest.fixture(scope="module")
def app():
    """Return app handler with set up database and application configurations."""
    app = create_app()
    app.config.from_object(TestingConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app
        db.session.rollback()


@pytest.fixture(scope="module")
def client(app):
    """Returns a test client instance for the Flask app."""
    with app.test_client() as client:
        db.drop_all()
        db.create_all()
        yield client
        db.session.rollback()
    fake.unique.clear()


@pytest.fixture(scope="module")
def new_author(app):
    """Returns \"_new_author\" function to call inside tests."""
    with app.app_context():

        def _new_author(given_name=None, given_bio=fake.paragraph()):
            """Create and return a new author instance for each invocation."""
            author = Author(name=given_name or fake.unique.name(), bio=given_bio)
            db.session.add(author)
            db.session.commit()
            return author

        return _new_author


@pytest.fixture(scope="module")
def new_genre(app):
    """Returns \"_new_genre\" function to call inside tests."""
    with app.app_context():

        def _new_genre(given_name=None, given_description=fake.paragraph()):
            """Create and return a new genre instance for each invocation."""
            genre = Genre(
                name=given_name or fake.unique.name(), description=given_description
            )
            db.session.add(genre)
            db.session.commit()
            return genre

        return _new_genre


@pytest.fixture(scope="module")
def new_book(app):
    """Returns \"_new_book\" function to call inside tests."""
    with app.app_context():

        def _new_book(
            given_title=None,
            given_author_id=None,
            given_genre_id=None,
            given_publication_date=fake.date_this_century(),
            given_description=fake.paragraph(),
        ):
            """Create and return a new book instance for each invocation."""
            author = Author(name=fake.unique.name(), bio=fake.sentence())
            genre = Genre(name=fake.unique.word(), description=fake.sentence())
            db.session.add(author)
            db.session.add(genre)
            db.session.commit()
            book = Book(
                title=given_title or fake.unique.sentence(),
                author_id=given_author_id or author.id,
                genre_id=given_genre_id or genre.id,
                publication_date=given_publication_date,
                description=given_description,
            )
            db.session.add(book)
            db.session.commit()
            return book

        return _new_book
