'''
Displays the graphical user interface (GUI) for the Sudoku game
'''

import pygame
import sys

# See constants.py for more information
from constants import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_color = (0, 0, 0) # black
        self.background_color = (255, 255, 255) # white

    def render_main_menu(self):
        """
        Render the main menu
        """
        self.screen.fill(self.background_color)

        # Render text of main menu
        self.render_title()
        self.render_selection_difficulty()

    def render_title(self, font_size=70) -> None:
        """
        Display the main menu of the game when called

        Parameters:
            font_size: changes the font size of the title. Default: 70px

        Returns:
            None
        """

        # Display title
        title = "Welcome to Sudoku!"

        # Create font of title
        font = pygame.font.Font(None, font_size)
        img = font.render(title, True, self.font_color)

        # Render title in the center (for x) and in the top quarter (for y)
        x = (self.screen.get_width() - img.get_width()) / 2
        y = (self.screen.get_height() - img.get_height()) / 4

        self.screen.blit(img, (x, y))

    def render_selection_difficulty(self, font_size=50):
        """
        Display the difficulty selection text and buttons for user to click
        """

        text = "Select Game Mode:"
        
        # Create font of text
        font = pygame.font.Font(None, font_size)
        img = font.render(text, True, self.font_color)

        # Render text in the center (for x and y)
        x = (self.screen.get_width() - img.get_width()) / 2
        y = (self.screen.get_height() - img.get_height()) / 2

        self.screen.blit(img, (x, y))

def main():
    pygame.init()

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    menu = Menu(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        menu.render_main_menu()
        pygame.display.update()

if __name__ == '__main__':
    main()