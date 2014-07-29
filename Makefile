# Makefile - gevsckio

# These targets are not files
.PHONY: req db setup run gunicorn

req:
	@pip install -r requirements.txt

db:
	@python manage.py syncdb --noinput

setup: req db

run:
	@python manage.py socketio_runserver --nopsyco

gunicorn:
	@gunicorn gevsckio.wsgi:application
