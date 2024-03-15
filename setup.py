"""check_urls, hello_world and other stuff"""
from setuptools import setup, find_packages

setup(
    name="python_scripts",
    version="0.1",
    packages=find_packages(),
    description='check_urls, hello_world and other stuff',
    author='Christian Hofmann',
    author_email='hofiorg@googlemail.com',
    url='https://github.com/hofiorg/python_scripts',
    install_requires=[
        'pylint',
        'requests',
        'pytest',
        'pytest-cov',
        'pytest-html'
    ],
    scripts=[
        'scripts/check_urls.py',
        'scripts/hello_world.py',
        'scripts/filter_lambda.py'
    ],
)
