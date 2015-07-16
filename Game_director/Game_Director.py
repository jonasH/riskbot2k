#coding: latin1
from Territories import Territories
from .Rules import Rules
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

    def move_soldiers(self, from_territory, to_territory, nbr_of_soldiers):
        if from_territory.get_name() in territories_names and to_territory.get_name() in territories_names:
            if from_territory.get_active_soldiers() - nbr_of_soldiers >= 1:
                from_territory.active_soldiers -= nbr_of_soldiers
                to_territory.active_soldiers += nbr_of_soldiers
            else:
                print("Du måste ha minst en soldat i varje territorie")
        else:
            print("Nu är det fajt!")



player1 = Game_Director([Territories.Scandinavia(), Territories.Russia(), Territories.Iceland(), Territories.Southern_Europe()])

print((player1.get_starting_soldiers()))
player1.turn += 1
player1.set_soldiers_new_round()
for territory in player1.territories:
    print((territory.get_name() + ": %d" %territory.get_active_soldiers()))
print("Flyttar trupper från ")
player1.move_soldiers(Territories.Scandinavia(), Territories.Russia(), 2)
for territory in player1.territories:
    print((territory.get_name() + ": %d" %territory.get_active_soldiers()))
