#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='taiga-contrib-jwt-auth',
    version=":versiontools:taiga_contrib_jwt_auth:",
    description="The Taiga plugin for JWT authentication",
    long_description="",
    keywords='taiga, jwt, auth, plugin',
    author='Allan SIMON',
    author_email='allan.simon@supinfo.com',
    url='https://github.com/allan-simon/taiga-contrib-jwt-auth',
    license='AGPL',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'PyJWT',
        'cryptography',
        'django >= 1.7',
    ],
    setup_requires=[
        'versiontools >= 1.8',
    ],
    classifiers=[
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
