from organizm import Organizm
import random


class Roslina(Organizm):
    sila = Organizm.sila

    


class Trawa(Roslina):
    sila = 0

    def akcja(Organizm):
        move = random.randrange(1, 50)
        moveWhere = random.choice([1, 2, 3, 4])
        if move == 1:
            match moveWhere:
                case 1:
                    trawa = Trawa(" trawa", (Organizm.pos_x) + 1, Organizm.pos_y)
                case 2:
                    trawa = Trawa(" trawa", Organizm.pos_x, (Organizm.pos_y) - 1)
                case 3:
                    trawa = Trawa(" trawa", (Organizm.pos_x) - 1, Organizm.pos_y)
                case 4:
                    trawa = Trawa(" trawa", Organizm.pos_x, (Organizm.pos_y) + 1)


class Mlecz(Roslina):
    sila = 0

    def akcja(Organizm):
        for x in range(1, 3):
            move = random.randrange(1, 50)
            moveWhere = random.choice([1, 2, 3, 4])
            
            if move == 1:
                match moveWhere:
                    case 1:
                        mlecz = Mlecz(" mlecz", (Organizm.pos_x) + 1, Organizm.pos_y)
                    case 2:
                        mlecz = Mlecz(" mlecz", Organizm.pos_x, (Organizm.pos_y) - 1)
                    case 3:
                        mlecz = Mlecz(" mlecz", (Organizm.pos_x) - 1, Organizm.pos_y)
                    case 4:
                        mlecz = Mlecz(" mlecz", Organizm.pos_x, (Organizm.pos_y) + 1)


class WilczaJagoda(Roslina):
    sila = 0

    def akcja(Organizm):
        move = random.randrange(1, 50)
        moveWhere = random.choice([1, 2, 3, 4])
        if move == 1:
            match moveWhere:
                case 1:
                    wilczaJagoda = WilczaJagoda(" wilczaJagoda", (Organizm.pos_x) + 1, Organizm.pos_y)
                case 2:
                    wilczaJagoda = WilczaJagoda(" wilczaJagoda", Organizm.pos_x, (Organizm.pos_y) - 1)
                case 3:
                    wilczaJagoda = WilczaJagoda(" wilczaJagoda", (Organizm.pos_x) - 1, Organizm.pos_y)
                case 4:
                    wilczaJagoda = WilczaJagoda(" wilczaJagoda", Organizm.pos_x, (Organizm.pos_y) + 1)
