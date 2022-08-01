#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

INSTALL_REQUIRES = [
  'numpy',
  'scipy',
  'pandas',
  'ftfy',
  'xmltodict',
  'lxml',
  'xlsxwriter',
  'prettytable',
  'decorator',
  'watchdog',
  'requests',
  'python-pptx',
  'pyreadstat'
]


setup(name='quantipy3',
      version='0.3.0',
      author='Geir Freysson',
      author_email='geir@datasmoothie.com',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      install_requires=INSTALL_REQUIRES,
      )
