'''
Displays the graphical user interface (GUI) for the Sudoku game
'''

import pygame
import sys

# See constants.py for more information
from constants import *

def render_title(screen, position: (int, int), font_size=70) -> None:
    """
    Display the main menu of the game when called

    Parameters:
        screen: the display of pygame.display.set_mode
        position: places title at a position (x, y) where x and y are integers

    Returns:
        None
    """
    screen.fill(BG_COLOR)

    # Display title
    title = "Welcome to Sudoku!"
    title_color = (0, 0, 0)

    # Create font of text
    font = pygame.font.Font(None, font_size)
    img = font.render(title, True, title_color)

    # Render title in the center (for x) and in the top quarter (for y)
    x = (screen.get_width() - img.get_width()) / 2
    y = (screen.get_height() - img.get_height()) / 4

    screen.blit(img, (x, y))

def main():
    pygame.init()

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        render_title(screen, (100, 100))
        pygame.display.update()

if __name__ == '__main__':
    main()