from swiat import *
import random
from grid import Grid


class Organizm(Swiat):
    sila = 0
    inicjatywa = 0
    pos_x = 0
    pos_y = 0
    typ = ""

    def __init__(self, typ, pos_x, pos_y):
        self.typ = typ
        self.pos_x = pos_x
        self.pos_y = pos_y
        Swiat.organisms.append(self)

    def akcja(Organizm):

        if Organizm.pos_x == 19:
            move = random.choice([2, 3, 4])
        elif Organizm.pos_y == 0 and Organizm.pos_x == 0:
            move = random.choice([1, 2])
        elif Organizm.pos_y == 19:
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



    def kolizja(self, other):


        if self == other:
            pass
            if self.pos_x == other.pos_x and self.pos_y == other.pos_y:
                print(str(self.typ) + " ta sama pozycja jak " + str(other.typ))
                if self.sila > other.sila:
                    print(str(self.typ), "jest lepszy od", str(other.typ))
                    print(str(self.pos_x), str(self.pos_y))
                    Grid.gridList[self.pos_x][self.pos_y] = self.typ
                    print("Usunięto słabszego - 1")
                elif self.sila < other.sila:
                    print(str(self.typ), "jest słabszy od", str(other.typ))
                    Grid.gridList[other.pos_x][other.pos_y] = other.typ
            else:
                Grid.gridList[self.pos_x][self.pos_y] = self.typ
                Grid.gridList[other.pos_x][other.pos_y] = other.typ
        else:
            print("brak kolizji")

        '''
        if len(Swiat.organisms) > 1:
            if self.pos_x == other.pos_x and self.pos_y == other.pos_y:
                if self.sila > other.sila:
                    Grid.gridList[self.pos_x][self.pos_y] = self.typ
                    print("Usunięto słabszego - 1")
                    Swiat.organisms.remove(other)
                else :
                        Swiat.organisms.remove(self)
                        Grid.gridList[other.pos_x][other.pos_y] = other.typ
                        print(other.typ)
                        print("usunięto słabszego - 2")
            else:
                Grid.gridList[self.pos_x][self.pos_y] = self.typ
                Grid.gridList[other.pos_x][other.pos_y] = other.typ
                print("usunięto nikogo - 3")
        else:
            Grid.gridList[self.pos_x][self.pos_y] = self.typ
        '''


    def rysowanie(Organizm):

        Grid.gridList[Organizm.pos_x][Organizm.pos_y] = Organizm.typ