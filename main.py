import sys
import pygame
from zwierze import *
from random import *
gridSize = int(input("Podaj "))

pygame.init()

# Window
WIDTH1, HEIGHT1 = 900, 700
WIN = pygame.display.set_mode((WIDTH1, HEIGHT1))

# Title
pygame.display.set_caption("Wirtualny Swiat")

# Clock
clock = pygame.time.Clock()


center = WIN.get_rect().center


# MainGame window
game = pygame.Surface((420, 420))
WIN.blit(game, game.get_rect(center=WIN.get_rect().center))

# Grid size
GRID_MARGIN = 1
GRID_WIDTH = (game.get_width() - (gridSize * GRID_MARGIN)) / gridSize
GRID_HEIGHT = (game.get_height() - (gridSize * GRID_MARGIN)) / gridSize

# Create a 2 dimensional array
grid = []

for row in range(gridSize):
    grid.append([])
    for column in range(gridSize):
        grid[row].append(0)

swiat = Swiat()

wilk1 = Wilk()
wilk1.x = randrange(gridSize)
wilk1.y = randrange(gridSize)

grid[wilk1.x][wilk1.y] = wilk1


def main():


    while True:
        dt = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

         # Draw the grid
        for row in range(gridSize):
            for column in range(gridSize):
                color = (255,255,255)
                if grid[row][column] == 1:
                    color = (255, 255, 255)
                pygame.draw.rect(game,color,[(GRID_MARGIN + GRID_WIDTH) * column + GRID_MARGIN,(GRID_MARGIN + GRID_HEIGHT) * row + GRID_MARGIN,GRID_WIDTH,GRID_HEIGHT])
        WIN.blit(game, game.get_rect(center = WIN.get_rect().center))


        pygame.display.update()

if __name__ == '__main__':
    main()
