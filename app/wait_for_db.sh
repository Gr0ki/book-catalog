#!/bin/sh

# Wait until MySQL is ready
while ! nc -z db 3306; do
    echo "Trying to connect to MySQL at 3306..."
    sleep 5
done

