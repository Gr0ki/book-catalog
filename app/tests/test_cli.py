# pylint: disable=redefined-outer-name
# pylint: disable=unused-import
"""
Tests for custom Flask CLI commands.
"""

from click.testing import CliRunner
from sqlalchemy import inspect

from .conftest import app
from ..book_catalog_app.settings.extensions import db
from ..book_catalog_app.models.models import Book, Author, Genre
from ..book_catalog_app.service.cli import populate_db_command, db_drop_all_command


def test_populate_db_command(app):
    """Test creating new rows in the db tables with the 'db-drop-all' custom cli command.
    (exit code, print message, new data existence in each table)"""

    runner = CliRunner()
    result = runner.invoke(populate_db_command)
    assert result.exit_code == 0
    assert "Mock data added to the database!" in result.output

    with app.app_context():
        # Check if the authors, genres, and books were created
        assert Author.query.count() == 10
        assert Genre.query.count() == 5
        assert Book.query.count() == 50


def test_drop_tables(app):
    """Test if tables were successfully deleted with the'db-drop-all' custom cli command.
    (exit code, print message, tables existence)"""
    runner = CliRunner()
    result = runner.invoke(db_drop_all_command)
    assert result.exit_code == 0
    assert "All tables has been droped." in result.output

    with app.app_context():
        inspector = inspect(db.engine)
        assert len(inspector.get_table_names()) == 0
