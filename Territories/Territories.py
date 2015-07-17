#coding: latin1

class Territory():
    def __init__(self, name, continent, start_soldiers):
        self.active_soldiers = start_soldiers
        self.continent = continent
        self.name = name
        self.owner = ""
        self.connections = []
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name
    def get_owner(self):
        return self.owner
    def get_connections(self):
        return self.connections
    def get_continent(self):
        return self.continent
    def add_connection(self, connection):
        self.connections.append(connection)
    def set_owner(self, owner):
        self.owner = owner

class Continent():
    def __init__(self, name):
        self.territories = []
        self.name = name
        self.connections = []
    def get_name(self):
        return self.name

    def get_territories(self):
        return self.territories

    def get_nbr_territories(self):
        return len(self.territories)

    def add_territory(self, t):
        self.territories.append(t)

    def add_connection(self,c):
        self.connections.append(c)

    def get_connections(self):
        return self.connections

class Board(object):
    def __init__(self):
        self.continents = []
        self.world = {}
    def get_continents(self):
        return self.continents

    def get_nbr_continents(self):
        return len(self.continents)

    def add_continent(self, c):
        self.continents.append(c)

    def add_world(self, w):
        self.world = w

    def get_world(self):
        return self.world