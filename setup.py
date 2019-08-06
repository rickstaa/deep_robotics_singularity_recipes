# -*- coding: utf-8 -*-
"""
Setup file of the `panda_autograsp` python package. This setup file was based upon the gqcnn setup.py file.

Author
------
Rick Staa
"""

## Future Imports ##
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

## Standard library imports ##
import logging
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

## Package requirements ##
setup_requirements = []
requirements = []

## Set up logger. ##
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#################################################
## Setuo classes ################################
#################################################
class DevelopCmd(develop):
    """Overload :py:class:`setuptools.command.develop.develop` class."""

    ## Add extra user arguments ##
    user_options_custom = [
        ("docker", None, "installing in Docker"),
    ]
    user_options = getattr(develop, "user_options", []) + user_options_custom

    def initialize_options(self):
        """Initialize extra argument options."""
        develop.initialize_options(self)

        # Initialize options.
        self.docker = False

    def finalize_options(self):
        """Set extra install arguments."""
        develop.finalize_options(self)

    def run(self):
        """Overload the :py:meth:`setuptools.command.develop.develop.run` method."""

        ## Run parent run method ##
        develop.run(self)

class InstallCmd(install, object):
    """Overload :py:class:`setuptools.command.install.install` class"""

    ## Add extra user arguments ##
    user_options_custom = [
        ("docker", None, "installing in Docker"),
    ]
    user_options = getattr(install, "user_options", []) + user_options_custom

    def initialize_options(self):
        """Initialize extra argument options."""
        install.initialize_options(self)

        # Initialize options.
        self.docker = False

    def finalize_options(self):
        """Set extra argument options."""
        install.finalize_options(self)

    def run(self):
        """Overload the :py:meth:`setuptools.command.install.install.run` method."""

        ## Run parent run method ##
        install.run(self)

#################################################
## Setup script #################################
#################################################

## Get current package version ##
__version__ = "0.0.5"

## Run python setup ##
setup(
    name="deep_robotics_singularity_recipes",
    version=__version__,
    description=(
        "A HPC singularity recipe repository."),
    author="Rick Staa",
    author_email="rick.staa@outlook.com",
    license="Rick Staa Copyright",
    url="https://github.com/rickstaa/deep_robotics_singularity_recipes",
    keywords="robotics deep learning singularity containers hpc",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering"
    ],
    packages=find_packages(),
    include_package_data=True,
    setup_requires=setup_requirements,
    install_requires=requirements,
    extras_require={
        "docs": ["sphinx", "sphinxcontrib-napoleon", "sphinx_rtd_theme", "sphinx-navtree", "sphinx-autobuild", "docutils", "doc8"],
        "dev": ["pytest", "bumpversion"]
    },
    cmdclass={
        "install": InstallCmd,
        "develop": DevelopCmd
    }
)