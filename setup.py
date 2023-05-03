"""
Setup script for the Aeryck Flask application.

This file uses setuptools to define the package name, version, dependencies, and other setup
configuration options for the Aeryck Flask application.

Args:
    None.

Returns:
    None.

Raises:
    None.

Usage:
    python setup.py install`

Dependencies:
    - flask (version >= 0.12)
    - Flask-Markdown (version >= 0.3)

"""
from setuptools import find_packages, setup

setup(
    name='aeryck',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'Flask-Markdown',
    ],
)
