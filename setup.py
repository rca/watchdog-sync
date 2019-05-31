#!/usr/bin/env python
import configparser
import os

from setuptools import setup

entry_points = {
    'console_scripts': [
        # 'bar = testpackage.console_scripts:bar',
    ],
}

scripts = [
    'scripts/watchdog-sync',
]

def get_required_packages():
    """
    Returns the packages used for install_requires

    This used to pin down every package in Pipfile.lock to the version, but that, in turn, broke
    downstream projects because it was way too strict.

    Now, this simply grabs all the items listed in the `Pipfile` `[packages]` section without version
    pinning
    """
    config = configparser.ConfigParser()
    config.read('Pipfile')

    install_requires = sorted([x for x in config['packages']])

    return install_requires

setup(
    name='watchdog-sync',
    url='https://github.com/rca/watchdog-sync',
    author='Roberto Aguilar',
    author_email='roberto.c.aguilar@gmail.com',
    version='0.0.0',
    # package_dir={'': 'src'},
    packages=[],
    scripts=scripts,
    entry_points=entry_points,
    install_requires=get_required_packages()
)
