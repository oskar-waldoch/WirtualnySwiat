import pygame 
from swiat import Swiat


class Grid:

    gridList = []
    gridSize = 0

    def __init__(self, screen, gridSize, gridMargin, gridWidth, gridHeight, colors):
        self.screen = screen
        self.gridSize = gridSize
        self.gridMargin = gridMargin
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.colors = colors


    def createGrid(self):

        for row in range(self.gridSize):
            self.gridList.append([])
            for column in range(self.gridSize):
                self.gridList[row].append(0)

        for row in range(self.gridSize):
            for column in range(self.gridSize):
                pygame.draw.rect(self.screen, self.colors[0], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                    
    def clearGrid(self):
        for row in range(self.gridSize):
            for column in range(self.gridSize):
                self.gridList[row][column] = 0

    def updateGrid(self):
        '''
        Wilk - colors[2], Owca - colors[3], Pies - colors[4], Leniwiec - colors[5], Zmija - colors[6],
        trawa - colors[7] , mlecz - colors[8], wilczaJagoda - colors[9]

        '''

        for row in range(self.gridSize):
            for column in range(self.gridSize):
                if self.gridList[row][column] == " wilk":
                    pygame.draw.rect(self.screen, self.colors[2], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                elif self.gridList[row][column] == " owca":
                    pygame.draw.rect(self.screen, self.colors[3], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                elif self.gridList[row][column] == " pies":
                    pygame.draw.rect(self.screen, self.colors[4], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                elif self.gridList[row][column] == " leniwiec":
                    pygame.draw.rect(self.screen, self.colors[5], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                elif self.gridList[row][column] == " zmija":
                    pygame.draw.rect(self.screen, self.colors[6], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                elif self.gridList[row][column] == " trawa":
                    pygame.draw.rect(self.screen, self.colors[7], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                elif self.gridList[row][column] == " mlecz":
                    pygame.draw.rect(self.screen, self.colors[8], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                elif self.gridList[row][column] == " wilczaJagoda":
                    pygame.draw.rect(self.screen, self.colors[9], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
                else: 
                    pygame.draw.rect(self.screen, self.colors[0], [(self.gridMargin + self.gridWidth)
                    * column + self.gridMargin,(self.gridMargin + self.gridHeight)
                    * row + self.gridMargin,self.gridWidth,self.gridHeight])
    
