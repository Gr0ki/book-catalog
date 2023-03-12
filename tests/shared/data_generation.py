"""Contains reusable code for data generation in the tests."""

from faker import Faker


fake = Faker()


def generate_data_for_book(new_author, new_genre):
    """Generates data for the book. Returns payload, author and genre instances."""

    author = new_author()
    genre = new_genre()
    payload = {
        "title": fake.unique.sentence(),
        "author_id": author.id,
        "genre_id": genre.id,
        "publication_date": fake.date_this_century(),
        "description": fake.paragraph(),
    }
    return payload, author, genre
