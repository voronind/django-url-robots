from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name='django-url-robots',
    version='2.0',
    description='Django robots.txt generator',
    long_description=long_description,
    url='http://github.com/dimka665/django-url-robots',
    author='Dmitry Voronin',
    author_email='dimka665@gmail.com',
    license='Python Software Foundation License',
    packages=['url_robots', 'url_robots.tests'],
    package_data={'url_robots': ['templates/*.*']},
    platforms=["any"],
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
