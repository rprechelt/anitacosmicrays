from os import path
from setuptools import setup, find_packages

# the anitacosmicrays version
__version__ = "0.0.1"

# get the absolute path of this project
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# the standard setup info
setup(
    name="anitacosmicrays",
    version=__version__,
    description=("A Python package to access reduced data products "
                 "of cosmic ray events observed by ANITA."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rprechelt/anitacosmicrays",
    author="Remy L. Prechelt",
    author_email="prechelt@hawaii.edu",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["anita", "cosmic rays", "physics", "radio"],
    packages=["anitacosmicrays"],
    python_requires=">=3.6*, <4",
    install_requires=["numpy", "cachetools"],
    extras_require={
        "test": ["pytest", "black", "mypy",
                 "coverage", "pytest-cov", "flake8"],
    },
    scripts=[],
    project_urls={},
    include_package_data=True,
)
