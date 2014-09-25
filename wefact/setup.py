#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-wefact-api',
    version='1.0',
    description='Python bindings to talk to the Wefact API',
    author='Mark Schouten',
    author_email='mark@tuxis.nl',
    url='https://github.com/tuxis-ie/misc/tree/master/wefact/',
    license='GPL',
    py_modules=['wefact.api'],
    package_dir={'': 'python'},
    platforms=['linux'],
    data_files=[
    ]
)

