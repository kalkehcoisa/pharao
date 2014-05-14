#-*- coding: utf-8 -*-

import unittest

from pyramid import testing
from .. import BaseUnitTests

class Tests(BaseUnitTests):
    def test_home(self):
        from ...views import home
        from ...resources import Resource

        request = testing.DummyRequest()
        request.context = Resource('', '')
        request.traversed = ('')
        response = home(request)
        self.assertTrue( 'pgdbs' in response )

    def test_schemas(self):
        from ..views import schemas
        from ...resources import Resource

        request = testing.DummyRequest()
        request.context = Resource('', '')
        request.traversed = ('')
        response = schemas(request)
        self.assertTrue( 'schemas' in response )

    def test_tables(self):
        from ..views import tables
        from ...resources import Resource

        request = testing.DummyRequest()
        request.context = Resource('', '')
        request.traversed = ('')
        response = tables(request)
        self.assertTrue( 'tables' in response )




