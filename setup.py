#!/usr/bin/env python

import os
import sys

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

license = """
MIT License
Copyright (c) 2018 Konnected Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

long_description = """
View details and usage examples in the `README.md <https://github.com/konnected-io/konnected-py> on GitHub`_.
For device support see `help.konnected.io <https://help.konnected.io>`_.
"""

setup(
    name='konnected',
    version='0.1.2',
    packages=['konnected'],
    url='https://github.com/konnected-io/konnected-py',
    license=license,
    description='A Python library for interacting with Konnected home automation controllers (see https://konnected.io)',
    long_description=long_description,
    author='Nate Clark, Konnected Inc',
    author_email='help@konnected.io',
    install_requires=['requests>=2.0'],
    project_urls={
      'Homepage': 'https://github.com/konnected-io/konnected-py',
      'Website & Online Store': 'https://konnected.io',
      'Help, Support and Community Forums': 'https://help.konnected.io',
      'Facebook': 'https://facebook.com/konnected.io/',
      'YouTube Channel': 'https://youtube.com/c/Konnected'
    }
)