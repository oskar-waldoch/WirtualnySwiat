from swiat import *


class Organizm(Swiat):
    sila = 0
    inicjatywa = 0
    pos_x = 0
    pos_y = 0

    def __init__(self, sila, inicjatywa, pos_x, pos_y):
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.pos_x = pos_x
        self.pos_y = pos_y
        Swiat.organisms.append(self)

    


