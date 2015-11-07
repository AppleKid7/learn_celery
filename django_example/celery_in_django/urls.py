from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from jobs.views import Home

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='Home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
