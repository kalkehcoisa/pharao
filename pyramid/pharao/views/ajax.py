#-*- coding: utf-8 -*-

from pyramid.view import view_config
from .. import backends


@view_config(name='schemas',
	         context="..resources.Resource",
	         renderer='json',
	         )
def schemas(request):
	server_name = request.POST.get('server_name', None)
	dbname = request.POST.get('database', None)

	schemas = []
	cont = 1
	for s in backends.Servers['Postgresql'][server_name].schemas(database=dbname):
		schemas.append( {'id': '1%.6d'%cont, 'name': s[0], 'isParent': True, 'schema': s[0]} )
	return schemas


@view_config(name='tables',
	         context="..resources.Resource",
	         renderer='json',
	         )
def tables(request):
	server_name = request.POST.get('server_name', None)
	dbname = request.POST.get('database', None)
	schema = request.POST.get('schema', None)

	tables = []
	cont = 1
	for t in backends.Servers['Postgresql'][server_name].tables(database=dbname, schema=schema):
		tables.append( {'id': '1%.8d'%cont, 'name': t[0], 'isParent': True, 'schema': t[0]} )
	return {'tables': tables}





