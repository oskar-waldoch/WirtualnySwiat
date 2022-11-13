from swiat import *
import random
from grid import Grid


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

    def akcja(Organizm):

        if Organizm.pos_x == 19:
            move = random.choice([2, 3, 4])
        elif Organizm.pos_y == 19:
            move = random.choice([1, 2, 3])
        elif Organizm.pos_x == 0:
            move = random.choice([1, 2, 4])
        elif Organizm.pos_y == 0:
            move = random.choice([1, 3, 4])
        elif Organizm.pos_y == 0 and Organizm.pos_x:
            move = random.choice([1, 2])
        else: 
            move = random.randrange(1,4)

        match move:
            case 1:
                Organizm.pos_x += 1
            case 2:
                Organizm.pos_y -= 1
            case 3:
                Organizm.pos_x -= 1
            case 4:
                Organizm.pos_y += 1


