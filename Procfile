release: python manage.py migrate
web: gunicorn config.wsgi:application
worker: REMAP_SIGTERM=SIGQUIT celery -A config.celery worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery -A config.celery beat --loglevel=info