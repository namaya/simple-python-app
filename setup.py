
from setuptools import setup, find_packages

setup(
    name="simple-python-app",
    version="0.1.0",
    description="A simple python application.",
    packages=find_packages(exclude=["test*"]),
)
