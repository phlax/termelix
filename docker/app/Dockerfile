FROM debian:latest

# setup Debian
COPY ./setup.sh /app/
RUN DEBIAN_FRONTEND=noninteractive /app/setup.sh

# setup Django
COPY ./setup-django.sh /app/
RUN DEBIAN_FRONTEND=noninteractive sudo -u app bash -c "./app/setup-django.sh"
