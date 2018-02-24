
cd /app
virtualenv . --python=python3
. bin/activate

pip install -U pip setuptools
git clone https://github.com/phlax/termelix
cd termelix
pip install -e .
pip install -r docker/app/requirements.txt
./manage.py
