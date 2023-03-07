# pylint: disable=redefined-outer-name
# pylint: disable=unused-import
"""
Tests for models.
"""

import datetime

from .fixtures import new_author, new_genre, new_book
from ..book_catalog_app.models.models import Book


def test_create_author(new_author):
    """Test if data provided for an author instance is stored as expected."""
    assert new_author.name == "Test Author"
    assert new_author.bio == "Test bio"


def test_create_genre(new_genre):
    """Test if data provided for a genre instance is stored as expected."""
    assert new_genre.name == "Test Genre"
    assert new_genre.description == "Test genre description"


def test_create_book(new_book):
    """Test if data provided for a book instance is stored as expected."""
    assert new_book.title == "Test Book"
    assert new_book.author.name == "Test Author"
    assert new_book.genres[0].name == "Test Genre"
    assert new_book.publication_date == datetime.date(2022, 1, 1)
    assert new_book.description == "Test book description"


# ________________________________________________________________________


def test_update_author_data(new_author):
    """Test if updated data is stored successfully in the author instance."""
    new_name = "Test Author 2"
    new_bio = "Test bio 2"
    new_author.name = new_name
    new_author.bio = new_bio
    assert new_author.name == new_name
    assert new_author.bio == new_bio


def test_update_genre_data(new_genre):
    """Test if updated data is stored successfully in the genre instance"""
    new_name = "Test Genre 2"
    new_description = "Test genre description 2"
    new_genre.name = new_name
    new_genre.description = new_description
    assert new_genre.name == new_name
    assert new_genre.description == new_description


def test_update_book_data(new_book):
    """Test if updated data is stored successfully in the book instance"""
    new_title = "Test Book 3"
    new_author_inst = None
    new_publication_date = datetime.date(2023, 3, 3)
    new_description = "Test book description 2"

    new_book.title = new_title
    new_book.author = new_author_inst
    new_book.genres.clear()
    new_book.publication_date = new_publication_date
    new_book.description = new_description

    assert new_book.title == new_title
    assert new_book.author == new_author_inst
    assert len(new_book.genres) == 0
    assert new_book.publication_date == new_publication_date
    assert new_book.description == new_description


# ________________________________________________________________________


def test_add_genre_to_book(new_author, new_genre):
    """Test adding genre to a book"""
    book = Book(title="Test title", author=new_author)
    book.genres.append(new_genre)
    assert new_genre in book.genres


def test_delete_genre_from_book(new_author, new_genre):
    """Test removing genre from a book"""
    book = Book(title="Test title", author=new_author, genres=[new_genre])
    book.genres.remove(new_genre)
    assert new_genre not in book.genres
