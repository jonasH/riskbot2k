#coding: latin1
import numpy

class Rules():
    def get_territory_bonus(self, numb_territories):
        from math import floor
        result = floor(numb_territories/3-3)
        result = max(0,result)
        result = min(10, result)
        if numb_territories == 39:
            return 9
        return result

    def stars_for_units(self, stars):
        from math import floor
        return floor(numpy.interp(stars, [2, 6, 10], [2,13,30]))