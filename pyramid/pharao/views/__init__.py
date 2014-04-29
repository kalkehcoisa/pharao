#-*- coding: utf-8 -*-

from pyramid.view import view_config
from ..models import (MySession, MyBase, mysql_engine)
from ..models import (PgSession, PgBase, pg_engine)
from pharao import models


@view_config(context="..resources.Resource",
			 renderer='pharao:templates/base.pt')
def home(request):
    connection = mysql_engine.connect()
    mysqldbs = [p[0] for p in connection.execute('SHOW DATABASES;').fetchall()]

    connection = pg_engine.connect()
    pgdbs = [p[0] for p in connection.execute("SELECT * FROM pg_database WHERE datistemplate = False;").fetchall()]

    #print( connection.execute("select column_name from INFORMATION_SCHEMA.COLUMNS where table_name = 'pg_database';").fetchall() )
    return {'project': 'Pharao', 'mysqldbs': mysqldbs, 'pgdbs': pgdbs}


@view_config(name='left_menu', 
			 context="..resources.Resource",
			 renderer='pharao:templates/left/menu.pt')
def left_menu(request):

    return {'project': 'Pharao'}
