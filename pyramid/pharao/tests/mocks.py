#-*- coding: utf-8 -*-

from pyramid import testing

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
        return 'test'


class MockMultiDict(list):
    """
    Used to 
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
        self.unauthenticated_userid = id

