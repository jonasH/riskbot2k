#coding: latin1

territory_dict = {1:'Europe', 2:'Asia', 3:'Africa', 4:'North America', 5:'South America', 6:'Australia'}

#EUROPA
class Scandinavia():
    def __init__(self):
        self.starting_soldiers = 1
        self.active_soldiers = 1
        self.territory = territory_dict[1]
        self.name = "Scandinavia"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Northern_Europe():
    def __init__(self):
        self.starting_soldiers = 2
        self.active_soldiers = 2
        self.territory = territory_dict[1]
        self.name = "Northern Europe"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Southern_Europe():
    def __init__(self):
        self.starting_soldiers = 2
        self.active_soldiers = 2
        self.territory = territory_dict[1]
        self.name = "Southern Europe"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Iceland():
    def __init__(self):
        self.starting_soldiers = 1
        self.active_soldiers = 1
        self.territory = territory_dict[1]
        self.name = "Iceland"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Russia():
    def __init__(self):
        self.starting_soldiers = 2
        self.active_soldiers = 2
        self.territory = territory_dict[1]
        self.name = "Russia"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Great_Britain():
    def __init__(self):
        self.starting_soldiers = 1
        self.active_soldiers = 1
        self.territory = territory_dict[1]
        self.name = "Great Britain"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Western_Europe():
    def __init__(self):
        self.starting_soldiers = 1
        self.active_soldiers = 1
        self.territory = territory_dict[1]
        self.name = "Western Europe"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

#NORD AMERIKA
class Alaska():
    def __init__(self):
        self.starting_soldiers = 2
        self.active_soldiers = 2
        self.territory = territory_dict[4]
        self.name = "Alaska"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Western_Canada():
    def __init__(self):
        self.starting_soldiers = 1
        self.active_soldiers = 1
        self.territory = territory_dict[4]
        self.name = "Western Canada"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Central_America():
    def __init__(self):
        self.starting_soldiers = 2
        self.active_soldiers = 2
        self.territory = territory_dict[4]
        self.name = "Central America"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Eastern_united_states():
    def __init__(self):
        self.starting_soldiers = 2
        self.active_soldiers = 2
        self.territory = territory_dict[4]
        self.name = "Eastern United States"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Greenland():
    def __init__(self):
        self.starting_soldiers = 2
        self.active_soldiers = 2
        self.territory = territory_dict[4]
        self.name = "Greenland"
    def get_starting_soldiers(self):
        return self.starting_soldiers
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name

class Territory():
    def __init__(self, name, continent, start_soldiers, owner):
        self.active_soldiers = start_soldiers
        self.continent = continent
        self.name = name
        self.owner = owner
    def get_active_soldiers(self):
        return self.active_soldiers
    def get_name(self):
        return self.name
    def get_owner(self):
        return self.owner

class Continents():
    def __init__(self):
        self.territories = []