import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market_stream.settings")

app = Celery("market_stream")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
