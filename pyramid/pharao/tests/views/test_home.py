#-*- coding: utf-8 -*-

import unittest

from pyramid import testing
from .. import BaseUnitTests


class Tests(BaseUnitTests):
    
    def test_home(self):
        from ...views.home import home as view
        from ...resources import Resource

        request = testing.DummyRequest()
        request.context = Resource('', '')
        request.traversed = ('')
        response = view(request)
        self.assertTrue( 'tables' in response )
    
    def test_left_menu(self):
        from ...views.home import left_menu as view
        from ...resources import Resource

        request = testing.DummyRequest()
        request.context = Resource('', '')
        request.traversed = ('')
        response = view(request)
        self.assertTrue( 'tables' in response )

    def test_frame_home(self):
        from ...views.home import frame_home as view
        from ...resources import Resource

        request = testing.DummyRequest()
        request.context = Resource('', '')
        request.traversed = ('')
        response = view(request)
        self.assertTrue( 'tables' in response )

