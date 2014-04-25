#-*- coding: utf-8 -*-

class MockSession(object):

    def merge(self, record):
        pass

    def flush(self):
        pass

    def add(self, record):
        pass

class MockMixin(object):

    def to_appstruct(self):
        return dict([('a','a'),('b','b')])

    def log(self):
        return 'teste'

