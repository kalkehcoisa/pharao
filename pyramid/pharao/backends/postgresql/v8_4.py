#-*- coding: utf-8 -*-


import sqlalchemy
from sqlalchemy.orm import (scoped_session, sessionmaker)

from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
        Column,
        String,
        Unicode,
        DateTime,
        ForeignKey,
        Boolean,
        Integer,
        Table
        )
from .types import BooleanString


DBSession = scoped_session( sessionmaker(extension=ZopeTransactionExtension()) )
Base = declarative_base()

#TODO
#review the models and column types of all tables.
'''
#saves psql output to file
\o v8_4.txt
\d *
\q
'''

######## Schema - information_schema ########
class SqlFeatures(Base):
    __tablename__= "sql_features"
    __table_args__ = {"schema": "information_schema"}

    feature_id = Column(Unicode, primary_key=True)
    feature_name = Column(Unicode)
    sub_feature_id = Column(Integer)
    sub_feature_name = Column(Unicode)
    is_supported = Column(BooleanString)
    is_verified_by = Column(BooleanString)
    comments = Column(Unicode)

    def __str__(self):
        return ""
    def __unicode__(self):
        return u""


class SqlImplementationInfo(Base):
    __tablename__= "sql_implementation_info"
    __table_args__ = {"schema": "information_schema"}

    implementation_info_id = Column(Integer, primary_key=True)
    implementation_info_name = Column(Unicode)
    integer_value = Column(Integer)
    character_value = Column(Unicode)
    comments = Column(Unicode)

    def __str__(self):
        return ""
    def __unicode__(self):
        return u""


class SqlLanguages(Base):
    __tablename__= "sql_languages"
    __table_args__ = {"schema": "information_schema"}
    #__mapper_args__ = {"primary_key":(col1, col2)}}

    #TODO
    #set the correct column types
    sql_language_source = Column(Unicode)
    sql_language_year = Column(Unicode)
    sql_language_conformance = Column(Unicode)
    sql_language_integrity = Column(Unicode)
    sql_language_implementation = Column(Unicode)
    sql_language_binding_style = Column(Unicode)
    sql_language_programming_language = Column(Unicode)

    def __str__(self):
        return ""
    def __unicode__(self):
        return u""

class SqlPackages(Base):
    __tablename__= "sql_packages"
    __table_args__ = {"schema": "information_schema"}

    #TODO
    #set the correct column types
    feature_id = Column(Unicode)
    feature_name = Column(Unicode)
    is_supported = Column(Unicode)
    is_verified_by = Column(Unicode)
    comments = Column(Unicode)

    def __str__(self):
        return ""
    def __unicode__(self):
        return u""

class SqlParts(Base):
    __tablename__= "sql_parts"
    __table_args__ = {"schema": "information_schema"}

    #TODO
    #set the correct column types
    feature_id = Column(Unicode)
    feature_name = Column(Unicode)
    is_supported = Column(Unicode)
    is_verified_by = Column(Unicode)
    comments = Column(Unicode)

    def __str__(self):
        return ""
    def __unicode__(self):
        return u""

class SqlSizing(Base):
    __tablename__= "sql_sizing"
    __table_args__ = {"schema": "information_schema"}

    #TODO
    #set the correct column types
    sizing_id = Column(Unicode)
    sizing_name = Column(Unicode)
    supported_value = Column(Unicode)
    comments = Column(Unicode)

    def __str__(self):
        return ""
    def __unicode__(self):
        return u""

class SqlSizingProfile(Base):
    __tablename__= "sql_sizing_profiles"
    __table_args__ = {"schema": "information_schema"}

    #TODO
    #set the correct column types
    sizing_id = Column(Unicode)
    sizing_name = Column(Unicode)
    profile_id = Column(Unicode)
    required_value = Column(Unicode)
    comments = Column(Unicode)

    def __str__(self):
        return ""
    def __unicode__(self):
        return u""


'''
                        List of relations
       Schema       |          Name           | Type  |  Owner   
--------------------+-------------------------+-------+----------
 pg_catalog         | pg_aggregate            | table | postgres
 pg_catalog         | pg_am                   | table | postgres
 pg_catalog         | pg_amop                 | table | postgres
 pg_catalog         | pg_amproc               | table | postgres
 pg_catalog         | pg_attrdef              | table | postgres
 pg_catalog         | pg_attribute            | table | postgres
 pg_catalog         | pg_auth_members         | table | postgres
 pg_catalog         | pg_authid               | table | postgres
 pg_catalog         | pg_cast                 | table | postgres
 pg_catalog         | pg_class                | table | postgres
 pg_catalog         | pg_constraint           | table | postgres
 pg_catalog         | pg_conversion           | table | postgres
 pg_catalog         | pg_database             | table | postgres
 pg_catalog         | pg_depend               | table | postgres
 pg_catalog         | pg_description          | table | postgres
 pg_catalog         | pg_enum                 | table | postgres
 pg_catalog         | pg_foreign_data_wrapper | table | postgres
 pg_catalog         | pg_foreign_server       | table | postgres
 pg_catalog         | pg_index                | table | postgres
 pg_catalog         | pg_inherits             | table | postgres
 pg_catalog         | pg_language             | table | postgres
 pg_catalog         | pg_largeobject          | table | postgres
 pg_catalog         | pg_listener             | table | postgres
 pg_catalog         | pg_namespace            | table | postgres
 pg_catalog         | pg_opclass              | table | postgres
 pg_catalog         | pg_operator             | table | postgres
 pg_catalog         | pg_opfamily             | table | postgres
 pg_catalog         | pg_pltemplate           | table | postgres
 pg_catalog         | pg_proc                 | table | postgres
 pg_catalog         | pg_rewrite              | table | postgres
 pg_catalog         | pg_shdepend             | table | postgres
 pg_catalog         | pg_shdescription        | table | postgres
 pg_catalog         | pg_statistic            | table | postgres
 pg_catalog         | pg_tablespace           | table | postgres
 pg_catalog         | pg_trigger              | table | postgres
 pg_catalog         | pg_ts_config            | table | postgres
 pg_catalog         | pg_ts_config_map        | table | postgres
 pg_catalog         | pg_ts_dict              | table | postgres
 pg_catalog         | pg_ts_parser            | table | postgres
 pg_catalog         | pg_ts_template          | table | postgres
 pg_catalog         | pg_type                 | table | postgres
 pg_catalog         | pg_user_mapping         | table | postgres
'''


