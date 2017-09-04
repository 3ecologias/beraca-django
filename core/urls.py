from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import settings
from . import views
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap

from core.views import AboutView

from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^cases/$', views.CasesView.as_view(), name='cases'),
    url(r'^cases/detail/(?P<pk>\d+)$', views.CaseDetailView.as_view(), name='detail'),
    url(r'^blog/$', views.BlogListView.as_view(), name='blog'),
    url(r'^blog/detail/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='post_detail'),
    url(r'^services/detail/(?P<pk>\d+)$', views.ServiceDetailView.as_view(), name='service_detail'),
    url(r'^robots.txt$', include('robots.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
