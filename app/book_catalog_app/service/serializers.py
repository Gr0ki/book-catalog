# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=too-many-ancestors
"""Serializers for declared app models."""

from ..settings.extensions import ma
from ..models.models import Genre, Author, Book


class GenreSchema(ma.SQLAlchemyAutoSchema):
    """Genre serializer."""

    class Meta:
        model = Genre
        load_instance = True
        dump_only = ("id",)


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    """Author serializer."""

    class Meta:
        model = Author
        load_instance = True
        dump_only = ("id",)


class BookSchema(ma.SQLAlchemyAutoSchema):
    """Book serializer."""

    class Meta:
        model = Book
        load_instance = True
        include_fk = True
        dump_only = ("id",)
