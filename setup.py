#!/usr/bin/env python
from setuptools import find_packages, setup

AUTHOR = __import__('flatcountries').__author__
EMAIL = __import__('flatcountries').__email__
LICENSE = __import__('flatcountries').__license__
VERSION = __import__('flatcountries').__version__


setup(
    name='flatcountries',
    version=VERSION,
    url='https://github.com/danie1k/flatcountries',
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
    ],
    platforms=[
        'OS Independent',
    ],
    packages=find_packages(),
)
