#-*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages


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
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
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
