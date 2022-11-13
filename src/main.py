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
    return pygame.font.Font("assets/dDicapslock.ttf", size)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0) # Wilk
orchid = (177, 74, 237) # Owca
tea_green = (204, 232, 204) # Pies
tangerine = (255, 155, 133) # Leniwiec
patriarch = (115, 0, 113) # Zmija
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
gridList1 = grid1.gridList

# Initialize objects
world = Swiat()
wilk1 = Wilk(5, 5, randrange(20), randrange(20))
owca1 = Owca(10, 10, randrange(20), randrange(20))


#attributes = [organism.pos_x for organism in Swiat.organisms]

gridList1[wilk1.pos_x][wilk1.pos_y] = " wilk1"
gridList1[owca1.pos_x][owca1.pos_y] = " owca1"


def main():


    MAIN_TITLE_TEXT = get_font(35).render("Wirtualny Swiat", True, white)
    MAIN_TITLE_RECT = MAIN_TITLE_TEXT.get_rect(center=(600, 100))

    AUTHORS_TEXT= get_font(15).render("Oskar-Waldoch-29, Dawid-Kit-00", True, white)
    AUTHORS_RECT = AUTHORS_TEXT.get_rect(center=(1070, 780))


    WINDOW.blit(MAIN_TITLE_TEXT, MAIN_TITLE_RECT)
    WINDOW.blit(AUTHORS_TEXT, AUTHORS_RECT)

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in gridList1]))


    while True:

        dt = clock.tick(60)/1000.0
        grid1.updateGrid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == button_nextTurn:
                    
                    gridList1[wilk1.pos_x][wilk1.pos_y] = 0
                    gridList1[owca1.pos_x][owca1.pos_y] = 0

                    list(map(lambda organism: organism.akcja(), Swiat.organisms))

                    gridList1[wilk1.pos_x][wilk1.pos_y] = " wilk1"
                    gridList1[owca1.pos_x][owca1.pos_y] = " owca1"

                    grid1.updateGrid()

            manager.process_events(event)
        manager.update(dt)


        WINDOW.blit(simulation, simulation.get_rect(center = WINDOW.get_rect().center))
        manager.draw_ui(WINDOW)


        pygame.display.update()

if __name__ == '__main__':
    main()
