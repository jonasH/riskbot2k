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


b = BlobApp(board)
b.run()