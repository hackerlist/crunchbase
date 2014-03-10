#-*- coding: utf-8 -*-

"""
    crunchbase
    ~~~~~~~~~~

    Setup
    `````
    $ pip install crunchbase
"""

import os
from distutils.core import setup

setup(
    name='crunchbase',
    version='0.0.1',
    url='http://github.com/hackerlist/crunchbase',
    author='mek',
    author_email='m@hackerlist.net',
    packages=[
        'crunchbase',
        'test'
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
        'requests >= 2.2.1',
    ],
    scripts=[
        "scripts/crunchbase"
        ],
    description="Crunchbase Python API",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
