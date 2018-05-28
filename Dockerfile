
FROM python:3.4

ENV VERSION 0.1

WORKDIR /usr/src/app

ENV APP_NAME smbackend 

RUN apt-get update && \
  apt-get install -y libpython3.4-dev libyaml-dev libxml2-dev \
  libxslt1-dev binutils libproj-dev gdal-bin python-gdal \
  postgresql-9.4-postgis-2.1 libpq-dev python-psycopg2 gettext

COPY requirements.txt .
COPY deploy/requirements.txt ./deploy/requirements.txt

RUN pip install --no-cache-dir -r deploy/requirements.txt

COPY . .

RUN cp deploy/local_settings.py .

CMD deploy/server.sh

