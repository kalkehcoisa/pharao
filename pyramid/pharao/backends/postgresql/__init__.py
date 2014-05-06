#-*- coding: utf-8 -*-

import sqlalchemy
from .v8_4 import *


#connection = pg_engine.connect()
#pgdbs = [p[0] for p in connection.execute("SELECT * FROM pg_database WHERE datistemplate = False;").fetchall()]

engine = sqlalchemy.create_engine('postgresql://pharao:1234@localhost/postgres')
DBSession.configure(bind=engine)
Base.metadata.bind = engine
