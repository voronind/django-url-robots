=========================
django-url-robots
=========================

``Django`` ``robots.txt`` generator. Based on using decorated ``django.conf.urls.defaults.url``

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

    urlpatterns += patterns('',
        url(r'^robots.txt$', 'url_robots.views.robots_txt'),
        )

4. Describe rules by boolean keyword arguments ``robots_allow`` and ``robots_disallow`` using for it ``url_robots.utils.url`` instead ``django.conf.urls.defaults.url``::

    from url_robots.utils import url
    
    urlpatterns += patterns('',
       url('^profile/private$', 'view', robots_disallow=True),
       )
 
``django-url-robots`` tested with ``Django-1.3``

Settings
====================

In this moment there are only one option to define template of ``robots.txt`` file::

    urlpatterns += patterns('',
        url(r'^robots.txt$', 'url_robots.views.robots_txt', {'template': 'my_awesome_robots_template.txt'}),
        )

Example
===================
robots_template.txt::

    User-agent: *
    Disallow: /*  # disallow all
    {{ rules|safe }}

urls.py::

    from django.conf.urls.defaults import patterns, include

    urlpatterns = patterns('',
        url(r'^profile', include('url_robots.tests.urls_profile')),
    )

urls_profile.py::

    from django.conf.urls.defaults import patterns
    from url_robots.utils import url

    urlpatterns = patterns('',
        url(r'^s$', 'view', name='profiles', robots_allow=True),
        url(r'^/(?P<nick>\w+)$', 'view'),
        url(r'^/(?P<nick>\w+)/private', 'view', name='profile_private', robots_disallow=True),
        url(r'^/(?P<nick>\w+)/public', 'view', name='profile_public', robots_allow=True),
        )

Resulting robots.txt::

    User-agent: *
    Disallow: /*  # disallow all
    Allow: /profiles$
    Disallow: /profile/*/private*
    Allow: /profile/*/public*

