"""""
W

"""
import sys
import pygame
from zwierze import *
from random import *
from grid import Grid
import pygame_gui

#gridSize = int(input("Podaj "))
gridSize = 20

pygame.init()

# Window
WIDTH1, HEIGHT1 = 1200, 800
WIN = pygame.display.set_mode((WIDTH1, HEIGHT1))

# Title
pygame.display.set_caption("Wirtualny Swiat")

# Font
def get_font(size):
    return pygame.font.Font("assets/dDicapslock.ttf", size)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
colors = [white, black, red]

# Clock
clock = pygame.time.Clock()

# MainGame window
game = pygame.Surface((450, 450))
WIN.blit(game, game.get_rect(center=WIN.get_rect().center))

# UI
button_layout_rect = pygame.Rect(0, 0, 120, 50)
button_layout_rect.bottomright = (-277, -125)

manager = pygame_gui.UIManager((WIDTH1, HEIGHT1))
button_nextTurn = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text='Next turn',
                                             manager=manager,
                                             anchors={'right': 'right',
                                                      'bottom': 'bottom'})


# Grid size
GRID_MARGIN = 1
GRID_WIDTH = (game.get_width() - (gridSize * GRID_MARGIN)) / gridSize
GRID_HEIGHT = (game.get_height() - (gridSize * GRID_MARGIN)) / gridSize


# Grid instance
grid1 = Grid(game, gridSize, GRID_MARGIN, GRID_WIDTH, GRID_HEIGHT, colors)
grid1.createGrid()
gridList1 = grid1.gridList


wilk1 = Wilk(5, 5, randrange(20), randrange(20))

gridList1[wilk1.pos_x][wilk1.pos_y] = " wilk1"

def main():

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in gridList1]))

    MAIN_TITLE_TEXT = get_font(35).render("Wirtualny Swiat", True, white)
    MAIN_TITLE_RECT = MAIN_TITLE_TEXT.get_rect(center=(600, 100))

    WIN.blit(MAIN_TITLE_TEXT, MAIN_TITLE_RECT)

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
                    wilk1.akcja()
                    gridList1[wilk1.pos_x][wilk1.pos_y] = " wilk1"
                    grid1.updateGrid()
                    print(wilk1.pos_x, wilk1.pos_y)

            manager.process_events(event)
        manager.update(dt)


        WIN.blit(game, game.get_rect(center = WIN.get_rect().center))
        manager.draw_ui(WIN)


        pygame.display.update()

if __name__ == '__main__':
    main()
