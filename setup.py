#!/usr/bin/env python
from distutils.core import setup

setup(
	name='iougen',
	version='0.1',
	description='Python library to generate Cisco IOU licenses',
	author='Brandon Bennett',
	author_email='bennetb@gmail.com',
	license='BSD',
	packages=['iougen'],
	scripts=['bin/iougen'])