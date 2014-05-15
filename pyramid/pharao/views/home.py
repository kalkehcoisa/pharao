#-*- coding: utf-8 -*-

from pyramid.view import view_config
from .. import backends


@view_config(context="..resources.Resource",
			 renderer='pharao:templates/base.pt')
def home(request):
    #for sgdb in backends.Servers.sgdbs():
    sgdbs = backends.Servers.sgdbs('Postgresql')
    #	sgdbs[(db_name+): [p[0] for p in sgbd.databases()]}
    return {'mysqldbs': [], 'sgdbs': sgdbs}

@view_config(name='left_menu', 
			 context="..resources.Resource",
			 renderer='pharao:templates/left/menu.pt')
def left_menu(request):
    return {}

@view_config(name='frame_home', 
             context="..resources.Resource",
             renderer='pharao:templates/frames/home.pt')
def frame_home(request):
    return {}

