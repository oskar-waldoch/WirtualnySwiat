"""""
W

"""
import sys
import pygame
from zwierze import *
from random import *
from swiat import Swiat
from grid import Grid
import pygame_gui

#gridSize = int(input("Podaj "))
gridSize = 20

pygame.init()

# Window
WIDTH, HEIGHT = 1200, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Title
pygame.display.set_caption("Wirtualny Swiat")

# Font
def get_font(size):
    return pygame.font.Font("./assets/dDicapslock.ttf", size)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orchid = (177, 74, 237)
tea_green = (204, 232, 204)
tangerine = (255, 155, 133)
patriarch = (115, 0, 113)
colors = [white, black, red, orchid, tea_green, tangerine, patriarch]

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
#wilk1 = Wilk(5, 5, randrange(20), randrange(20))
#owca1 = Owca(10, 10, randrange(20), randrange(20))

wilk1 = Wilk(" wilk", 10, 5, 5, 5)
owca1 = Owca(" owca", 5, 10, 5, 5)
#owca2 = Owca(" owca", 15, 10, 15, 15)


def main():

    main_title_text = get_font(35).render("Wirtualny Swiat", True, white)
    main_title_rect = main_title_text.get_rect(center=(600, 100))

    authors_text= get_font(15).render("Oskar-Waldoch-29, Dawid-Kit-11", True, white)
    authors_rect = authors_text.get_rect(center=(1070, 780))

    WINDOW.blit(main_title_text, main_title_rect)
    WINDOW.blit(authors_text, authors_rect)

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in grid1.gridList]))

    print(Swiat.organisms)

    while True:

        dt = clock.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == button_nextTurn:
                    
                    wilk1.pos_x = 5
                    wilk1.pos_y = 5

                    owca1.pos_x = 5
                    owca1.pos_y = 5

                    # The problems is here below. This shits breaks everything. If we were to call the kolizja() function
                    # of every animal instance manualy, it works fantastically.
                    list(map(lambda organism: organism.kolizja(organism), Swiat.organisms))
                    
                    #list(map(lambda organism: organism.akcja(), Swiat.organisms))

                    grid1.updateGrid()

                    print(Swiat.organisms)

            manager.process_events(event)
        manager.update(dt)


        WINDOW.blit(simulation, simulation.get_rect(center = WINDOW.get_rect().center))
        manager.draw_ui(WINDOW)


        pygame.display.update()

if __name__ == '__main__':
    main()
