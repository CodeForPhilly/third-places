FROM python:3.10-slim-bullseye

RUN mkdir -p /usr/local/src
WORKDIR /usr/local/src
COPY requirements.txt /usr/local/src/

ARG buildDeps=" build-essential libpq-dev"
ARG deps=" gdal-bin gettext postgresql-client"

RUN apt-get update && apt-get install -y $buildDeps $deps --no-install-recommends
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get purge -y --auto-remove $buildDeps
RUN rm -rf requirements.txt /var/lib/apt/lists/*

COPY . /usr/local/src
CMD ["python3", "manage.py", "runserver", "8321"]