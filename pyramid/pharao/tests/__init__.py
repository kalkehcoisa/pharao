#-*- coding:utf-8 -*-

from pyramid.config import Configurator
from pyramid.paster import get_appsettings

import os
import unittest
from pyramid import testing
import transaction

from sqlalchemy import (create_engine, engine_from_config)
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class BaseUnitTests(unittest.TestCase):
    settings = None
    config = None
    engine = None

    @classmethod
    def setUpClass(cls):
        #TODO
        raise Exception('The tests aren\'t properly done and configured yet.')
        
        from sqlalchemy import create_engine
        transaction.begin()

        folder = os.path.dirname(os.path.abspath(__file__))
        config_uri = os.path.join(folder,'../../','testing.ini')
        cls.settings = get_appsettings(config_uri)
        cls.engine = create_engine(cls.settings['sqlalchemy.postgresql']) 
        DBSession.configure(bind=cls.engine)
        Base.metadata.create_all(cls.engine)

        transaction.commit()

    def setUp(self):
        transaction.begin()
        self.config = testing.setUp(settings=self.settings)
        self.config.include('pyramid_chameleon')

        self.config.set_request_factory(CustomRequest)

        self.config.add_static_view('static', 'pharao:static', cache_max_age=3600)
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


