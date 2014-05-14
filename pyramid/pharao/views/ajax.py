#-*- coding: utf-8 -*-

from pyramid.view import view_config
from ..backends import Postgresql


@view_config(name='schemas',
	         context="..resources.Resource",
	         renderer='json',
	         )
def schemas(request):
	dbname = request.POST.get('database', None)

	schemas = []
	cont = 1
	for s in Postgresql.schemas(database=dbname):
		schemas.append( {'id': '1%.6d'%cont, 'name': s[0], 'isParent': True, 'schema': s[0]} )
	return schemas

@view_config(name='tables',
	         context="..resources.Resource",
	         renderer='json',
	         )
def tables(request):
	dbname = request.POST.get('database', None)
	schema = request.POST.get('schema', None)
	tables = Postgresql.tables(database=dbname, schema=schema)
	return {'tables': tables}


