from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name='django-url-robots',
    version='1.0.2',
    package_dir={'url_robots': 'url_robots'},
#    packages=['markitup_field', 'markitup_field.tests'],
#    packages=['markitup_field'],
#    py_modules=['markitup_field'],
    description='Django robots.txt generator',
    author='Dmitry Voronin',
    author_email='dimka665@gmail.com',
    license='Python Software Foundation License',
    url='http://github.com/dimka665/django-url-robots',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)