__author__ = 'Rickard'

import unittest
from Game_director.Rules import Rules

class TerritoryTestCase(unittest.TestCase):
    def setUp(self):
        self.ins = Rules()

    def test_negative(self):
        for i in range(-10, 12):
            exp = 0
            res = self.ins.get_territory_bonus(i)
            self.assertEquals(res, exp)

    def test_positive(self):
        res = self.ins.get_territory_bonus(12)
        self.assertEquals(res, 1)
        res = self.ins.get_territory_bonus(18)
        self.assertEquals(res, 3)
        res = self.ins.get_territory_bonus(26)
        self.assertEquals(res, 5)
        res = self.ins.get_territory_bonus(42)
        self.assertEquals(res, 10)
        res = self.ins.get_territory_bonus(36)
        self.assertEquals(res, 9)
        res = self.ins.get_territory_bonus(39)
        self.assertEquals(res, 9)
        res = self.ins.get_territory_bonus(40)
        self.assertEquals(res, 10)
        res = self.ins.get_territory_bonus(412)
        self.assertEquals(res, 10)

class TerritoryTestCase(unittest.TestCase):
    def setUp(self):
        self.ins = Rules()

    def test_negative(self):
        for i in range(-10, 2):
            res = self.ins.stars_for_units(i)
            self.assertEquals(0, res)

    def test_positives(self):
        res = self.ins.stars_for_units(3)
        self.assertEquals(4, res)
        res = self.ins.stars_for_units(4)
        self.assertEquals(7, res)
        res = self.ins.stars_for_units(5)
        self.assertEquals(10, res)
        res = self.ins.stars_for_units(6)
        self.assertEquals(13, res)
        res = self.ins.stars_for_units(7)
        self.assertEquals(17, res)
        res = self.ins.stars_for_units(8)
        self.assertEquals(21, res)
        res = self.ins.stars_for_units(9)
        self.assertEquals(25, res)
        res = self.ins.stars_for_units(10)
        self.assertEquals(30, res)

    def test_positives_2(self):
            res = self.ins.stars_for_units(2)
            self.assertEquals(2, res)

if __name__ == '__main__':
    unittest.main()
