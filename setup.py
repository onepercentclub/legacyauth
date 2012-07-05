from setuptools import setup, find_packages


setup(
    name='legacyauth',
    version='0.1',
    author='1%CLUB',
    author_email='info@1procentclub.nl',
    packages=find_packages(),
    url='https://github.com/onepercentclub/legacyauth/',
    description='Legacy authentication module for the 1%CLUB.',
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.4",
    ],
)