from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import settings
from . import views
from django.views.generic.base import TemplateView

from core.views import AboutView

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^cases/$', views.CasesView.as_view(), name='cases'),
    url(r'^cases/detail/(?P<pk>\d+)$', views.CaseDetailView.as_view(), name='detail'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
