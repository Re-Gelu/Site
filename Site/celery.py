import os

from celery import Celery

from django_celery_results.apps import CeleryResultConfig
from django_celery_beat.apps import BeatConfig
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Site.settings')

celery_broker = os.environ.get("REDIS_URL", default='redis://localhost:6379/0')

app = Celery('Site', broker=celery_broker)

#print("CELERY BROKER IS: ", celery_broker)
      
app.config_from_object('Site.settings')
app.autodiscover_tasks()

app.conf.update(result_extended=True)
app.conf.timezone = 'Europe/Moscow'

CeleryResultConfig.verbose_name = "Результаты Celery"
BeatConfig.verbose_name = "Периодические задачи"