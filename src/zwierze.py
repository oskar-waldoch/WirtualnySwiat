from organizm import Organizm
import random


class Zwierze(Organizm):
    sila = Organizm.sila
    inicjatywa = Organizm.inicjatywa

    
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
