"""check_urls, hello_world and other stuff."""
from setuptools import setup, find_packages

setup(
    name="python_scripts",
    version="0.1",
    packages=find_packages(),
    scripts=['check_urls.py', 'hello_world.py', 'filter_lambda.py'],
)