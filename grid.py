import pygame 
class Grid:

    def __init__(self, size):
        self.size = size

    def createGrid(self, screen, gridSize, gridMargin, gridWidth, gridHeight, color):
        grid = []

        for row in range(gridSize):
            grid.append([])
            for column in range(gridSize):
                grid[row].append(0)

        for row in range(gridSize):
            for column in range(gridSize):
                pygame.draw.rect(screen, color, [(gridMargin + gridWidth) * column + gridMargin,(gridMargin + gridHeight) * row + gridMargin,gridWidth,gridHeight])

