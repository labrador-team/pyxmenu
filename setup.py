from setuptools import setup, find_packages

PACKAGE_NAME = 'pyargos'
PACKAGE_VERSION = '0.1.0'

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    author='Labrador Team',
    packages=find_packages(),
    requires=['typing', 'requests']
)
