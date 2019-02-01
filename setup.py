#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io

from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='neue-fische-bank-app',
    version='0.1.0',
    license='MIT license',
    description='Neue Fische - Bank App',
    long_description=read('README.md'),
    author='Manuel Wiedenmann',
    author_email='manuel@funkensturm.de',
    url='https://github.com/fsmanuel/nf-bank-app',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
)
