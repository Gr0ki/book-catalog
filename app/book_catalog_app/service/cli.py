"""Custom Flask CLI commands to manage tables and their data."""

import click
from flask.cli import with_appcontext
from faker import Faker

from app.book_catalog_app.models.models import Author, Book, Genre
from ..settings.extensions import db

fake = Faker()


@click.command("populate-db")
@with_appcontext
def populate_db_command():
    """Populate the database with mock data."""
    # Create some fake authors
    authors = []
    for _ in range(10):
        author = Author(name=fake.name(), bio=fake.paragraph())
        db.session.add(author)
        authors.append(author)
    db.session.commit()

    # Create some fake genres
    genres = []
    for _ in range(5):
        genre = Genre(name=fake.word(), description=fake.paragraph())
        db.session.add(genre)
        genres.append(genre)
    db.session.commit()

    # Create some fake books
    for _ in range(50):
        book = Book(
            title=fake.sentence(),
            author=fake.random_element(authors).id,
            publication_date=fake.date_this_century(),
            description=fake.paragraph(),
        )
        # Add some random genres to the book
        book.genres.extend(fake.random_elements(genres, unique=True))
        db.session.add(book)
    db.session.commit()

    print("Mock data added to the database!")


@click.command("db-drop-all")
@with_appcontext
def db_drop_all_command():
    """Drop all database tables."""
    db.drop_all()

    print("All tables has been droped.")
