'''
Displays the graphical user interface (GUI) for the Sudoku game
'''

import pygame
import sys

# See constants.py for more information
from constants import *

class Menu:
    '''
    Displays visuals for:
        - Main menu
        - Sudoku screen
        - Game over (win and lose)
    '''
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
        self.main_menu = self.MainMenu(self.screen, self.font_color, self.background_color)
        self.main_menu.render_title()
        self.main_menu.render_selection_difficulty()

    class MainMenu:
        """
        Display the main menu (or starting menu) of the game when called.

        Parameters:
            font_size: changes the font size of the title. Default: 70px

        Returns:
            None
        """

        def __init__(self, screen, font_color, background_color):
            self.font_color = font_color
            self.background_color = background_color
            self.screen = screen

            self.title = "Welcome to Sudoku!"
            self.select_game_mode = "Select Game Mode:"

        def render_title(self, font_size=70) -> None:
            """
            Renders title to screen
            """

            # Create font of title
            font = pygame.font.Font(None, font_size)
            img = font.render(self.title, True, self.font_color)

            # Render title in the center (for x) and in the top quarter (for y)
            x = (self.screen.get_width() - img.get_width()) / 2
            y = (self.screen.get_height() - img.get_height()) / 4

            self.screen.blit(img, (x, y))

        def render_selection_difficulty(self, font_size=50) -> None:
            """
            Display the difficulty selection text and buttons for user to click
            """

            # Create font of text
            font = pygame.font.Font(None, font_size)
            img = font.render(self.select_game_mode, True, self.font_color)

            # Render text in the center (for x and y)
            x = (self.screen.get_width() - img.get_width()) / 2
            y = (self.screen.get_height() - img.get_height()) / 2

            self.screen.blit(img, (x, y))

            # Render difficulty buttons to screen


class Button:
    '''
    Creates clickable buttons. Also defines default themes for clickable buttons.
    '''

    def __init__(self, x, y, width, height, button_text, on_click_function, one_press=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.on_click_function = on_click_function
        self.one_press = one_press # Can this button only be clicked once?
        self.already_pressed = False

    def render(self):
        '''
        Renders button to screen
        '''
        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

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