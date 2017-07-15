import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="rdoclient-py3",
    version="2.0.1",
    author="RANDOM.ORG (original library), "
           "nicorellius (Python 3 implementation)",
    author_email="nicorellius@protonmail.com",
    description="RANDOM.ORG JSON-RPC API (release 2) Python 3 implementation.",
    license="MIT",
    keywords="RANDOM.ORG random client implementation",
    url="https://github.com/nicorellius/json-rpc-python3",
    packages=['rdoclient_py3'],
    python_requires='>=3',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
