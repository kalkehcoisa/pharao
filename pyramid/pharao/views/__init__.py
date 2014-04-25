#-*- coding: utf-8 -*-

from pyramid.view import view_config
from ..models import (MySession, MyBase, mysql_engine)
from ..models import (PgSession, PgBase, pg_engine)
from pharao import models


@view_config(route_name='home', renderer='pharao:templates/mytemplate.pt')
def my_view(request):
    connection = mysql_engine.connect()
    mysqldbs = connection.execute('SHOW DATABASES;').fetchall()

    connection = pg_engine.connect()
    pgdbs = connection.execute('select datname as database from pg_database;').fetchall()

    return {'project': 'Pharao', 'mysqldbs': mysqldbs, 'pgdbs': pgdbs}