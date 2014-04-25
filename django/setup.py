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
    'django>=1.6',
    'psycopg2>=2.5.1',
    ]

setup(name='django-pharao',
      version='0.1',
      description='django-pharao',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg django postgresql mysql',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='django-pharao',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = django-pharao:main
      [console_scripts]
      initialize_pharao_db = django-pharao.scripts.initializedb:main
      """,
      )
