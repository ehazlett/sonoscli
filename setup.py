#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1'
reqs = open('requirements.txt').read().splitlines()
setup(
    name='sonoscli',
    version=version,
    description='Sonos Music System CLI',
    url='http://github.com/ehazlett/sonoscli',
    download_url=('https://github.com/ehazlett/'
                  'sonoscli/archive/%s.tar.gz' % version),
    author='Evan Hazlett',
    author_email='ejhazlett@gmail.com',
    packages=[
        'sonoscli',
    ],
    entry_points={
        'console_scripts': [
            'sonoscli = sonoscli.cli:main',
        ],
    },
    install_requires = reqs,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        ]
)
