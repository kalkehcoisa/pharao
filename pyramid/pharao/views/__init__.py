#-*- coding: utf-8 -*-

from pyramid.view import view_config
from ..backends import Postgresql



@view_config(context="..resources.Resource",
			 renderer='pharao:templates/base.pt')
def home(request):
    #connection = mysql_engine.connect()
    #mysqldbs = [p[0] for p in connection.execute('SHOW DATABASES;').fetchall()]

    pgdbs = [p[0] for p in Postgresql.databases()]
    tables = Postgresql.tables(database='testes', schema='quack')

    print('\n\n')
    print(tables)
    print('\n\n')

    #print( connection.execute("select column_name from INFORMATION_SCHEMA.COLUMNS where table_name = 'pg_database';").fetchall() )
    return {'project': 'Pharao', 'mysqldbs': [], 'pgdbs': pgdbs}


@view_config(name='left_menu', 
			 context="..resources.Resource",
			 renderer='pharao:templates/left/menu.pt')
def left_menu(request):

    return {'project': 'Pharao'}


@view_config(name='frame_home', 
             context="..resources.Resource",
             renderer='pharao:templates/frames/home.pt')
def frame_home(request):

    return {'project': 'Pharao'}

