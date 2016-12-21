#coding=utf-8

from django.conf.urls import include

from url_robots.utils import url


urlpatterns = [
    url(r'^profile', include('url_robots.tests.urls_profile')),
]
