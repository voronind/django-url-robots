=========================
django-url-robots
=========================

``Django`` ``robots.txt`` generator. Based on using decorated ``django.conf.urls.url``.
It gets ``urlpatterns`` and replaces ambiguous parts by ``*``.

Installation & Usage
=========================

The recommended way to install django-url-robots is with `pip <http://pypi.python.org/pypi/pip>`_

1. Install from PyPI with ``easy_install`` or ``pip``::

    pip install django-url-robots

2. Add ``'url_robots'`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'url_robots',
        ...
        )

3. Add url_robots view to your root URLconf::

    urlpatterns += [
        url(r'^robots\.txt$', url_robots.views.robots_txt),
        ]

4. Describe rules by boolean keyword argument ``robots_allow`` using for it ``url_robots.utils.url`` instead ``django.conf.urls.url``::

    from url_robots.utils import url
    
    urlpatterns += [
       url('^profile/private$', views.some_view, robots_allow=False),
       ]
 
``django-url-robots`` tested with ``Django-1.8+``. Encodes unicode characters by percent-encoding.

Settings
====================

In this moment there are only one option to define template of ``robots.txt`` file::

    urlpatterns += [
        url(r'^robots\.txt$', url_robots.views.robots_txt, {'template': 'my_awesome_robots_template.txt'}),
        ]

Example
===================
robots_template.txt::

    User-agent: *
    Disallow: /*  # disallow all
    {{ rules|safe }}

urls.py::

    from django.conf.urls import include

    urlpatterns = [
        url(r'^profile', include('url_robots.tests.urls_profile')),
    ]

urls_profile.py::

    from url_robots.utils import url

    urlpatterns = [
        url(r'^s$', views.some_view, name='profiles', robots_allow=True),
        url(r'^/(?P<nick>\w+)$', views.some_view),
        url(r'^/(?P<nick>\w+)/private', views.some_view, name='profile_private', robots_allow=False),
        url(r'^/(?P<nick>\w+)/public', views.some_view, name='profile_public', robots_allow=True),
        ]

Resulting robots.txt::

    User-agent: *
    Disallow: /*  # disallow all
    Allow: /profiles$
    Disallow: /profile/*/private*
    Allow: /profile/*/public*

