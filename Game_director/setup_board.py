__author__ = 'riqv'
from test.conf import test_connections
from Territories.Territories import Territory, Board, Continent
import configobj
from blobapp import BlobApp
board = Board()
world_conf = configobj.ConfigObj('..\\conf\\earth_world.ini', configspec='..\\conf\\board_spec.ini')

world_dict = {}



for continent in world_conf.keys():
    c = Continent(continent)
    board.add_continent(c)

    for territory in world_conf[continent]:
        ss = world_conf[continent][territory]['start_soldiers']
        t = Territory(territory, continent, ss)
        c.add_territory(t)
        world_dict[territory] = t

for continent in world_conf.keys():
    for territory in world_conf[continent]:
        for c in world_conf[continent][territory]['connections']:
            world_dict[territory].add_connection(world_dict[c])

continent_connections = {}
for continent in board.get_continents():
    connections_list = []
    connections_set = set()
    connections_dict = {}
    territory_list = []
    for territory in continent.get_territories():
        territory_list.append(territory)
        for connections in territory.get_connections():
            connections_list.append(connections.get_continent())
            connections_set.add(connections.get_continent())
        connections_set.remove(continent.get_name())
        for ranker in [x for x in connections_set]:
            connections_dict[ranker] = connections_list.count(ranker)
    continent_connections[continent.get_name()] = {'connecting_continents':connections_dict,
                                                   'territories':territory_list}



# sorted_ranks = sort_rankings(continent_connections['asia']['connecting_continents'])
# for x in range(0,len(sorted_ranks)):
#     print sorted_ranks[x]

board.add_world(continent_connections)
b = BlobApp(board)
b.run()