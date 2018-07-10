#!venvserver/bin/python

"""
Author Notes:
Please don't execute this script separately. Use 'install_server' instead.
This script assumes that venvserver virtual environment has already been created before this script was actually executed.
"""

__author__ = 'Saurav Kumar'
__title__ = 'setup_server'
__version__ = '1.0'

import os
from distutils.core import setup
from setuptools import find_packages

# Allow setup_server.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements_server.txt') as reqs:
    install_requires = []
    for line in reqs.read().split('\n'):
        if (line and not line.startswith('#')):
            assert isinstance(install_requires, object)
            install_requires.append(line)

setup(name='kivyconnectserver',
      version='1.0',
      author='Saurav Kumar',
      author_email='saur.k10@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      url='https://github.org/sauravmahuri2007/kivyconnect.git',
      license='Proprietary',
      description='KivyConnectServer',
      classifiers=[
          'Environment :: System Environment',
          'Framework :: Flask',
      ],
      zip_safe=False,
      install_requires=install_requires,)