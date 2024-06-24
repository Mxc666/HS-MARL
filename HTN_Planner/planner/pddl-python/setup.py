#!/usr/bin/env python
"""PDDL parser setup file."""

from distutils.core import setup

setup(name='pddl',
      version='1.0',
      description='PDDL Parser library',
      author='Charles Lesire',
      author_email='charles.lesire@onera.fr',
      packages=['pddl', 'pddl.parser'],
      zip_safe=False,
      )
