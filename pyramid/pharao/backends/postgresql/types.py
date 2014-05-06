#-*- coding: utf-8 -*-

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    class_mapper
    )

from sqlalchemy import types
from sqlalchemy.schema import Column
from sqlalchemy.orm import class_mapper


class BooleanString(types.TypeDecorator):
    impl = types.String

    def __init__(self, length=16):
        self.impl.length = length
        types.TypeDecorator.__init__(self, length=self.impl.length)

    def process_bind_param(self, value, dialect=None):
        if value == True:
            return 'YES'
        elif value == False:
            return 'NO'
        else:
            return None

    def process_result_value(self, value, dialect=None):
        if value == 'YES':
            return True
        elif value == 'NO':
            return False
        else:
        	return None

    def is_mutable(self):
        return False