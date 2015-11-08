from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View


from celery.result import AsyncResult

from .tasks import fft_random

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

@login_required
def profile_redirect(request):
    return HttpResponseRedirect(reverse('jobs:Profile', args=[request.user.username]))
    
    
class Profile(LoginRequiredMixin, View):
    def get(self, request, username):
        if 'task_id' in request.session.keys():
            # That AsyncResult takes a constructor on
            # the task_id is super-convenient:
            t = AsyncResult(request.session['task_id'])
            request.session['task_state'] = t.state

        return render(request, 'profile.html')

    def post(self, request, username):
        if 'ffts' in request.POST.keys():
            count = int(request.POST['ffts'])
            t = fft_random.delay(count)
            request.session['task_id'] = t.task_id
            request.session['task_state'] = t.state

        return render(request, 'profile.html')


class Home(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        return render(request, 'home.html')
