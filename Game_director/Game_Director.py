# coding: latin1
from Territories import Territories
from .Rules import Rules
from random import randint


class Game_Director():
    def __init__(self, territories):
        self.territories = territories
        self.turn = 0
        self.nbr_soldiers = 0
        self.rules = Rules()

    def get_starting_soldiers(self):
        for t in self.territories:
            self.nbr_soldiers += t.get_starting_soldiers()
        return self.nbr_soldiers

    def get_nbr_territories(self):
        return len(self.territories)

    def set_soldiers_new_round(self):
        if self.turn == 0:
            return self.get_starting_soldiers()
        else:
            self.nbr_soldiers = self.nbr_soldiers + 3 + self.rules.get_territory_bonus()[self.get_nbr_territories()]


class Combat():
    def throw_die(self, throws):
        throw_list = []
        for throw in range(0, throws):
            throw_list.append(randint(1, 6))
        return throw_list

    def combat(self, attacker, defender):
        if attacker > defender:
            return attacker
        else:
            return defender

    def war(self,attacker, defender):
        attacker['throw_results'] = self.throw_die(attacker['soldiers'])
        defender['throw_results'] = self.throw_die(defender['soldiers'])
        nbr_throws = min([attacker['soldiers'], defender['soldiers']])
        for x in range(0, nbr_throws):
            combat_results = self.combat(max(attacker['throw_results']), max(defender['throw_results']))
            if combat_results == max(attacker['throw_results']):
                defender['soldiers'] -= 1
                attacker['throw_results'].pop(attacker['throw_results'].index(combat_results))
                defender['throw_results'].pop(defender['throw_results'].index(max(defender['throw_results'])))
                return attacker
            else:
                attacker['soldiers'] -= 1
                defender['throw_results'].pop(defender['throw_results'].index(combat_results))
                attacker['throw_results'].pop(attacker['throw_results'].index(max(attacker['throw_results'])))
            return defender
