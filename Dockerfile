FROM python:3.10-slim-buster
# This image contains the minimal necessary packages to run Python applications, 
# making it smaller and more suitable for containers where minimizing image size is a concern.

LABEL maintainer='rasifrazak123@gmail.com'
# This label is used to indicate the person or entity responsible for maintaining the Docker image.
#  It's commonly used to provide contact information for those who might have questions, issues, or contributions related to the image.

ENV PYTHONDONTWRITEBYTECODE 1
#  Prevents Python from writing pyc files to disc

ENV PYTHONUNBUFFERED 1
# The output generated by the application will be displayed immediately without buffering. 
# This can be helpful for debugging and monitoring the application's behavior.

COPY ./requirements.txt /tmp/requirements.txt
# This instruction copies the file requirements.txt from the local directory (where the Dockerfile is located),
#  into the /tmp directory within the Docker image.

COPY ./requirements.dev.txt /tmp/requirements.dev.txt
# This instruction copies the file requirements.dev.txt from the local directory (where the Dockerfile is located),
#  into the /tmp directory within the Docker image.

COPY ./app /app
# The WORKDIR /app line in a Dockerfile sets the working directory for subsequent commands within the Docker image. 
# It changes the default directory that commands will be executed in when you run the container based on the image.

WORKDIR /app
# It provides a way to specify the directory where commands, scripts, and other operations should be executed by default.

# ARG DEV=false
EXPOSE 8000



RUN apt-get update \
  &&  python -m venv /py \
  && /py/bin/pip install --upgrade pip \
  && apt-get install -y \
        libxrender1 \
        libxext6 \
        libfontconfig1 \
        libjpeg-dev \
        libpng-dev \
        libpq-dev \
        wkhtmltopdf \
  # psql client and dependencies for db backup
  && apt-get install -y wget gnupg2 \
  && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
  && apt-get update \
  && apt-get install -y postgresql-client-13 \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # Curl
  # && apt-get install -y curl unzip \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && /py/bin/pip install -r /tmp/requirements.txt \
  &&  if [ $DEV = "true" ]; \
   then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
   fi  \
  && rm -rf /tmp  \
  && adduser \
    --disabled-password \
    --no-create-home \
    django-user \
  && mkdir -p /log \
  && mkdir -p /vol/web/media \
  &&  mkdir -p /vol/web/static \
  && mkdir -p /backups \
  && mkdir -p /tmp/runtime-django-user \
  && chown -R django-user:django-user /tmp/runtime-django-user \
  && chown -R django-user:django-user /vol  \
  && chown -R django-user:django-user /app  \
  && chown -R django-user:django-user /log  \
  && chown -R django-user:django-user /backups  \
  && chmod -R 755 /vol \
  && chmod -R 755 /app \
  && chmod -R 777 /log \
  && chmod -R 777 /backups \
  && chmod a+w /backups \
  && chmod a+w /py/lib/python3.10/site-packages/django_celery_beat/migrations/


ENV XDG_RUNTIME_DIR=/tmp/runtime-django-user


ENV PATH="/py/bin:$PATH"
USER django-user
