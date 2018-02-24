
apt update
apt install -q -yy \
        sudo \
        virtualenv \
        git

useradd --shell /bin/bash -c "" -m app
chown -R app:app /app
