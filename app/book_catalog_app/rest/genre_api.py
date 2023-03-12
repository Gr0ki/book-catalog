"""Contains Genre API resorces."""
from flask_restful import Resource, reqparse

from ..service.models import Genre, db
from ..service.serializers import GenreSchema


class GenreResource(Resource):
    """Genre RESTful resource, supports the following requests:
    GET(list/detailed), POST, PUT, DELETE."""

    def __init__(self):
        """Parser setup."""
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument("name")
        self.parser.add_argument("description")

    def get(self, genre_id=None):
        """GET(list/detailed) Genre[s] request handler."""
        if genre_id:
            genre = Genre.query.get_or_404(
                genre_id, description="That genre doesn't exist!"
            )
            return GenreSchema().dump(genre)

        genres = Genre.query.all()
        return GenreSchema(many=True).dump(genres)

    def post(self):
        """POST Genre request handler."""
        args = self.parser.parse_args(strict=True)
        if args["name"] is None or "name" not in args.keys():
            return {"message": "Missing data for required field."}, 400
        if len(Genre.query.filter_by(name=args["name"]).all()) != 0:
            return {"message": "A genre with the same name value already exists."}, 409
        genre = Genre(name=args["name"], description=args["description"])
        db.session.add(genre)
        db.session.commit()
        return GenreSchema().dump(genre)

    def put(self, genre_id):
        """Genre PUT request handler."""
        args = self.parser.parse_args(strict=True)

        name_condition = args["name"] is None or "name" not in args.keys()
        description_condition = (
            args["description"] is None or "description" not in args.keys()
        )
        if name_condition or description_condition:
            return {"message": "Missing data for required field."}, 400

        genre = Genre.query.get_or_404(
            genre_id, description="That genre doesn't exist!"
        )

        if (
            genre.name != args["name"]
            and len(Genre.query.filter_by(name=args["name"]).all()) != 0
        ):
            return {"message": "A genre with the same name value already exists."}, 409

        genre.name = args["name"] or genre.name
        genre.description = args["description"] or genre.description
        db.session.commit()
        return GenreSchema().dump(genre)

    def delete(self, genre_id):
        """Genre DELETE request handler."""
        genre = Genre.query.get_or_404(
            genre_id, description="That genre doesn't exist!"
        )
        db.session.delete(genre)
        db.session.commit()
        return "", 204
