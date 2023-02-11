#!/usr/bin/env python3

# Copyright 2013 Bootlin

#
"""Build tar.gz for pdf-link-checker

Required packages:
    python-pdfminer
    pdfminer-data # recommended for encoding data needed to read some PDF documents
                  # in CJK (Chinese, Japanese, Korean) languages.
"""

from setuptools import setup

setup(
    name='pdf-link-checker',
    version='1.2.0',
    description='Reports broken hyperlinks in PDF documents',
    long_description=open('README.rst').read(),

    author='Ezequiel Garcia',
    author_email='ezequiel.garcia@bootlin.com',
    license='GPL-2',

    url='https://github.com/bootlin/pdf-link-checker',
    scripts=['bin/pdf-link-checker'],
    install_requires=['pdfminer'],
)
