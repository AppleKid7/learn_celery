from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from jobs.views import Home, profile_redirect


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='Home'),
    url(r'^accounts/',
        include('registration.backends.simple.urls')),
    url(r'^accounts/profile/',
        profile_redirect,
        name='redirect_to_profile'),
    url(r'^(?P<username>[A-Za-z0-9]+)/',
        include('jobs.urls', namespace='jobs')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
