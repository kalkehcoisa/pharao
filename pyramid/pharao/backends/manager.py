#-*- coding: utf-8 -*-

from .postgresql import Postgresql

from collections import OrderedDict


class ServerList():

    servers = OrderedDict()

    def __init__(self, servers):
        self.servers['Postgresql'] = OrderedDict()
        self.servers['Mysql'] = OrderedDict()

        for p in servers.split('\n'):
            server = p.split('://')[0].lower()
            if server in ['postgresql', 'mysql']:
                self.__add_server(server)

    def __add_server(self, server):
        sgdb = Postgresql(server)
        index = '%s:%s'%(sgdb.db_host,sgdb.db_port)
        self.servers[server.capitalize()][index] = sgdb

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if len(self.servers) >= self.index:
            raise StopIteration
        self.index += 1
        return self.servers[self.index]

    def __getitem__(self, item):
        return self.servers[item]

    def items(self):
        return self.servers.items()
    
    def keys(self):
        return self.servers.keys()
    
    def values(self):
        return self.servers.values()


    def sgdbs(self, name=None):
        if name:
            return self.servers[name].keys()
        else:
            ret = []
            for srv in self.servers.keys():
                ret.extend(srv.keys())
            return ret
