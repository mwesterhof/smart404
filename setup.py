#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

install_requires = [
    'Django>=1.11',
]

test_require = [
    # For coverage and PEP8 linting
    # TODO: check if all these are needed
    'coverage>=3.7.0',
    'flake8>=2.2.0',
    'isort>=4.2.0',
    'tox>=2.3.1',
    'cryptography==1.4',
    'PyYAML==3.11',
    'bumpversion==0.5.3',
    'wheel==0.29.0',
    'watchdog==0.8.3',
]

docs_require = [
    'sphinx',
    'sphinx_rtd_theme',
]

setup(
    name='smart404',
    version='0.1',
    description="A django module to provide review and redirection of 404 urls from the admin", # NOQA
    long_description=readme + '\n\n' + changelog,
    author="Marco Westerhof",
    author_email='m.westerhof@lukkien.com',
    url='',  # TODO
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=install_requires,
    license='MIT',
    zip_safe=False,
    keywords='smart404',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    extras_require={
        'testing': test_require,
        'docs': docs_require,
    },
)
