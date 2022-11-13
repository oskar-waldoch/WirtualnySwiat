import pygame 
from swiat import Swiat


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
        '''
        Wilk - colors[2], Owca - colors[3], Pies - colors[4], Leniwiec - colors[5], Zmija - colors[6]

        '''

        for row in range(self.gridSize):
            for column in range(self.gridSize):
                if self.gridList[row][column] == " wilk1":
                    pygame.draw.rect(self.screen, self.colors[2], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                elif self.gridList[row][column] == " owca1":
                    pygame.draw.rect(self.screen, self.colors[3], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                else: 
                    pygame.draw.rect(self.screen, self.colors[0], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])