# Python file for the Python Setuptools

from setuptools import setup
from os import path

# Setting the content of README.md to the long description 
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ChildCare',
    version='0.0.1',
    description='Python library to get \
                statistical data about \
                the child care situation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/runningturtles/ChildCare.git',
    author='runningturtles',
    author_email='wangxn@gmx.com',
    license='unlicense',
    packages=['ChildCare']
)
