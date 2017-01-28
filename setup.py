"""Packaging boilerplate for oeuvre."""
import os
import sys

import setuptools

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))  # noqa

import oeuvre

setuptools.setup(
    version=oeuvre.__version__,
    # We have to define classifiers here because setuptools will otherwise
    # error about `programming language` already being defined.
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
