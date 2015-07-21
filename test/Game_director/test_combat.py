__author__ = 'rickard'
import unittest
from mock import patch
from controller.game_actions import war, battle, throw_die
from model.world import Territory

class CombatTestCase(unittest.TestCase):

    def test_die_high(self):
        res = throw_die(200)
        self.assertLessEqual(max(res),6)

    def test_die_low(self):
        res = throw_die(200)
        self.assertGreater(min(res),0)

    @patch('controller.game_actions.throw_die')
    def test_battle(self,mock_method):
        p1 = Territory('',None,2)
        p2 = Territory('',None,1)
        mock_method.side_effect = [[6],[6]]
        res = battle(p1,p2, 1)
        self.assertTrue(res)

    @patch('controller.game_actions.throw_die')
    def test_war_jonas_vinner(self,mock_method):
        p1 = Territory('',None,2)
        p2 = Territory('',None,1)
        mock_method.side_effect = [[6],[6]]
        res = war(p1,p2, 1)
        self.assertEqual(res, p2)

    @patch('controller.game_actions.throw_die')
    def test_war_rickard_vinner(self,mock_method):
        p1 = Territory('',None,2)
        p2 = Territory('',None,1)
        mock_method.side_effect = [[6],[5]]
        res = war(p1,p2, 1)
        self.assertEqual(res, p1)

    @patch('controller.game_actions.throw_die')
    def test_war_flera_dies_jonas_win(self,mock_method):
        p1 = Territory('',None,2)
        p2 = Territory('',None,2)
        mock_method.side_effect = [[6],[5,6]]
        res = war(p1,p2, 1)
        self.assertEqual(res, p2)

    @patch('controller.game_actions.throw_die')
    def test_war_flera_dies_rickard_win(self,mock_method):
        p1 = Territory('',None,2)
        p2 = Territory('',None,1)
        mock_method.side_effect = [[5,6],[5]]
        res = war(p1,p2, 1)
        self.assertEqual(res, p1)

if __name__ == '__main__':
    unittest.main()