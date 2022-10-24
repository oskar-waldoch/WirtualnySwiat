import pygame
import sys
import pygame_gui

pygame.init()

# Window
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Title
pygame.display.set_caption("Wirtualny Swiat")

# Clock
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((800, 600))

def main():

    while True:
        dt = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()

if __name__ == '__main__':
    main()
