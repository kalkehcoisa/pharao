#-*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import ( scoped_session, sessionmaker)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session( sessionmaker(extension=ZopeTransactionExtension()) )
Base = declarative_base()

engine = sqlalchemy.create_engine('mysql+pymysql://pharao:1234@localhost')


'''class TempTable(Base):
    __tablename__= "temp_table"

    id = Column(Integer, primary_key=True)
    nome = Column(Unicode(20))
    texto = Column(String(10))

    def __str__(self):
        return u"%s, %s, id: %s" % (self.texto, self.nome, self.id)
    def __unicode__(self):
        return u"%s, %s, id: %s" % (self.texto, self.nome, self.id)'''