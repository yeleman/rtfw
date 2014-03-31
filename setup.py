#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

"""rtfw - Port of PyRTF 0.45: Rich Text Format Document Generation

PyRTF is a pure python module for the efficient generation of rich text format
documents. Supports styles, tables, cell merging, jpg and png images and tries
to maintain compatibility with as many RTF readers as possible. """

import  sys

from distutils.core import setup

classifiers = """\
Development Status :: 4 - Beta
Topic :: Text Editors :: Text Processing
Topic :: Software Development :: Libraries :: Python Modules
Intended Audience :: Developers
Programming Language :: Python
License :: OSI Approved :: GNU General Public License (GPL)
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
"""

if sys.version_info < (2, 3):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

doclines = __doc__.split("\n")

setup(name = 'rtfw',
      version = '0.2',
      author = 'Renaud Gaudin, Simon Cusack (original)',
      author_email = 'rgaudin@gmail.com',
      url = 'https://pypi.python.org/pypi/rtfw',
      license = 'http://www.gnu.org/licenses/gpl.html',
      install_requires = ['python-magic>=0.4.6', 'rtfunicode'],
      platforms = ['Any'],
      description = doclines[0],
      classifiers = filter(None, classifiers.split('\n')),
      long_description = '\n'.join(doclines[2:]),
      keywords = ('RTF',
                  'Rich Text',
                  'Rich Text Format',
                  'documentation',
                  'reports'),
      packages = ['rtfw'],
      package_dir = { '' : '.' })
