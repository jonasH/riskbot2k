__author__ = 'jonas'

import unittest
import configobj
from validate import Validator
import os
import test_connections

#[[iceland]]
#start_soldiers = 1
#[[[connections]]]
#greenland
#scandinavia

class IniTestCase(unittest.TestCase):
    def test_earthworld(self):
        validator = Validator()
        if os.path.exists('../../conf/earth_world.ini'):
            conf = configobj.ConfigObj('../../conf/earth_world.ini',
                                       configspec='../../conf/board_spec.ini')
        val = conf.validate(validator)
        self.assertTrue(val)

    def test_geography(self):
        config = { 'continent1':{
                        'country1':{'connections':['country2','country3']},
                        'country2':{'connections':['country1','country3']},
                        'country3':{'connections':['country1','country2']},
                        'country4':{'connections':['country5','country2']}
                            },
        }

        self.assertTrue(test_connections.test_connections(config))
if __name__ == '__main__':
    unittest.main()
