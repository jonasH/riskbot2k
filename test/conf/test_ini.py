__author__ = 'jonas'

import unittest
import configobj
from validate import Validator
import os

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
        print(val)
        self.assertTrue(val)


if __name__ == '__main__':
    unittest.main()
