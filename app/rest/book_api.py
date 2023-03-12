"""Contains Book API resorces."""
from flask_restful import Resource, reqparse

from ..service.models import Book, db
from ..service.serializers import BookSchema


class BookResource(Resource):
    """Book RESTful resource, supports the following requests:
    GET(list/detailed), POST, PUT, DELETE."""

    def __init__(self):
        """Parser setup."""
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument("title")
        self.parser.add_argument("author_id")
        self.parser.add_argument("genre_id")
        self.parser.add_argument("publication_date")
        self.parser.add_argument("description")

    def get(self, book_id=None):
        """GET(list/detailed) Book[s] request handler."""
        if book_id:
            book = Book.query.get_or_404(
                book_id, description="That book doesn't exist!"
            )
            return BookSchema().dump(book)

        books = Book.query.all()
        return BookSchema(many=True).dump(books)

    def post(self):
        """POST Book request handler."""
        args = self.parser.parse_args(strict=True)

        if args["title"] is None or "title" not in args.keys():
            return {"message": "Missing data for required field."}, 400
        if len(Book.query.filter_by(title=args["title"]).all()) != 0:
            return {"message": "A book with the same title value already exists."}, 409

        book = Book(
            title=args["title"],
            author_id=args["author_id"],
            genre_id=args["genre_id"],
            publication_date=args["publication_date"],
            description=args["description"],
        )
        db.session.add(book)
        db.session.commit()
        return BookSchema().dump(book)

    def put(self, book_id):
        """Book PUT request handler."""
        args = self.parser.parse_args(strict=True)

        title_condition = args["title"] is None or "title" not in args.keys()
        author_id_condition = (
            args["author_id"] is None or "author_id" not in args.keys()
        )
        genre_id_condition = args["genre_id"] is None or "genre_id" not in args.keys()
        description_condition = (
            args["description"] is None or "description" not in args.keys()
        )
        if (
            title_condition
            or author_id_condition
            or genre_id_condition
            or description_condition
        ):
            return {"message": "Missing data for required field."}, 400

        book = Book.query.get_or_404(book_id, description="That book doesn't exist!")

        if (
            book.title != args["title"]
            and len(Book.query.filter_by(title=args["title"]).all()) != 0
        ):
            return {"message": "A book with the same title value already exists."}, 409

        book.title = args["title"]
        book.author_id = args["author_id"]
        book.genre_id = args["genre_id"]
        book.publication_date = args["publication_date"]
        book.description = args["description"]
        db.session.commit()
        return BookSchema().dump(book)

    def delete(self, book_id):
        """Book DELETE request handler."""
        book = Book.query.get_or_404(book_id, description="That book doesn't exist!")
        db.session.delete(book)
        db.session.commit()
        return "", 204
