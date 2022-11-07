import pygame
import sys
from button import Button
from grid import Cell
import pygame

#x = int(input("Podaj "))

pygame.init()

# Window
WIDTH1, HEIGHT1 = 900, 700
WIN = pygame.display.set_mode((WIDTH1, HEIGHT1))

# Title
pygame.display.set_caption("Wirtualny Swiat")

# Clock
clock = pygame.time.Clock()


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)
# UI


center = WIN.get_rect().center

"""""
def drawgrid(w, rows, surface):
    sizebtwn = w // rows
    for i in range(0, w, sizebtwn):
        x, y = i, i
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

class Cube:
    def update(self, sizebtwn):
        x, y = pygame.mouse.get_pos()
        ix = x // sizebtwn
        iy = y // sizebtwn
        self.cx, self.cy = ix * sizebtwn, iy * sizebtwn
        self.square = pygame.Rect(self.cx, self.cy, sizebtwn, sizebtwn)
    def draw(self, surface):
        click = pygame.mouse.get_pressed()
        if click[0]:
            pygame.draw.rect(surface, (255, 255, 255), self.square)

# MainGame window
game = pygame.Surface((400, 400))
WIN.blit(game, game.get_rect(center = WIN.get_rect().center))

drawgrid(game.get_width(), 10, game)
cube = Cube()
"""

game = pygame.Surface((400, 400))



WIDTH = 20
HEIGHT = 20
# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(50):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(25):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

def main():

    while True:
        dt = clock.tick()
        time_delta = clock.tick(60)/1000.0

        #for button in [PLAY_BUTTON]:
            #button.update(WIN)

        #cube.update(game.get_width() // 10)
        #cube.draw(game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
                print(grid)
         # Draw the grid
        for row in range(25):
            for column in range(25):
                color = (255,255,255)
                if grid[row][column] == 1:
                    color = (255, 45, 65)
                pygame.draw.rect(game,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        WIN.blit(game, game.get_rect(center = WIN.get_rect().center))


        pygame.display.update()

if __name__ == '__main__':
    main()
