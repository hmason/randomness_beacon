import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "randomness_beacon",
    version = "0.0.1",
    author = "Hilary Mason",
    author_email = "me@hilarymason.com",
    description = ("A wrapper for the NIST randomness beacon, a source of true random numbers"),
    license = "BSD",
    keywords = "NIST randomness beacon random numbers",
    url = "https://github.com/hmason/randomness_beacon",
    packages=['randomness_beacon'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
