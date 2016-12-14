#coding=utf-8


from robots.utils import url

urlpatterns = [
    url(r'^s$', 'view', name='profiles', robots_allow=True),
    url(r'^/(?P<nick>\w+)$', 'view'),
    url(r'^/(?P<nick>\w+)/private', 'view', name='profile_private', robots_allow=False),
    url(r'^/(?P<nick>\w+)/public', 'view', name='profile_public', robots_allow=True),
    ]