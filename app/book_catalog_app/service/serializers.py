# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=too-many-ancestors
"""Serializers for declared app models."""

from marshmallow.fields import Nested
from marshmallow import ValidationError

from ..settings.extensions import ma
from .models import Genre, Author, Book


class GenreSchema(ma.SQLAlchemyAutoSchema):
    """Serializer for Genre model."""

    class Meta:
        model = Genre
        load_instance = True
        ordered = True

    id: int = ma.auto_field(dump_only=True)
    name: str = ma.auto_field()
    description: str = ma.auto_field()


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    """Serializer for Author model."""

    class Meta:
        model = Author
        load_instance = True
        ordered = True

    id: int = ma.auto_field(dump_only=True)
    name: str = ma.auto_field()
    bio: str = ma.auto_field()


class BookSchema(ma.SQLAlchemyAutoSchema):
    """Serializer for Book model."""

    class Meta:
        model = Book
        load_instance = True
        ordered = True

    id: int = ma.auto_field(dump_only=True)
    title: str = ma.auto_field()
    author_id: int = ma.auto_field()
    genre_id: int = ma.auto_field()
    publication_date: str = ma.auto_field()
    description: str = ma.auto_field()
    author: AuthorSchema = Nested("AuthorSchema", dump_only=True)
    genre: GenreSchema = Nested("GenreSchema", dump_only=True)

    def validate_author_id(self, value):
        """Confirm that referenced Author exists."""
        author = Author.query.get(value)
        if author is None:
            raise ValidationError("Author does not exist")

    def validate_genre_id(self, value):
        """Confirm that referenced Genre exists."""
        genre = Genre.query.get(value)
        if genre is None:
            raise ValidationError("Genre does not exist")
