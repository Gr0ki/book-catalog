# pylint: disable=redefined-outer-name
"""
Fixtures for pytest tests.
"""

import datetime
import pytest

from ..manage import create_app
from ..book_catalog_app.settings.config import TestingConfig
from ..book_catalog_app.settings.extensions import db
from ..book_catalog_app.models.models import Book, Author, Genre


@pytest.fixture(scope="session")
def app():
    """Return app handler with set up database and application configurations."""
    app = create_app()
    app.config.from_object(TestingConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app
        db.session.rollback()


@pytest.fixture(scope="function")
def db_handler(app):
    """Provides db handler for testing purposes within app context."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db
        db.session.rollback()


@pytest.fixture(scope="function")
def new_author(db_handler):
    """Create and return a new author instance for each invocation."""
    author = Author(name="Test Author", bio="Test bio")
    db_handler.session.add(author)
    db_handler.session.commit()
    return author


@pytest.fixture(scope="function")
def new_genre(db_handler):
    """Create and return a new genre instance for each invocation."""
    genre = Genre(name="Test Genre", description="Test genre description")
    db_handler.session.add(genre)
    db_handler.session.commit()
    return genre


@pytest.fixture(scope="function")
def new_book(new_author, new_genre, db_handler):
    """Create and return a new book instance for each invocation."""
    book = Book(
        title="Test Book",
        author=new_author.id,
        publication_date=datetime.date(2022, 1, 1),
        description="Test book description",
    )
    book.genres.append(new_genre)
    db_handler.session.add(book)
    db_handler.session.commit()
    return book
