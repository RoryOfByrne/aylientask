from setuptools import setup, find_packages

setup(
    name="paint", 
    version="0.1.0",
    install_requires=['django', 'django-rest-framework'],
    packages=find_packages(),
    scripts=['scripts/manage.py'] # makes manage.py available on the PATH
)