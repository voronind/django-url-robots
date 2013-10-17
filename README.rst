=========================
django-robots
=========================

``Django`` ``robots.txt`` generator. Based on using decorated ``django.conf.urls.url``.
It gets ``urlpatterns`` and replaces ambiguous parts by ``*``.

Installation & Usage
=========================

The recommended way to install django-robots is with `pip <http://pypi.python.org/pypi/pip>`_

1. Install from PyPI with ``easy_install`` or ``pip``::

    pip install git+https://github.com/valeriansaliou/django-robots

2. Add ``'robots'`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'robots',
        ...
        )

3. Add robots view to your root URLconf::

    urlpatterns += patterns('',
        url(r'^robots\.txt$', 'robots.views.robots_txt'),
        )

4. Describe rules by boolean keyword argument ``robots_allow`` using for it ``robots.utils.url`` instead ``django.conf.urls.url``::

    from robots.utils import url
    
    urlpatterns += patterns('',
       url('^profile/private$', 'view', robots_allow=False),
       )
 
``django-robots`` tested with ``Django-1.3``. Encodes unicode characters by percent-encoding.

Settings
====================

In this moment there are only one option to define template of ``robots.txt`` file::

    urlpatterns += patterns('',
        url(r'^robots\.txt$', 'robots.views.robots_txt', {'template': 'my_awesome_robots_template.txt'}),
        )

Example
===================
robots_template.txt::

    User-agent: *
    Disallow: /*  # disallow all
    {{ rules|safe }}

urls.py::

    from django.conf.urls import patterns, include

    urlpatterns = patterns('',
        url(r'^profile', include('robots.tests.urls_profile')),
    )

urls_profile.py::

    from django.conf.urls import patterns
    from robots.utils import url

    urlpatterns = patterns('',
        url(r'^s$', 'view', name='profiles', robots_allow=True),
        url(r'^/(?P<nick>\w+)$', 'view'),
        url(r'^/(?P<nick>\w+)/private', 'view', name='profile_private', robots_allow=False),
        url(r'^/(?P<nick>\w+)/public', 'view', name='profile_public', robots_allow=True),
        )

Resulting robots.txt::

    User-agent: *
    Disallow: /*  # disallow all
    Allow: /profiles$
    Disallow: /profile/*/private*
    Allow: /profile/*/public*

