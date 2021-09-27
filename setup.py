#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "unityagents==0.4.0",
    "numpy~=1.19.5",
    "dynaconf~=3.1",
    "jinja2~=3.0.1",
]

test_requirements = []

setup(
    author="Juan Carlos Calvo Jackson",
    author_email="juancarlos.calvo@quantumblack.com",
    python_requires="~=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    description="1rst project of the Udacity nanodegree program",
    entry_points={
        "console_scripts": [
            "navigation=navigation.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="navigation",
    name="navigation",
    packages=find_packages(include=["navigation", "navigation.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/juan-carlos-calvo/navigation",
    version="0.2.0",
    zip_safe=False,
    dependency_links=["unityagents"],
)
