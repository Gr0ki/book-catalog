# pylint: disable=duplicate-code
"""
Tests for book CRUD API.
"""

from faker import Faker

from ...book_catalog_app.service.serializers import (
    BookSchema,
    AuthorSchema,
    GenreSchema,
)
from ..shared.data_generation import generate_data_for_book

fake = Faker()


def test_get_book_details_success(client, new_book):
    """BookDetails.GET - 200"""

    book = new_book()
    response = client.get(f"/api/books/{book.id}")
    schema = BookSchema()
    expected_response = schema.dump(book)

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == expected_response


def test_get_book_details_404(client):
    """BookDetails.GET - 404"""

    response = client.get("/api/books/999")

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That book doesn't exist!"}


# __________________________________________________________


def test_get_book_list_success(client, new_book):
    """BookList.GET - 200"""

    book1 = new_book()
    book2 = new_book()
    response = client.get("/api/books")
    schema = BookSchema()
    expected_book1 = schema.dump(book1)
    expected_book2 = schema.dump(book2)
    expected_book1["id"] = book1.id
    expected_book2["id"] = book2.id

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert expected_book1 in response.json
    assert expected_book2 in response.json


# __________________________________________________________


def test_post_book_success(client, new_author, new_genre):
    """book.POST - 200"""

    payload, author, genre = generate_data_for_book(new_author, new_genre)
    payload["publication_date"] = payload["publication_date"].strftime("%Y-%m-%d")

    response = client.post("/api/books", content_type="application/json", json=payload)
    payload["id"] = response.json["id"]
    author_schema = AuthorSchema()
    genre_schema = GenreSchema()
    payload["author"] = author_schema.dump(author)
    payload["genre"] = genre_schema.dump(genre)

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == payload


def test_post_book_409_violation_unique_constrain(
    client, new_book, new_author, new_genre
):
    """book.POST - 409 (violation unique constrain for name)"""

    book = new_book()
    author = new_author()
    genre = new_genre()
    payload = {
        "title": book.title,
        "author_id": author.id,
        "genre_id": genre.id,
        "publication_date": fake.date_this_century().strftime("%Y-%m-%d"),
        "description": fake.paragraph(),
    }
    response = client.post(
        "/api/books",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 409
    assert response.content_type == "application/json"
    assert response.json == {
        "message": "A book with the same title value already exists."
    }


def test_post_book_400_unknown_field(client, new_book, new_author, new_genre):
    """book.POST - 400 (unknown field)"""

    book = new_book()
    author = new_author()
    genre = new_genre()
    payload = {
        "id": 1,
        "title": book.title,
        "author_id": author.id,
        "genre_id": genre.id,
        "publication_date": fake.date_this_century().strftime("%Y-%m-%d"),
        "description": fake.paragraph(),
    }
    response = client.post(
        "/api/books",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Unknown arguments: id"}


def test_post_book_400_empty_request_body(client):
    """book.POST - 400 (empty request body)"""

    response = client.post("/api/books", content_type="application/json", json={})

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Missing data for required field."}


# __________________________________________________________


def test_put_book_success(client, new_book):
    """book.PUT - 200"""

    book = new_book()
    payload = {
        "title": fake.unique.sentence(),
        "author_id": book.author_id,
        "genre_id": book.genre_id,
        "publication_date": fake.date_this_century().strftime("%Y-%m-%d"),
        "description": fake.paragraph(),
    }
    response = client.put(
        f"/api/books/{book.id}", content_type="application/json", json=payload
    )
    book_schema = BookSchema().dump(book)
    book_schema["title"] = payload["title"]
    book_schema["publication_date"] = payload["publication_date"]
    book_schema["description"] = payload["description"]

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == book_schema


def test_put_book_409_violation_unique_constrain(client, new_book):
    """book.PUT - 409 (violation unique constrain for name)"""

    book1 = new_book()
    book2 = new_book()
    payload = {
        "title": book1.title,
        "author_id": book2.author_id,
        "genre_id": book2.genre_id,
        "publication_date": fake.date_this_century().strftime("%Y-%m-%d"),
        "description": fake.paragraph(),
    }
    response = client.put(
        f"/api/books/{book2.id}",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 409
    assert response.content_type == "application/json"
    assert response.json == {
        "message": "A book with the same title value already exists."
    }


def test_put_book_404(client, new_book):
    """book.PUT - 404"""

    book = new_book()
    payload = {
        "title": fake.unique.sentence(),
        "author_id": book.author_id,
        "genre_id": book.genre_id,
        "publication_date": fake.date_this_century().strftime("%Y-%m-%d"),
        "description": fake.paragraph(),
    }
    response = client.put(
        "/api/books/999",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That book doesn't exist!"}


def test_put_book_400_unknown_field(client, new_book):
    """book.PUT - 400 (unknown field)"""

    book = new_book()
    payload = {
        "id": 1,
        "title": fake.unique.sentence(),
        "author_id": book.author_id,
        "genre_id": book.genre_id,
        "publication_date": fake.date_this_century().strftime("%Y-%m-%d"),
        "description": fake.paragraph(),
    }
    response = client.put(
        f"/api/books/{book.id}",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Unknown arguments: id"}


def test_put_book_400_empty_request_body(client, new_book):
    """book.PUT - 400 (empty request body)"""

    book = new_book()
    response = client.put(
        f"/api/books/{book.id}",
        content_type="application/json",
        json={},
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Missing data for required field."}


# # __________________________________________________________


def test_delete_book_success(client, new_book):
    """book.DELETE - 204"""

    book = new_book()
    response = client.delete(f"/api/books/{book.id}")

    assert response.status_code == 204
    assert response.content_type == "application/json"


def test_delete_book_404(client):
    """book.DELETE - 404"""

    response = client.delete("/api/books/999")

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That book doesn't exist!"}
