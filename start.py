'''
Displays the graphical user interface (GUI) for the Sudoku game
'''

import pygame
import sys

def main():
    pygame.init()

    # Initialize the screen
    HEIGHT = 800
    WIDTH = 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()