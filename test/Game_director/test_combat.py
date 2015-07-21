__author__ = 'rickard'
import unittest
from mock import patch
from Game_director.Game_Director import Combat

class CombatTestCase(unittest.TestCase):
    def setUp(self):
        self.p1 = {'name':'rickard','soldiers':1}
        self.p2 = {'name':'jonas','soldiers':1}
        self.ins = Combat()

    def test_die_high(self):
        res = self.ins.throw_die(200)
        self.assertLessEqual(max(res),6)

    def test_die_high(self):
        res = self.ins.throw_die(200)
        self.assertGreater(min(res),0)

    def test_war(self):
        with patch.object(Combat, 'throw_die') as mock_method:
            mock_method.return_value = 6
            res = self.ins.war(self.p1,self.p2)
            self.assertEqual(res['name'],'jonas')
if __name__ == '__main__':
    unittest.main()