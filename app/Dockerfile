FROM python:3.11.1-alpine3.17

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
RUN mkdir -p /app
COPY . /app
WORKDIR /app
EXPOSE 5000

ARG DEV=false
RUN pip install virtualenv && \
    virtualenv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apk add gcc musl-dev mariadb-connector-c-dev && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /venv/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    pip uninstall -y virtualenv distlib filelock platformdirs  && \
    apk del gcc musl-dev && \
    adduser \
    --disabled-password \
    --no-create-home \
    app-user

ENV PATH="/venv/bin:$PATH"

USER app-user