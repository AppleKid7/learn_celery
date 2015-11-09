from celery import shared_task, current_task
from numpy import random
from scipy.fftpack import fft


@shared_task
def fft_random(n):
    """
    Brainless number crunching just to have a substantial task:
    """
    j = 0
    for i in range(n):
        x = random.normal(0, 0.1, 2000)
        y = fft(x)
        if i == int(j*n/20):
            j += 1
            print("j={}".format(j))
            current_task.update_state(state='PROGRESS',
                                      meta={'current': i, 'total': n})
    return random.random()
