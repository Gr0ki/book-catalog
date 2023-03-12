# pylint: disable=duplicate-code
"""
Tests for genre CRUD API.
"""

from faker import Faker

from app.service.serializers import GenreSchema

fake = Faker()


def test_get_genre_details_success(client, new_genre):
    """GenreDetails.GET - 200"""

    genre = new_genre()
    response = client.get(f"/api/genres/{genre.id}")
    schema = GenreSchema()
    expected_response = schema.dump(genre)

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == expected_response


def test_get_genre_details_404(client):
    """GenreDetails.GET - 404"""

    response = client.get("/api/genres/999")

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That genre doesn't exist!"}


# __________________________________________________________


def test_get_genre_list_success(client, new_genre):
    """GenreList.GET - 200"""

    genre1 = new_genre()
    genre2 = new_genre()
    response = client.get("/api/genres")
    schema = GenreSchema()
    expected_genre1 = schema.dump(genre1)
    expected_genre2 = schema.dump(genre2)
    expected_genre1["id"] = genre1.id
    expected_genre2["id"] = genre2.id

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert expected_genre1 in response.json
    assert expected_genre2 in response.json


# __________________________________________________________


def test_post_genre_success(client):
    """genre.POST - 200"""

    payload = {"name": fake.unique.word(), "description": "Test description"}
    response = client.post("/api/genres", content_type="application/json", json=payload)
    payload["id"] = response.json["id"]

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == payload


def test_post_genre_409_violation_unique_constrain(client, new_genre):
    """genre.POST - 409 (violation unique constrain for name)"""

    genre = new_genre()
    response = client.post(
        "/api/genres",
        content_type="application/json",
        json={"name": genre.name, "description": "Test description2"},
    )

    assert response.status_code == 409
    assert response.content_type == "application/json"
    assert response.json == {
        "message": "A genre with the same name value already exists."
    }


def test_post_genre_400_unknown_field(client):
    """genre.POST - 400 (unknown field)"""

    response = client.post(
        "/api/genres",
        content_type="application/json",
        json={"id": 1, "name": fake.unique.word(), "description": "Test description"},
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Unknown arguments: id"}


def test_post_genre_400_empty_request_body(client):
    """genre.POST - 400 (empty request body)"""

    response = client.post("/api/genres", content_type="application/json", json={})

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Missing data for required field."}


# __________________________________________________________


def test_put_genre_success(client, new_genre):
    """genre.PUT - 200"""

    genre = new_genre()
    payload = {"name": fake.unique.word(), "description": "Test description"}
    response = client.put(
        f"/api/genres/{genre.id}",
        content_type="application/json",
        json=payload,
    )
    payload["id"] = genre.id

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == payload


def test_put_genre_409_violation_unique_constrain(client, new_genre):
    """genre.PUT - 409 (violation unique constrain for name)"""

    genre1 = new_genre()
    genre2 = new_genre()
    payload = {"name": genre1.name, "description": "Test description"}
    response = client.put(
        f"/api/genres/{genre2.id}",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 409
    assert response.content_type == "application/json"
    assert response.json == {
        "message": "A genre with the same name value already exists."
    }


def test_put_genre_404(client):
    """genre.PUT - 404"""

    response = client.put(
        "/api/genres/999",
        content_type="application/json",
        json={"name": fake.unique.word(), "description": "Test description"},
    )

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That genre doesn't exist!"}


def test_put_genre_400_unknown_field(client, new_genre):
    """genre.PUT - 400 (unknown field)"""

    genre = new_genre()
    payload = {"id": 1, "name": fake.unique.word(), "description": "Test description"}
    response = client.put(
        f"/api/genres/{genre.id}",
        content_type="application/json",
        json=payload,
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Unknown arguments: id"}


def test_put_genre_400_empty_request_body(client, new_genre):
    """genre.PUT - 400 (empty request body)"""

    genre = new_genre()
    response = client.put(
        f"/api/genres/{genre.id}",
        content_type="application/json",
        json={},
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.json == {"message": "Missing data for required field."}


# __________________________________________________________


def test_delete_genre_success(client, new_genre):
    """genre.DELETE - 204"""

    genre = new_genre()
    response = client.delete(f"/api/genres/{genre.id}")

    assert response.status_code == 204
    assert response.content_type == "application/json"


def test_delete_genre_404(client):
    """genre.DELETE - 404"""

    response = client.delete("/api/genres/999")

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.json == {"message": "That genre doesn't exist!"}
