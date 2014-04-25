#-*- coding:utf-8 -*-

'''from pyramid.config import Configurator
from sqlalchemy import create_engine

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings

from ..models import (
    DBSession,
    Base
    )
from familias import CustomRequest


import os
import unittest
from pyramid import testing
import transaction


def routes(config):
    config.add_route('pycicu-crop', '/ajax-upload/crop/')
    config.add_route('pycicu-upload', '/ajax-upload/')

class UnitTestViews(unittest.TestCase):    
    @classmethod
    def setUpClass(cls):
        from sqlalchemy import create_engine
        transaction.begin()

        folder = os.path.dirname(os.path.abspath(__file__))
        config_uri = os.path.join(folder,'../../','testing.ini')
        cls.settings = get_appsettings(config_uri)
        cls.engine = create_engine(cls.settings['sqlalchemy.url']) 
        DBSession.configure(bind=cls.engine)
        Base.metadata.create_all(cls.engine)

        transaction.commit()

    def setUp(self):
        transaction.begin()
        self.config = testing.setUp(settings=self.settings)
        self.config.include('pyramid_chameleon')
        
        self.config.include(routes, route_prefix='/pycicu/')

        self.config.set_request_factory(CustomRequest)

        self.config.add_static_view('static', 'familias:static', cache_max_age=3600)
        self.config.add_static_view('userfiles', 'familias:userfiles', cache_max_age=3600)
        self.config.add_static_view('deform', 'deform:static', cache_max_age=3600)
        self.config.scan()

    def tearDown(self):
        testing.tearDown()
        transaction.abort()

    @classmethod
    def tearDownClass(cls):
        transaction.begin()
        Base.metadata.drop_all(cls.engine)
        DBSession.remove()
        transaction.commit()


class MyMultiDict(list):
    """
    O MyMultiDict baseado em dict perde a ordem dos itens 
    e ela é usada pela lógica do colander/deform.
    """

    def getall(self, key, d=None):
        return self.get(key, d)
        
    def get(self, key, d=None):
        for p in self:
            if p[0] == key:
                if d is None:
                    return p[1]
        return None

    def items(self):
        return self

    def keys(self):
        return [p[0] for p in self]

    def values(self):
        return [p[1] for p in self]



class AuthDummyRequest(testing.DummyRequest):
    authenticated_userid = None
    unauthenticated_userid = None

    def __init__(self, *args, **kw):
        if 'userid' in kw:
            self.set_userid(kw['userid'])
        testing.DummyRequest.__init__(self, *args, **kw)
    def set_userid(self, id):
        self.authenticated_userid = id
        self.unauthenticated_userid = id'''

