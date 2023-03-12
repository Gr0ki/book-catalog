# **Book Catalog**

[![Build Status](https://app.travis-ci.com/Gr0ki/book-catalog.svg?token=pSdsQ1fKcT8fisi2WN4y&branch=main)](https://app.travis-ci.com/Gr0ki/book-catalog)
[![Coverage Status](https://coveralls.io/repos/github/Gr0ki/book-catalog/badge.svg?branch=main&t=VooMEp)](https://coveralls.io/github/Gr0ki/book-catalog?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


The project contains `RESTful API` (see docs link below) and is supposed to contain template views (see `Software Requirements Specification` by following the link below), but this wasn't implemented yet.

There was CI process configured by using `Travis CI` (`pylint`, `pytest`, `coveralls`).

All models, serializers and API endpoints were `covered by tests`.

Also, there were configured `Gunicorn` and `Nginx`, `mysql` and `Flask` app in separate `docker` containers.

All used technologies, services, frameworks are listed in the "about" section (on the right side of this page).

## **Documentation**

[📚 Software Requirements Specification 📚](./documentation/Software_Requirements_Specification.md)

[📚 API documentation (Postman) 📚](https://documenter.getpostman.com/view/22115905/2s93JtQ3cR)

## **Setup instruction**

### Docker compose:

1. Export some **environment variables** with your values, for example:

    - **[Option 1]**: Export in the `.env` file:

            export SECRET_KEY=1example4SECRET3key3
            export DB=mysql
            export DB_USER=example_user
            export DB_PASSWORD=example_password
            export MYSQL_ROOT_PASSWORD=example_root_user_password
            export DB_PORT=3306
            export DB_TEST_PORT=33062
            export DB_NAME=db_example
            export TEST_DB_NAME=test_db_example
            export COVERAGE_FILE=/home/app-user/book-catalog/coverage/.coverage
            export COVERALLS_REPO_TOKEN=None

        And run docker compose by specifying path to env, for example (option 1):

            docker compose --env-file <path-to-env-file> <your command>

    - **[Option 2]**: Export env variables to your shell and use commands below without changes:

            export SECRET_KEY=1example4SECRET3key3 && export DB=mysql && export DB_USER=example_user && export DB_PASSWORD=example_password && export MYSQL_ROOT_PASSWORD=example_root_user_password && export DB_PORT=3306 && export DB_TEST_PORT=33062 && export DB_NAME=db_example && export TEST_DB_NAME=test_db_example && export DEV=true && export COVERAGE_FILE=/home/app-user/book-catalog/coverage/.coverage && export COVERALLS_REPO_TOKEN=None


2. Set `DEV` to `true` if you want to test or check the linting of the app; otherwise, leave it blank or set it to `false`.

        export DEV=true

3. Build docker containers with a command:

        docker compose build

4. To run the app follow the next steps (by running containers for the first time, don't forget to use `./app/wait_for_db.sh` script) **[optional]**:

    - Apply migrations:

            docker compose run --rm flask sh -c "flask db upgrade -d ./app/src/migrations"

    - Populate database with random data:

            docker compose run --rm flask sh -c "flask populate-db"

    - Start the app:

            docker compose up



5. To run `tests` and `pylint` use the following command **[optional]**:

        docker-compose run --rm flask sh -c "pylint ./app && ./app/wait_for_db.sh && pytest"


To sum up: by combining all the above, after exporting env variables, you can run the following script to build containers, migrate and populate db, and start the server all at once:

    docker compose build && docker compose run --rm flask sh -c "./app/wait_for_db.sh && flask db upgrade -d ./app/src/migrations && flask populate-db" && docker compose up