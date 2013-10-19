#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1'
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
    install_requires = [
        "argparse>=1.2.1",
        "clint>=0.3.1",
        "requests>=2.0.0",
        "soco>=0.6.0",
    ],
    dependency_links = [
        "https://github.com/SoCo/SoCo/archive/master.zip",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        ]
)
