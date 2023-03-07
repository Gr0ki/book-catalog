# **Book Catalog**

[![Build Status](https://app.travis-ci.com/Gr0ki/book-catalog.svg?token=pSdsQ1fKcT8fisi2WN4y&branch=main)](https://app.travis-ci.com/Gr0ki/book-catalog)
[![Coverage Status](https://coveralls.io/repos/github/Gr0ki/book-catalog/badge.svg?t=VooMEp)](https://coveralls.io/github/Gr0ki/book-catalog)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## **Documentation**

[Software Requirements Specification](./documentation/Software_Requirements_Specification.md)

## **Setup instruction**

### Docker compose:

1. Export some **environment variables** with your values, for example:

        export SECRET_KEY=1example4SECRET3key3
        export DB=mysql
        export DB_USER=example_user
        export DB_PASSWORD=example_password
        export MYSQL_ROOT_PASSWORD=example_root_user_password
        export DB_PORT=3306
        export DB_TEST_PORT=33062
        export DB_NAME=db_example
        export TEST_DB_NAME=test_db_example
        export COVERAGE_FILE=/home/app-user/book-catalog/.coverage

2. Set **DEV** to **"true"** if you want to test or check the linting of the app; otherwise, leave it blank or set it to **"false"**.

        export DEV=true

3. Build docker containers with a command:

        docker compose build

4. To run the app follow the next steps **\[optional\]**:

    - Apply migrations:

            docker compose run --rm app sh -c "flask db upgrade -d ./app/book_catalog_app/migrations"

    - Start the app:

            docker compose up

5. To run **tests** and **pylint** use the following command **\[optional\]**:

        docker-compose run --rm app sh -c "pylint ./app && ./app/wait_for_db.sh && pytest"
