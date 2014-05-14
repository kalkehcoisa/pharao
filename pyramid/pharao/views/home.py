#-*- coding: utf-8 -*-

from pyramid.view import view_config
from ..backends import Postgresql


@view_config(context="..resources.Resource",
			 renderer='pharao:templates/base.pt')
def home(request):
    pgdbs = [p[0] for p in Postgresql.databases()]
    return {'mysqldbs': [], 'pgdbs': pgdbs}

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

