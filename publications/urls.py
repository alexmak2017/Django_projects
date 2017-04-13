from django.conf.urls import url

from publications.views import publications, single_publication


urlpatterns = [
    url(r'^$', publications, name="publications"),
    url(r'^(?P<publication_id>[\d]+)$', single_publication, name="single_publication"),
    url(r'^(?P<publication_id>[\d]+)/likes$', single_publication, name="single_publication"),
]
