#!/usr/bin/env python3

from celery import Celery
from numpy import random
from scipy.fftpack import fft

app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
    CELERY_MESSAGE_COMPRESSION='gzip',
    CELERY_IGNORE_RESULT=False,
)


@app.task
def add(x, y):
    return x + y


@app.task
def fft_random(n):
    """
    This is just a huge number crunching task so that progress reporting won't be meaningless:
    """
    #fft_random.backend.mark_as_started(fft_random.request.id, progress=0)
    for i in range(n):
        x = random.normal(0, 0.1, 2000)
        y = fft(x)
