from organizm import Organizm
import random


class Zwierze(Organizm):
    sila = Organizm.sila
    inicjatywa = Organizm.inicjatywa

    
class Wilk(Zwierze):
    sila = 9
    inicjatywa = 5


class Owca(Zwierze):
    sila = 4
    inicjatywa = 4


class Pies(Zwierze):
    sila = 6
    inicjatywa = 4


class Leniwiec(Zwierze):
    sila = 2
    inicjatywa = 1


class Zmija(Zwierze):
    sila = 2
    inicjatywa = 3
