from organizm import Organizm
import random


class Zwierze(Organizm):
    sila = Organizm.sila
    inicjatywa = Organizm.inicjatywa

    def akcja( Organizm):

        #move = random.randrange(1,4)

        if Organizm.pos_x == 19:
            #move = random.randrange(2,4)
            move = random.choice([2, 3, 4])
        elif Organizm.pos_y == 19:
            #move = random.randrange(1,3)
            move = random.choice([1, 2, 3])
        elif Organizm.pos_x == 0:
            move = random.choice([1, 2, 4])
        elif Organizm.pos_y == 0:
            move = random.choice([1, 3, 4])
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
        




class Wilk(Zwierze):
    Zwierze.sila = 9
    Zwierze.inicjatywa = 5
    


class Owca(Zwierze):
    Zwierze.sila = 4
    Zwierze.inicjatywa = 4


class Pies(Zwierze):
    Zwierze.sila = 6
    Zwierze.inicjatywa = 4


class Leniwiec(Zwierze):
    Zwierze.sila = 2
    Zwierze.inicjatywa = 1


class Zmija(Zwierze):
    Zwierze.sila = 2
    Zwierze.inicjatywa = 3
