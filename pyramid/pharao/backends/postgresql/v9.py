#-*- coding: utf-8 -*-


import sqlalchemy
from sqlalchemy.orm import (scoped_session, sessionmaker)

from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
        Column,
        String,
        Unicode,
        DateTime,
        ForeignKey,
        Boolean,
        Integer,
        Table
        )
from .types import BooleanString


DBSession = scoped_session( sessionmaker(extension=ZopeTransactionExtension()) )
Base = declarative_base()


#TODO
#review the models and column types of all tables.
'''
#saves psql output to file
\o v9.txt
\d *
\q
'''

