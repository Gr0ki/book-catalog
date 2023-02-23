from setuptools import setup, find_packages

setup(
    name="book-catalog-app",
    version="1.0.0",
    description="""The Book Catalog is a web application that allows
reading, writing, updating, and deleting books, genres, and authors.
It provides HTML forms and REST API to perform these actions on stored data.
The application also offers an opportunity to search books by published dates
in API and Forms.""",
    packages=find_packages(),
    install_requires=(
        "Flask",
        "Flask-SQLAlchemy",
        "python-dotenv",
        "mysqlclient"
    )
)
