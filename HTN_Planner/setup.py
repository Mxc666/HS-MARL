#!/usr/bin/env python

from distutils.core import setup

setup(name='hipop',
      version='9.0',
      description='Hierarchical Partial-Order Planner',
      author='Charles Lesire, Alexandre Albore',
      author_email='charles.lesire@onera.fr, alexandre.albore@onera.fr',
      packages=['hipop', 'hipop.search', 'hipop.utils', 'hipop.grounding', 'hipop.plan'],
      zip_safe=False,
      #scripts=['bin/hipop-shop.py', 'bin/hipop-search.py', 'bin/hipop-pop.py'],
      )
