from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^politicians/$', views.PoliticianList.as_view(), name='politician-list'),
    url(r'^politicians/(?P<slug>[a-zA-Z\-0-9]+)/?$', views.PoliticianDetail.as_view(), name='politician-detail'),
]