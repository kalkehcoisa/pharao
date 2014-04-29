#-*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

__author__ = 'Jayme Tosi Neto'

extra = {}
if sys.version_info >= (3,):
  pass

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, '../README.txt')).read()
CHANGES = open(os.path.join(here, '../CHANGES.txt')).read()

requires = [
    'pyramid>=1.5a2',
    'pyramid_chameleon>=0.1',
    'pyramid_tm>=0.7',
    'pyramid_deform==0.2',
    'pyramid_debugtoolbar>=0.1',
    'SQLAlchemy>=0.9.3',
    'psycopg2>=2.5.1',
    'PyMySQL',
    'deform>=2.0a2',
    'waitress>=0.8.8',
    'zope.sqlalchemy',
    ]

setup(name='pharao',
      version='0.1.1.1',
      description='pharao',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        #https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Programming Language :: Python",
        "Framework :: Pyramid",
        'Development Status :: 2 - Pre-Alpha',

        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        'Topic :: Software Development :: Libraries',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ],
      author='Jayme Tosi Neto',
      author_email='kalkehcoisa@gmail.com',
      url='',
      keywords='web wsgi bfg pylons pyramid postgresql mysql',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pharao',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pharao:main
      [console_scripts]
      initialize_pharao_db = pharao.scripts.initializedb:main
      """,
      )
