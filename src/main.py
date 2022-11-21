"""""
W

"""
import sys, os, json, pygame, pygame_gui
from zwierze import *
from roslina import *
from random import *
from swiat import Swiat
from grid import Grid

gridSize = int(input("Podaj "))
#gridSize = 20

pygame.init()

# Window
WIDTH, HEIGHT = 1200, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Title
pygame.display.set_caption("Wirtualny Swiat")

# Font
def get_font(size):
    return pygame.font.Font("dDicapslock.ttf", size)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 190, 11)
green = (67, 170, 139)
orange = (251, 86, 7)
blue = (58, 134, 255)
pink = (194, 0, 251)
macaroni = (252, 176, 126)
purple = (60, 9, 108)
colors = [white, black, red, yellow, green, orange, blue, pink, macaroni, purple]

# Clock
clock = pygame.time.Clock()

# Simulation window
simulation = pygame.Surface((450, 450))
WINDOW.blit(simulation, simulation.get_rect(center=WINDOW.get_rect().center))

# UI
button_layout_rect = pygame.Rect(0, 0, 120, 50)
button_layout_rect.bottomright = (-277, -125)

manager = pygame_gui.UIManager((WIDTH, HEIGHT))
button_nextTurn = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text='Next turn',
                                             manager=manager,
                                             anchors={'right': 'right',
                                                      'bottom': 'bottom'})


# Grid size
GRID_MARGIN = 1
GRID_WIDTH = (simulation.get_width() - (gridSize * GRID_MARGIN)) / gridSize
GRID_HEIGHT = (simulation.get_height() - (gridSize * GRID_MARGIN)) / gridSize

# Grid instance
grid1 = Grid(simulation, gridSize, GRID_MARGIN, GRID_WIDTH, GRID_HEIGHT, colors)
grid1.createGrid()

# Initialize objects
world = Swiat()
wilk1 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))
owca1 = Owca(" owca", randrange(gridSize), randrange(gridSize))
pies1 = Pies(" pies", randrange(gridSize), randrange(gridSize))
leniwiec1 = Leniwiec(" leniwiec", randrange(gridSize), randrange(gridSize))
zmija1 = Zmija(" zmija", randrange(gridSize), randrange(gridSize))
pies2 = Pies(" pies", randrange(gridSize), randrange(gridSize))
owca2 = Owca(" owca", randrange(gridSize), randrange(gridSize))

trawa1 = Trawa(" trawa", randrange(gridSize), randrange(gridSize))
mlecz1 = Mlecz(" mlecz", randrange(gridSize), randrange(gridSize))
wilczaJagoda1 = WilczaJagoda(" wilczaJagoda", randrange(gridSize), randrange(gridSize))

wilk1 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))
wilk2 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))
wilk3 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))
wilk4 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))
wilk5 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))
wilk6 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))
wilk8 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))
wilk9 = Wilk(" wilk", randrange(gridSize), randrange(gridSize))

rosliny = [" mlecz"," trawa", " wilczaJagoda"]
'''
if os.path.isfile('data/data.json'):
		with open('data/data.json', 'r') as f:
			openJSON = json.load(f)
			openedFile = openJSON
			grid = openedFile['grid']
'''



def main():

    main_title_text = get_font(35).render("Wirtualny Swiat", True, white)
    main_title_rect = main_title_text.get_rect(center=(600, 100))

    authors_text= get_font(15).render("Oskar-Waldoch-29, Dawid-Kit-11", True, white)
    authors_rect = authors_text.get_rect(center=(1070, 780))

    animals_wilk_text = get_font(17).render("Wilk - czerwony", True, red)
    animals_wilk_rect = animals_wilk_text.get_rect(center=(1070, 250))

    animals_owca_text = get_font(17).render("Owca - zolty", True, yellow)
    animals_owca_rect = animals_owca_text.get_rect(center=(1070, 275))

    animals_pies_text = get_font(17).render("Pies - zielony", True, green)
    animals_pies_rect = animals_pies_text.get_rect(center=(1070, 300))

    animals_leniwiec_text = get_font(17).render("Leniwiec - pomaranczowy", True, orange)
    animals_leniwiec_rect = animals_leniwiec_text.get_rect(center=(1070, 325))

    animals_zmija_text = get_font(17).render("Zmija - niebieski", True, blue)
    animals_zmija_rect = animals_zmija_text.get_rect(center=(1070, 350))

    animals_trawa_text = get_font(17).render("Trawa - rozowy", True, pink)
    animals_trawa_rect = animals_trawa_text.get_rect(center=(1070, 375))

    animals_mlecz_text = get_font(17).render("Mlecz - macaroni", True, macaroni)
    animals_mlecz_rect = animals_mlecz_text.get_rect(center=(1070, 400))

    animals_jagoda_text = get_font(17).render("Wilcza jagoda - fioletowy", True, purple)
    animals_jagoda_rect = animals_jagoda_text.get_rect(center=(1070, 425))



    WINDOW.blit(main_title_text, main_title_rect)
    WINDOW.blit(authors_text, authors_rect)
    WINDOW.blit( animals_wilk_text, animals_wilk_rect)
    WINDOW.blit(animals_owca_text, animals_owca_rect)
    WINDOW.blit(animals_pies_text, animals_pies_rect)
    WINDOW.blit(animals_leniwiec_text, animals_leniwiec_rect)
    WINDOW.blit(animals_zmija_text, animals_zmija_rect)
    WINDOW.blit(animals_trawa_text, animals_trawa_rect)
    WINDOW.blit(animals_mlecz_text, animals_mlecz_rect)
    WINDOW.blit(animals_jagoda_text, animals_jagoda_rect)


    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in grid1.gridList]))

    #print(Swiat.organisms)

    def killList(eventLog):
            row_y = 70
            for item in eventLog:
                text2 = get_font(15).render(item, True, white)
                WINDOW.blit(text2, (25, 200 + row_y))
                row_y += 20
    eventLog = []

    while True:

        dt = clock.tick(60)/1000.0

        # Save grid
        json_data = {'grid' : grid1.gridList}
        with open('data.json', 'w') as f:
            json.dump(json_data, f)

        #print(len(Swiat.organisms))

    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == button_nextTurn:
                    
                    grid1.clearGrid()
                    killList(eventLog)
                    print(eventLog)
                
                    list(map(lambda organism: organism.akcja(), Swiat.organisms))
                    '''
                    for i in range(1, 10):
                        for x in range(len(Swiat.organisms)):
                            for y in range(x+1, len(Swiat.organisms)):
                                if Swiat.organisms[x].pos_x == Swiat.organisms[y].pos_x and Swiat.organisms[x].pos_y == Swiat.organisms[y].pos_y and Swiat.organisms[x].typ == Swiat.organisms[y].typ and Swiat.organisms[x].typ not in rosliny:
                                    match Swiat.organisms[x].typ:
                                        case " owca":
                                            owca = Owca(" owca", Swiat.organisms[x].pos_x + 1, Swiat.organisms[x].pos_y)
                                        case " wilk":
                                            wilk = Wilk(" wilk", Swiat.organisms[x].pos_x + 1, Swiat.organisms[x].pos_y)
                                        case " pies":
                                            pies = Pies(" pies", Swiat.organisms[x].pos_x + 1, Swiat.organisms[x].pos_y)
                                        case " zmija":
                                            zmija = Zmija(" zmija", Swiat.organisms[x].pos_x + 1, Swiat.organisms[x].pos_y)
                                    eventLog.append("rozmnozono")
                                elif Swiat.organisms[x].pos_x == Swiat.organisms[y].pos_x and Swiat.organisms[x].pos_y == Swiat.organisms[y].pos_y:
                                    print(str(Swiat.organisms[x]) + " ta sama pozycja co " + str(Swiat.organisms[y]))
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
                                            eventLog.append((str(Swiat.organisms[x].typ) + " (" + str(Swiat.organisms[x].pos_x) + " )" + " zabija " + str(Swiat.organisms[y].typ)))
                                            Swiat.organisms.remove(Swiat.organisms[y])
                                            break
                                        else:
                                            eventLog.append(str(Swiat.organisms[y].typ) + " zabija " + str(Swiat.organisms[x].typ))
                                            Swiat.organisms.remove(Swiat.organisms[x])
                                            break
                    '''

                    list(map(lambda organism: organism.kolizja(), Swiat.organisms))
                    
                    killList(eventLog)
    
                    #list(map(lambda organism: print( str(organism.typ) + " " + str(organism.pos_x) + " " +str(organism.pos_y)), Swiat.organisms))

                    list(map(lambda organism: organism.rysowanie(), Swiat.organisms))



                    grid1.updateGrid()
            
            manager.process_events(event)
        manager.update(dt)


        WINDOW.blit(simulation, simulation.get_rect(center = WINDOW.get_rect().center))
        manager.draw_ui(WINDOW)

        pygame.display.update()

if __name__ == '__main__':
    main()
