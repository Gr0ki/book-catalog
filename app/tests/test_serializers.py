# pylint: disable=redefined-outer-name
# pylint: disable=unused-import
"""Tests for serializers."""

from .conftest import new_genre, new_author, new_book, db_handler
from ..book_catalog_app.service.serializers import GenreSchema, AuthorSchema, BookSchema


def test_genre_schema_serializition(new_genre):
    """Test dump Genre model object to serialized data."""
    serializer = GenreSchema()
    serialized_genre = serializer.dump(new_genre)
    assert serialized_genre["id"] == new_genre.id
    assert serialized_genre["name"] == new_genre.name
    assert serialized_genre["description"] == new_genre.description


def test_genre_schema_deserialization(db_handler):
    """Test load serialized data to Genre model object."""

    payload = {
        "name": "Test Genre",
        "description": "Test genre description",
    }
    serializer = GenreSchema()
    genre_model_object = serializer.load(data=payload, session=db_handler.session)
    assert genre_model_object.name == payload["name"]
    assert genre_model_object.description == payload["description"]


# __________________________________________________________


def test_author_schema_serializition(new_author):
    """Test dump Author model object to serialized data."""

    serializer = AuthorSchema()
    serialized_author = serializer.dump(new_author)
    assert serialized_author["id"] == new_author.id
    assert serialized_author["name"] == new_author.name
    assert serialized_author["bio"] == new_author.bio


def test_author_schema_deserialization(db_handler):
    """Test load serialized data to Author model object."""

    payload = {
        "name": "Test Author",
        "bio": "Test bio",
    }
    serializer = AuthorSchema()
    serialized_author = serializer.load(data=payload, session=db_handler.session)
    assert serialized_author.name == payload["name"]
    assert serialized_author.bio == payload["bio"]


# __________________________________________________________


def test_book_schema_serializition(new_book, new_author, db_handler):
    """Test dump Book model object to serialized data."""
    new_book.author = new_author.id
    db_handler.session.add(new_book)
    db_handler.session.commit()

    serializer = BookSchema()
    serialized_book = serializer.dump(new_book)
    assert serialized_book["id"] == new_book.id
    assert serialized_book["title"] == new_book.title
    assert serialized_book["author"] == new_book.author
    assert serialized_book["publication_date"] == new_book.publication_date.strftime(
        "%Y-%m-%d"
    )
    assert serialized_book["description"] == new_book.description


def test_book_schema_deserialization(new_book, new_author, db_handler):
    """Test load serialized data to Book model object."""

    payload = {
        "title": new_book.title,
        "author": new_author.id,
        "publication_date": new_book.publication_date.strftime("%Y-%m-%d"),
        "description": new_book.description,
    }
    serializer = BookSchema()
    serialized_book = serializer.load(data=payload, session=db_handler.session)
    assert payload["title"] == serialized_book.title
    assert payload["author"] == serialized_book.author
    assert payload["publication_date"] == serialized_book.publication_date.strftime(
        "%Y-%m-%d"
    )
    assert payload["description"] == serialized_book.description


# __________________________________________________________
