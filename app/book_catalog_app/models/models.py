# pylint: disable=too-few-public-methods
"""
Flask app models
"""

from ..settings.extensions import db


book_genre = db.Table(
    "book_genre",
    db.Column("book_id", db.Integer, db.ForeignKey("book.id"), primary_key=True),
    db.Column("genre_id", db.Integer, db.ForeignKey("genre.id"), primary_key=True),
)


class Author(db.Model):
    """An Author model"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.Text)
    books = db.relationship("Book", backref="book_author")

    def __str__(self):
        """A human-readable representation of an Author oblect"""
        return f"Author: id={self.id}, name={self.name}"


class Book(db.Model):
    """A Book model"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("author.id"))
    genres = db.relationship(
        "Genre", secondary=book_genre, backref=db.backref("books", lazy=True)
    )
    publication_date = db.Column(db.Date)
    description = db.Column(db.Text)

    def __str__(self):
        """A human-readable representation of a Book oblect"""
        return f"Book: id={self.id}, title={self.title}"


class Genre(db.Model):
    """A Genre model"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __str__(self):
        """A human-readable representation of a Genre oblect"""
        return f"Genre: id={self.id}, name={self.name}"
