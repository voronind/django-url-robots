#coding=utf-8

from django.conf.urls import patterns, include

from url_robots.utils import url


urlpatterns = patterns('',
    url(r'^profile', include('url_robots.tests.urls_profile')),
)
