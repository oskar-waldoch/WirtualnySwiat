import sys
import pygame
import zwierze
import random
from grid import Grid

gridSize = int(input("Podaj "))

pygame.init()

# Window
WIDTH1, HEIGHT1 = 900, 700
WIN = pygame.display.set_mode((WIDTH1, HEIGHT1))

# Title
pygame.display.set_caption("Wirtualny Swiat")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# MainGame window
game = pygame.Surface((420, 420))
WIN.blit(game, game.get_rect(center=WIN.get_rect().center))

# Grid size
GRID_MARGIN = 1
GRID_WIDTH = (game.get_width() - (gridSize * GRID_MARGIN)) / gridSize
GRID_HEIGHT = (game.get_height() - (gridSize * GRID_MARGIN)) / gridSize


####grid[wilk1.x][wilk1.y] = wilk1

grid1 = Grid(gridSize)


def main():

    grid1.createGrid(game, gridSize, GRID_MARGIN, GRID_WIDTH, GRID_HEIGHT, white)

    while True:
        dt = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        WIN.blit(game, game.get_rect(center = WIN.get_rect().center))


        pygame.display.update()

if __name__ == '__main__':
    main()
