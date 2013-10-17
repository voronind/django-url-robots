#coding=utf-8

from django.conf.urls import patterns, include

from robots.utils import url


urlpatterns = patterns('',
    url(r'^profile', include('robots.tests.urls_profile')),
)
