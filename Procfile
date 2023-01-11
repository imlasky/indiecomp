release: python manage.py migrate
web: gunicorn config.wsgi:application
worker: REMAP_SIGTERM=SIGQUIT celery -A config worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery -A config beat --loglevel=info
