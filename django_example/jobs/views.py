from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View


from celery.result import AsyncResult

from .tasks import fft_random
from .models import JobModel


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


@login_required
def profile_redirect(request):
    return HttpResponseRedirect(reverse('jobs:Profile',
                                        args=[request.user.username]))


class Profile(LoginRequiredMixin, View):
    def get(self, request, username):
        jobUIDs = JobModel.objects.filter(user=request.user)

        async_results = []
        active_job = False
        jobs = []
        for UID in jobUIDs:
            task = AsyncResult(UID.task_id)
            async_results.append(task)
            j = {'state': task.state,
                 'submission_time': UID.submission_time}

            if task.state in ['PENDING', 'STARTED', 'PROGRESS']:
                active_job = True
                j['result'] = 'unknown'
                j['progress'] = 1

                if task.state == 'PROGRESS':
                    j['progress'] = int(100.0*float(task.info['current'])/float(task.info['total']))

            elif task.state == 'SUCCESS':
                j['result'] = task.result
            else:
                j['result'] = 'unknown'
                j['progress'] = 1

            jobs.append(j)

        context = {'jobs': jobs}

        if active_job:
            request.session['active_job'] = True
        else:
            request.session['active_job'] = False

        return render(request, 'profile.html', context=context)

    def post(self, request, username):
        if 'ffts' in request.POST.keys():
            count = int(request.POST['ffts'])
            task = fft_random.delay(count)
            job = JobModel(user=request.user, task_id=task.task_id)
            job.save()

        return HttpResponseRedirect(reverse('jobs:Profile',
                                            args=[request.user.username]))


class Home(View):
    def get(self, request):
        return render(request, 'home.html')
