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
        attacker['dies'] = self.throw_die(attacker['soldiers'])
        if defender['soldiers'] >3:
            defender['dies'] = self.throw_die(defender['soldiers'])
        else:
            defender['dies'] = self.throw_die(2)
        nbr_throws = defender['soldiers']
        for x in range(0, nbr_throws):
            if attacker['soldiers'] == 0 or len(attacker['dies']) == 0:
                return winner
            combat_results = self.combat(max(attacker['dies']), max(defender['dies']))
            if combat_results == max(attacker['dies']) and combat_results != max(defender['dies']):
                defender['soldiers'] -= 1
                attacker['dies'].pop(attacker['dies'].index(combat_results))
                defender['dies'].pop(defender['dies'].index(max(defender['dies'])))
                winner = attacker
            else:
                attacker['soldiers'] -= 1
                attacker['dies'].pop(attacker['dies'].index(max(attacker['dies'])))
                defender['dies'].pop(defender['dies'].index(combat_results))
                winner = defender
        return winner