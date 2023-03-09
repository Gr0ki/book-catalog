"""Create Book, Genre, Author and book_genre tables.

Revision ID: 7cdc76e3ece7
Revises:
Create Date: 2023-03-07 17:44:38.467435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7cdc76e3ece7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "author",
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("bio", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "genre",
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "book",
        sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("author", sa.Integer(), nullable=True),
        sa.Column("publication_date", sa.Date(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author"],
            ["author.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "book_genre",
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.Column("genre_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["book_id"],
            ["book.id"],
        ),
        sa.ForeignKeyConstraint(
            ["genre_id"],
            ["genre.id"],
        ),
        sa.PrimaryKeyConstraint("book_id", "genre_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("book_genre")
    op.drop_table("book")
    op.drop_table("genre")
    op.drop_table("author")
    # ### end Alembic commands ###
