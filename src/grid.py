import pygame 

class Grid:

    def __init__(self, screen, gridSize, gridMargin, gridWidth, gridHeight, colors):
        self.screen = screen
        self.gridSize = gridSize
        self.gridMargin = gridMargin
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.colors = colors
        self.gridList = []

    def createGrid(self):
        self.gridList = []

        for row in range(self.gridSize):
            self.gridList.append([])
            for column in range(self.gridSize):
                self.gridList[row].append(0)

        for row in range(self.gridSize):
            for column in range(self.gridSize):
                pygame.draw.rect(self.screen, self.colors[0], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])

    def updateGrid(self):

        for row in range(self.gridSize):
            for column in range(self.gridSize):
                if self.gridList[row][column] == " wilk1":
                    pygame.draw.rect(self.screen, self.colors[2], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                else: 
                    pygame.draw.rect(self.screen, self.colors[0], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])