#-*- coding: utf-8 -*-

import os
import sys
import codecs
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pharao.models import (DBSession, Base)

from pharao.models.authentication import *
from pharao.models.log import *

def populatePaises(database=DBSession):
    with codecs.open(os.path.dirname(__file__)+'/lista-paises.txt', 'r', encoding='utf-8') as paises:
        for row in paises:
            data = row.replace('\n', '').split(', ')
            pais = Pais(iso=data[0],iso3=data[1],id=data[2],nome=data[3])
            database.add(pais)
            database.flush()

def populateEstadosBR(database=DBSession):
    pais = database.query(Pais).filter(Pais.nome==u'Brasil').first()
    with codecs.open( os.path.dirname(__file__)+'/estados-brasil.txt', 'r', encoding='utf-8') as estados:
        for row in estados:
            data = row.replace('\n', '').split(', ')
            est = Estado(id=data[0],iso=data[1],nome=data[2], pais_id=pais.id)
            database.add(est)
            database.flush()

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv, database=DBSession):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    if config_uri != 'testing':
        setup_logging(config_uri)
        settings = get_appsettings(config_uri)
        engine = engine_from_config(settings, 'sqlalchemy.')
        database.configure(bind=engine)
        #database.execute('CREATE EXTENSION hstore;')
        Base.metadata.create_all(engine)

    with transaction.manager:
        populatePaises(database)
        populateEstadosBR(database)

        statuses = [u'Não possui', u'Não sabe informar', u'Recusa']
        for p in statuses:
            database.add(IntegranteStatus(nome=p))
        database.flush()

        statuses = [u'Sim', u'Só ler', u'Não']
        for p in statuses:
            database.add(SabeLer(nome=p))
        database.flush()


