import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_in_django.settings')

from django.conf import settings
from celery import Celery

app = Celery('celery_in_django',
             backend='amqp',
             broker='amqp://guest@localhost//')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
