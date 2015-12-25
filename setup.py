#!/usr/bin/env python3

import os
import sys
import platform
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "stratotraffic",
    version = "1.0",
    packages = [],
    scripts = ["scripts/stratotraffic"],
    install_requires = ["docopt", "requests", "Pillow"],
    author = "Felix \"KoffeinFlummi\" Wiegand",
    author_email = "koffeinflummi@gmail.com",
    description = "Script to read/unlock strato.de server traffic/speed.",
    long_description = read("README.md"),
    license = "MIT",
    keywords = "",
    url = "https://github.com/KoffeinFlummi/stratotraffic",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities"
    ]
)
