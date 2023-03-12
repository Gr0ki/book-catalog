"""Contains Author API resorces."""
from flask_restful import Resource, reqparse

from ..service.models import Author, db
from ..service.serializers import AuthorSchema


class AuthorResource(Resource):
    """Author RESTful resource, supports the following requests:
    GET(list/detailed), POST, PUT, DELETE."""

    def __init__(self):
        """Parser setup."""
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument("name")
        self.parser.add_argument("bio")

    def get(self, author_id=None):
        """GET(list/detailed) Author[s] request handler."""
        if author_id:
            author = Author.query.get_or_404(
                author_id, description="That author doesn't exist!"
            )
            return AuthorSchema().dump(author)

        authors = Author.query.all()
        return AuthorSchema(many=True).dump(authors)

    def post(self):
        """POST Author request handler."""
        args = self.parser.parse_args(strict=True)

        if args["name"] is None or "name" not in args.keys():
            return {"message": "Missing data for required field."}, 400
        if len(Author.query.filter_by(name=args["name"]).all()) != 0:
            return {
                "message": "An Author with the same name value already exists."
            }, 409

        author = Author(name=args["name"], bio=args["bio"])
        db.session.add(author)
        db.session.commit()
        return AuthorSchema().dump(author)

    def put(self, author_id):
        """Author PUT request handler."""
        args = self.parser.parse_args(strict=True)

        name_condition = args["name"] is None or "name" not in args.keys()
        bio_condition = args["bio"] is None or "bio" not in args.keys()
        if name_condition or bio_condition:
            return {"message": "Missing data for required field."}, 400

        author = Author.query.get_or_404(
            author_id, description="That author doesn't exist!"
        )

        if (
            author.name != args["name"]
            and len(Author.query.filter_by(name=args["name"]).all()) != 0
        ):
            return {
                "message": "An Author with the same name value already exists."
            }, 409

        author.name = args["name"] or author.name
        author.bio = args["bio"] or author.bio
        db.session.commit()
        return AuthorSchema().dump(author)

    def delete(self, author_id):
        """Author DELETE request handler."""
        author = Author.query.get_or_404(
            author_id, description="That author doesn't exist!"
        )
        db.session.delete(author)
        db.session.commit()
        return "", 204
