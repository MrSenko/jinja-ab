#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

config = {
    'name' : 'jinja-ab',
    'version' : '0.2.1',
    'packages' : find_packages(),
    'author' : 'Mr. Senko',
    'author_email' : 'atodorov@mrsenko.com',
    'license' : 'BSD',
    'description' : 'Support A/B testing for Jinja2 templates',
    'long_description' : long_description,
    'url' : 'https://github.com/MrSenko/jinja-ab',
    'keywords' : ['A/B testing', 'Jinja2'],
    'classifiers' : [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    'zip_safe' : False,
    'install_requires' : ['Jinja2'],
}

setup(**config)
