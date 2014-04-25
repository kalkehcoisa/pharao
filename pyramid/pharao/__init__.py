#-*- coding: utf-8 -*-

from pyramid.config import Configurator
'''from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid
from pyramid.i18n import get_localizer
from pyramid.threadlocal import get_current_request
from pkg_resources import resource_filename
import deform

import pyramid_redis_session

from sqlalchemy import engine_from_config, Table

from .models.authentication import Usuario

from singleton import (MOBILE, USERFILES, MAC, MSSQL_USER,
        MSSQL_HOST, MSSQL_PASSWORD)

from .models.authentication import group_finder

from .resources import get_root

import uuid


class CustomRequest(Request):
    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        if userid is not None:
            return DBSession.query(Usuario).filter( Usuario.login==userid ).first()


def get_mac_address():
    return '-'.join('%02X' % ((uuid.getnode() >> 8*i) & 0xff) for i in reversed(xrange(6)))

def routes(config):
    config.add_route('pycicu-crop', '/ajax-upload/crop/')
    config.add_route('pycicu-upload', '/ajax-upload/')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    global MOBILE
    global USERFILES
    global MAC
    global MSSQL_USER
    global MSSQL_HOST
    global MSSQL_PASSWORD

    MOBILE = settings['familias.mobile'] == 'True'
    if MOBILE:
        MAC = get_mac_address()
    else:
        MSSQL_USER = settings['mssql.user']
        MSSQL_HOST = settings['mssql.host']
        MSSQL_PASSWORD = settings['mssql.password']

    USERFILES = settings['familias.userfiles']
    
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    authn_policy = AuthTktAuthenticationPolicy('^4VhV0sRwqZ' +
            'O-y_If{bea$+v;}qQKl-9.F>>4yM[RQv,lDCfO>cYp2N/gzQiq+R',
            callback=group_finder,
            hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings)
    session_factory = pyramid_redis_session.session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(get_root)
    config.include('pyramid_chameleon')
    config.add_translation_dirs(
            'colander:locale',
            'deform:locale')

    def translator(term):
        return get_localizer(get_current_request()).translate(term)

    deform_template_dir = resource_filename('deform', 'templates/')
    zpt_renderer = deform.ZPTRendererFactory(
            [deform_template_dir],
            translator=translator)
    deform.Form.set_default_renderer(zpt_renderer)
    
    config.include(routes, route_prefix='/pycicu/')
    
    config.set_request_factory(CustomRequest)

    config.add_static_view('static', 'familias:static', cache_max_age=3600)
    config.add_static_view('userfiles', 'familias:userfiles', cache_max_age=3600)
    config.add_static_view('deform', 'deform:static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()'''


import sqlalchemy
from .models import *
from pharao import models


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    
    MySession.configure(bind=mysql_engine)
    MyBase.metadata.bind = mysql_engine
    #Base.metadata.create_all(engine)

    #e("show tables").fetchall()

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
