from django.shortcuts import render

from django.views.generic import View
from .tasks import fft_random

class Home(View):
    def get(self, request):
        return render(request, 'home.html', context={})

    def post(self, request):
        if 'ffts' in request.POST.keys():
            count = int(request.POST['ffts'])
            # Without the .delay, no task is performed.
            # fft_random(count)
            # With .delay, a task is sent to celery:
            fft_random.delay(count)

        print(request.POST)
        return render(request, 'home.html', context={})

