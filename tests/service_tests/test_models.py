"""
Tests for models.
"""

from faker import Faker

from ..shared.data_generation import generate_data_for_book

fake = Faker()


def test_create_author(new_author):
    """Test if data provided for an author instance is stored as expected."""

    payload = {"name": fake.unique.name(), "bio": fake.paragraph()}
    author = new_author(given_name=payload["name"], given_bio=payload["bio"])
    assert author.name == payload["name"]
    assert author.bio == payload["bio"]


def test_create_genre(new_genre):
    """Test if data provided for a genre instance is stored as expected."""

    payload = {"name": fake.unique.name(), "description": fake.paragraph()}
    genre = new_genre(
        given_name=payload["name"], given_description=payload["description"]
    )
    assert genre.name == payload["name"]
    assert genre.description == payload["description"]


def test_create_book(new_book, new_author, new_genre):
    """Test if data provided for a book instance is stored as expected."""

    payload, _, _ = generate_data_for_book(new_author, new_genre)
    book = new_book(
        given_title=payload["title"],
        given_author_id=payload["author_id"],
        given_genre_id=payload["genre_id"],
        given_publication_date=payload["publication_date"],
        given_description=payload["description"],
    )

    assert book.title == payload["title"]
    assert book.author_id == payload["author_id"]
    assert book.genre_id == payload["genre_id"]
    assert book.publication_date == payload["publication_date"]
    assert book.description == payload["description"]


# ________________________________________________________________________


def test_update_author_data(new_author):
    """Test if updated data is stored successfully in the author instance."""

    author = new_author()
    payload = {"name": fake.unique.name(), "bio": fake.paragraph()}
    author.name = payload["name"]
    author.bio = payload["bio"]
    assert author.name == payload["name"]
    assert author.bio == payload["bio"]


def test_update_genre_data(new_genre):
    """Test if updated data is stored successfully in the genre instance."""

    genre = new_genre()
    payload = {"name": fake.unique.name(), "description": fake.paragraph()}
    genre.name = payload["name"]
    genre.description = payload["description"]
    assert genre.name == payload["name"]
    assert genre.description == payload["description"]


def test_update_book_data(new_book, new_author, new_genre):
    """Test if updated data is stored successfully in the book instance."""

    book = new_book()
    payload, _, _ = generate_data_for_book(new_author, new_genre)

    book.title = payload["title"]
    book.author_id = payload["author_id"]
    book.genre_id = payload["genre_id"]
    book.publication_date = payload["publication_date"]
    book.description = payload["description"]

    assert book.title == payload["title"]
    assert book.author_id == payload["author_id"]
    assert book.genre_id == payload["genre_id"]
    assert book.publication_date == payload["publication_date"]
    assert book.description == payload["description"]
