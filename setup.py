from setuptools import setup

Version = "0.0.2"

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(name='CalCalc',
    version=Version,
    license='MIT',
    py_modules=["CalCalc"],
    package_dir={'':'CalCalc'},
    long_description=long_description,
    )