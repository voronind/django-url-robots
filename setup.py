# -*- coding: utf-8 -*- 

from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name='django-robots',
    version='1.5alt',
    description='Django robots.txt generator',
    long_description=long_description,
    url='https://github.com/valeriansaliou/django-robots',
    author='Valérian Saliou',
    author_email='valerian@valeriansaliou.name',
    license='Python Software Foundation License',
    packages=['robots', 'robots.tests'],
    package_data={'robots': ['templates/*.*']},
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)