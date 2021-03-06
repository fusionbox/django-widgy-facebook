import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-widgy-facebook',
    version='0.1',
    packages=['widgy_facebook'],
    include_package_data=True,
    license='BSD 2-Clause',
    description='A widget for integrating facebook posts in Widgy.',
    long_description=README,
    url='https://github.com/fusionbox/django-widgy-facebook',
    author='Fusionbox, Inc.',
    author_email='programmers@fusionbox.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.8',
        'django-widgy[all]'
    ]
)
