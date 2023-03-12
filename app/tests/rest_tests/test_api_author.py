# pylint: disable=duplicate-code
"""
Tests for Author CRUD API.
"""

from faker import Faker

from ...book_catalog_app.service.serializers import AuthorSchema

fake = Faker()


def test_get_author_details_success(client, new_author):
    """AuthorDetails.GET - 200"""

    author = new_author()
    response = client.get(f"/api/authors/{author.id}")
    schema = AuthorSchema()
    expected_response = schema.dump(author)

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == expected_response


def test_get_author_details_404(client):
    """AuthorDetails.GET - 404"""

    response = client.get("/api/authors/999")

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That author doesn't exist!"}


# __________________________________________________________


def test_get_author_list_success(client, new_author):
    """AuthorList.GET - 200"""

    author1 = new_author()
    author2 = new_author()
    response = client.get("/api/authors")
    schema = AuthorSchema()
    expected_author1 = schema.dump(author1)
    expected_author2 = schema.dump(author2)
    expected_author1["id"] = author1.id
    expected_author2["id"] = author2.id

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert expected_author1 in response.json
    assert expected_author2 in response.json


# __________________________________________________________


def test_post_author_success(client):
    """Author.POST - 200"""

    payload = {"name": fake.unique.name(), "bio": "Test bio"}
    response = client.post(
        "/api/authors", content_type="application/json", json=payload
    )
    payload["id"] = response.json["id"]

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == payload


def test_post_author_409_violation_unique_constrain(client, new_author):
    """Author.POST - 409 (violation unique constrain for name)"""

    author = new_author()
    response = client.post(
        "/api/authors",
        content_type="application/json",
        json={"name": author.name, "bio": "Test bio2"},
    )

    assert response.status_code == 409
    assert response.content_type == "application/json"
    assert response.json == {
        "message": "An Author with the same name value already exists."
    }


def test_post_author_400_unknown_field(client):
    """Author.POST - 400 (unknown field)"""

    response = client.post(
        "/api/authors",
        content_type="application/json",
        json={"id": 1, "name": fake.unique.name(), "bio": "Test bio"},
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Unknown arguments: id"}


def test_post_author_400_empty_request_body(client):
    """Author.POST - 400 (empty request body)"""

    response = client.post("/api/authors", content_type="application/json", json={})

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Missing data for required field."}


# __________________________________________________________


def test_put_author_success(client, new_author):
    """Author.PUT - 200"""

    author = new_author()
    payload = {"name": fake.unique.name(), "bio": "Test bio"}
    response = client.put(
        f"/api/authors/{author.id}",
        content_type="application/json",
        json=payload,
    )
    payload["id"] = author.id

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == payload


def test_put_author_409_violation_unique_constrain(client, new_author):
    """Author.PUT - 409 (violation unique constrain for name)"""

    author1 = new_author()
    author2 = new_author()
    payload = {"name": author1.name, "bio": "Test bio"}
    response = client.put(
        f"/api/authors/{author2.id}",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 409
    assert response.content_type == "application/json"
    assert response.json == {
        "message": "An Author with the same name value already exists."
    }


def test_put_author_404(client):
    """Author.PUT - 404"""

    response = client.put(
        "/api/authors/999",
        content_type="application/json",
        json={"name": fake.unique.name(), "bio": "Test bio"},
    )

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That author doesn't exist!"}


def test_put_author_400_unknown_field(client, new_author):
    """Author.PUT - 400 (unknown field)"""

    author = new_author()
    payload = {"id": 1, "name": fake.unique.name(), "bio": "Test bio"}
    response = client.put(
        f"/api/authors/{author.id}",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Unknown arguments: id"}


def test_put_author_400_empty_request_body(client, new_author):
    """Author.PUT - 400 (empty request body)"""

    author = new_author()
    response = client.put(
        f"/api/authors/{author.id}",
        content_type="application/json",
        json={},
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Missing data for required field."}


# __________________________________________________________


def test_delete_author_success(client, new_author):
    """Author.DELETE - 204"""

    author = new_author()
    response = client.delete(f"/api/authors/{author.id}")

    assert response.status_code == 204
    assert response.content_type == "application/json"


def test_delete_author_404(client):
    """Author.DELETE - 404"""

    response = client.delete("/api/authors/999")

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That author doesn't exist!"}
