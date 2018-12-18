import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pasport_mo.settings')

app = Celery('pasport_mo')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
