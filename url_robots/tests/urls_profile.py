#coding=utf-8


from url_robots.utils import url

urlpatterns = [
    url(r'^s$', lambda x: (), name='profiles', robots_allow=True),
    url(r'^/(?P<nick>\w+)$', lambda x: ()),
    url(r'^/(?P<nick>\w+)/private', lambda x: (), name='profile_private', robots_allow=False),
    url(r'^/(?P<nick>\w+)/public', lambda x: (), name='profile_public', robots_allow=True),
    ]