#coding=utf-8

from django.conf.urls import include

from robots.utils import url


urlpatterns = [
    url(r'^profile', include('robots.tests.urls_profile')),
]
