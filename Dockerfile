FROM python:3.11.1-alpine3.17

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN addgroup -S appgroup && \
    adduser -S app-user -G appgroup

RUN mkdir -p /home/app-user/book-catalog
WORKDIR /home/app-user/book-catalog

COPY ./app/requirements.txt /tmp/requirements.txt
COPY ./app/requirements.dev.txt /tmp/requirements.dev.txt

ARG DEV=${DEV}

RUN pip install virtualenv && \
    virtualenv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apk add gcc musl-dev mariadb-connector-c-dev && \
    apk add git && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /venv/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    pip uninstall -y virtualenv distlib filelock platformdirs  && \
    apk del gcc musl-dev && \
    chown -R app-user:appgroup /home/app-user/book-catalog/

ENV PATH="/venv/bin:$PATH"

EXPOSE 5000

USER app-user