#!/usr/bin/env python

from setuptools import setup

setup(
    name='konnected',
    version='1.1.0',
    packages=['konnected'],
    url='https://github.com/konnected-io/konnected-py',
    description='A async Python library for interacting with Konnected home automation controllers (see https://konnected.io)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nate Clark, Konnected Inc',
    author_email='help@konnected.io',
    install_requires=['aiohttp>=3.6.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ],
    project_urls={
      'Homepage': 'https://github.com/konnected-io/konnected-py',
      'Website & Online Store': 'https://konnected.io',
      'Support and Community Forums': 'https://help.konnected.io',
      'Facebook': 'https://facebook.com/konnected.io',
      'YouTube Channel': 'https://youtube.com/c/Konnected'
    }
)
