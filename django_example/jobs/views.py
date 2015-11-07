from django.shortcuts import render
from django.views.generic import View

from celery.result import AsyncResult

from .tasks import fft_random

class Home(View):
    def get(self, request):
        if 'task_id' in request.session.keys():
            # That AsyncResult takes a constructor on
            # the task_id is super-convenient:
            t = AsyncResult(request.session['task_id'])
            request.session['task_state'] = t.state

        return render(request, 'home.html')

    def post(self, request):
        if 'ffts' in request.POST.keys():
            count = int(request.POST['ffts'])
            t = fft_random.delay(count)
            request.session['task_id'] = t.task_id
            request.session['task_state'] = t.state

        return render(request, 'home.html')

