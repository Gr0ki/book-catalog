# pylint: disable=too-few-public-methods
"""
Flask app models
"""

from ..settings.extensions import db


class Author(db.Model):
    """An Author model"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    bio = db.Column(db.Text)
    books = db.relationship("Book", backref="author")

    def __repr__(self):
        """A human-readable representation of an Author oblect"""
        return f"Author: id={self.id}, name={self.name}"


class Genre(db.Model):
    """A Genre model"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    books = db.relationship("Book", backref="genre")

    def __repr__(self):
        """A human-readable representation of a Genre oblect"""
        return f"Genre: id={self.id}, name={self.name}"


class Book(db.Model):
    """A Book model"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    publication_date = db.Column(db.Date)
    description = db.Column(db.Text)

    def __repr__(self):
        """A human-readable representation of a Book oblect"""
        return f"Book: id={self.id}, title={self.title}"
