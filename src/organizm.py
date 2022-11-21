from swiat import *
import random
from grid import Grid
import zwierze



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

        if Organizm.pos_x == Grid.gridSize-1 and Organizm.pos_y == Grid.gridSize-1:
            move = random.choice([2, 3])
        elif Organizm.pos_y == 0 and Organizm.pos_x == 0:
            move = random.choice([1, 4])
        elif Organizm.pos_y == Grid.gridSize-1 and Organizm.pos_x == 0:
            move = random.choice([1, 2])
        elif Organizm.pos_y == 0 and Organizm.pos_x == Grid.gridSize-1:
            move = random.choice([3, 4])
        elif Organizm.pos_x == Grid.gridSize-1:
            move = random.choice([2, 3, 4])
        elif Organizm.pos_y == Grid.gridSize-1:
            move = random.choice([1, 2, 3])
        elif Organizm.pos_x == 0:
            move = random.choice([1, 2, 4])
        elif Organizm.pos_y == 0:
            move = random.choice([1, 3, 4])
        else: 
            move = random.choice([1, 2, 3, 4])

        match move:
            case 1:
                Organizm.pos_x += 1
            case 2:
                Organizm.pos_y -= 1
            case 3:
                Organizm.pos_x -= 1
            case 4:
                Organizm.pos_y += 1

    def kolizja(Organizm):

        rosliny = [" mlecz"," trawa", " wilczaJagoda"]
        for x in range(len(Swiat.organisms)):
            cos = 1
            for y in range(x+1, len(Swiat.organisms)):
                #print(len(Swiat.organisms))
                if Swiat.organisms[x].pos_x == Swiat.organisms[y].pos_x and Swiat.organisms[x].pos_y == Swiat.organisms[y].pos_y and Swiat.organisms[x].typ == Swiat.organisms[y].typ and Swiat.organisms[x].typ not in rosliny:
                    if Grid.gridList[Swiat.organisms[x].pos_x] != 0 and Grid.gridList[Swiat.organisms[y].pos_y] != 0:
                        cos = 2
                        match Swiat.organisms[x].typ:
                            case " owca":
                                zwierze.Owca(" owca", Swiat.organisms[x].pos_x + cos, Swiat.organisms[x].pos_y)
                            case " wilk":
                                zwierze.Wilk(" wilk", Swiat.organisms[x].pos_x + cos, Swiat.organisms[x].pos_y)
                            case " pies":
                                zwierze.Pies(" pies", Swiat.organisms[x].pos_x + cos, Swiat.organisms[x].pos_y)
                            case " zmija":
                                zwierze.Zmija(" zmija", Swiat.organisms[x].pos_x + cos, Swiat.organisms[x].pos_y)
                    else:
                        match Swiat.organisms[x].typ:
                            case " owca":
                                zwierze.Owca(" owca", Swiat.organisms[x].pos_x + cos, Swiat.organisms[x].pos_y)
                            case " wilk":
                                zwierze.Wilk(" wilk", Swiat.organisms[x].pos_x + cos, Swiat.organisms[x].pos_y)
                            case " pies":
                                zwierze.Pies(" pies", Swiat.organisms[x].pos_x + cos, Swiat.organisms[x].pos_y)
                            case " zmija":
                                zwierze.Zmija(" zmija", Swiat.organisms[x].pos_x + cos, Swiat.organisms[x].pos_y)
        for i in range(1, 10):
                        for x in range(len(Swiat.organisms)):
                            for y in range(x+1, len(Swiat.organisms)):
                                if Swiat.organisms[x].pos_x == Swiat.organisms[y].pos_x and Swiat.organisms[x].pos_y == Swiat.organisms[y].pos_y:
                                    #print(str(Swiat.organisms[x]) + " ta sama pozycja co " + str(Swiat.organisms[y]))
                                    if Swiat.organisms[x].typ == " zmija" or Swiat.organisms[y].typ == " zmija" or Swiat.organisms[y].typ == " wilczeJagody" or Swiat.organisms[y].typ == " wilczeJagody":
                                        if Swiat.organisms[x].sila != Swiat.organisms[y].sila:
                                            Swiat.organisms.remove(Swiat.organisms[x])
                                            Swiat.organisms.remove(Swiat.organisms[y])
                                            break
                                        else:
                                            pass
                                    else:
                                        if Swiat.organisms[x].sila == Swiat.organisms[y].sila:
                                            pass
                                        elif Swiat.organisms[x].sila > Swiat.organisms[y].sila:
                                            #eventLog.append((str(Swiat.organisms[x].typ) + " (" + str(Swiat.organisms[x].pos_x) + " )" + " zabija " + str(Swiat.organisms[y].typ)))
                                            Swiat.organisms.remove(Swiat.organisms[y])
                                            break
                                        else:
                                           # eventLog.append(str(Swiat.organisms[y].typ) + " zabija " + str(Swiat.organisms[x].typ))
                                            Swiat.organisms.remove(Swiat.organisms[x])
                                            break
    def rysowanie(Organizm):

        Grid.gridList[Organizm.pos_x][Organizm.pos_y] = Organizm.typ
