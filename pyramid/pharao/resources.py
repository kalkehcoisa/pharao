
from pyramid.security import Allow, ALL_PERMISSIONS, Authenticated, Deny, Everyone
import sqlalchemy as sa

class Resource(dict):
    __acl__ = [
            (Allow, Authenticated, 'view'),
            (Allow, 'g:admin', ALL_PERMISSIONS),
        ]

    def __init__(self, name, parent, **kw):
        self.__name__ = name
        self.__parent__ = parent
        for p in kw:
            setattr(self, p, kw[p])


class MenuResource(Resource):
	pass


def get_root(request):
    root = Resource('', None)

    #exemplo = ExemploResource('exemplo', root)
    #exemplo['um'] = UmResource('um', exemplo)
    #exemplo['outro'] = OutroResource('outro', exemplo)
    #root['exemplo'] = exemplo
    return root 
