"""Tests for serializers."""

from faker import Faker

from app.service.serializers import (
    GenreSchema,
    AuthorSchema,
    BookSchema,
)
from ..shared.data_generation import generate_data_for_book


fake = Faker()


def test_genre_schema_serializition(new_genre):
    """Test dump Genre model object to serialized data."""

    genre = new_genre()
    serializer = GenreSchema()
    serialized_genre = serializer.dump(genre)
    assert serialized_genre["id"] == genre.id
    assert serialized_genre["name"] == genre.name
    assert serialized_genre["description"] == genre.description


def test_genre_schema_deserialization():
    """Test load serialized data to Genre model object."""

    payload = {"name": fake.unique.name(), "description": fake.paragraph()}
    serializer = GenreSchema()
    genre_model_object = serializer.load(data=payload)
    assert genre_model_object.name == payload["name"]
    assert genre_model_object.description == payload["description"]


# __________________________________________________________


def test_author_schema_serializition(new_author):
    """Test dump Author model object to serialized data."""

    author = new_author()
    serializer = AuthorSchema()
    serialized_author = serializer.dump(author)
    assert serialized_author["id"] == author.id
    assert serialized_author["name"] == author.name
    assert serialized_author["bio"] == author.bio


def test_author_schema_deserialization():
    """Test load serialized data to Author model object."""

    payload = {"name": fake.unique.name(), "bio": fake.paragraph()}
    serializer = AuthorSchema()
    serialized_author = serializer.load(data=payload)
    assert serialized_author.name == payload["name"]
    assert serialized_author.bio == payload["bio"]


# __________________________________________________________


def test_book_schema_serializition(new_book):
    """Test dump Book model object to serialized data."""

    book = new_book()
    serializer = BookSchema()
    serialized_book = serializer.dump(book)
    assert serialized_book["id"] == book.id
    assert serialized_book["title"] == book.title
    assert serialized_book["author_id"] == book.author_id
    assert serialized_book["genre_id"] == book.genre_id
    assert serialized_book["publication_date"] == book.publication_date.strftime(
        "%Y-%m-%d"
    )
    assert serialized_book["description"] == book.description


def test_book_schema_deserialization(new_author, new_genre):
    """Test load serialized data to Book model object."""

    payload, _, _ = generate_data_for_book(new_author, new_genre)
    payload["publication_date"] = payload["publication_date"].strftime("%Y-%m-%d")
    serializer = BookSchema()
    serialized_book = serializer.load(data=payload)
    assert payload["title"] == serialized_book.title
    assert payload["author_id"] == serialized_book.author_id
    assert payload["genre_id"] == serialized_book.genre_id
    assert payload["publication_date"] == serialized_book.publication_date.strftime(
        "%Y-%m-%d"
    )
    assert payload["description"] == serialized_book.description


# __________________________________________________________
