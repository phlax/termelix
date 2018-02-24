#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""termelix
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages


install_requires = []
extras_require = {}
extras_require['test'] = [
    "pytest",
    "pytest-mock",
    "requests_mock",
    "coverage",
    "pytest-coverage",
    "codecov",
    "flake8"],

setup(
    name='termelix',
    version='0.0.1',
    description='termelix',
    long_description="termelix",
    url='https://github.com/translate/makeyfile',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 5 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Programming Language :: Python :: 2.7',
    ],
    keywords='termelix',
    install_requires=install_requires,
    extras_require=extras_require,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True)
