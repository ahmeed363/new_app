# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in new_app/__init__.py
from new_app import __version__ as version

setup(
	name='new_app',
	version=version,
	description='newAhmed',
	author='Ahmed',
	author_email='aa@mm.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
