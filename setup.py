#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

is_release = False
if "--release" in sys.argv:
    is_release = True
    sys.argv.remove("--release")

base = os.path.dirname(os.path.abspath(__file__))

README_PATH = os.path.join(base, "README.rst")

install_requires = [
    "attrs",
    "clint",
    "coloredlogs",
    "docopt",
    "gitpython",
    "py",
    "verboselogs",
]

tests_require = []

setup(
    name="surgen",
    setup_requires=["vcver"],
    vcver={"is_release": is_release, "path": base},
    description=(
        "a utility library to help provide api route "
        "generation form function signature for web "
        "frameworks."
    ),
    long_description=open(README_PATH).read(),
    author="Yusuke Tsutsumi",
    author_email="yusuke@tsutsumi.io",
    url="https://github.com/toumorokoshi/surgen",
    # data_files=data_files,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Software Distribution",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    tests_require=tests_require,
    entry_points={"console_scripts": ["surgen=surgen.main:main"]},
)
