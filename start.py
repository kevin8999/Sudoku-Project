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

        self.button_font_size = 30

        # Checks the current menu that Menu is on
        self.current_menu = "main menu"

    def create_main_menu(self):
        self.screen.fill(self.background_color)

        # Render text of main menu
        self.main_menu = self.MainMenu(self.screen, self.font_color, self.background_color, self.button_font_size)
        self.main_menu.render_title()

    def render_main_menu(self):
        """
        Updates render of the main menu
        """
        self.current_menu = "main menu"
        self.main_menu.render_selection_difficulty()

    class MainMenu:
        """
        Display the main menu (or starting menu) of the game when called.

        Parameters:
            font_size: changes the font size of the title. Default: 70px

        Returns:
            None
        """

        def __init__(self, screen, font_color, background_color, button_font_size):
            self.font_color = font_color
            self.background_color = background_color
            self.screen = screen

            self.title = "Welcome to Sudoku!"
            self.select_game_mode = "Select Game Mode:"
            self.button_font_size = button_font_size

            self.create_buttons()

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
        
        def create_buttons(self):
            self.button_easy = Button(
                screen=self.screen,
                x=(self.screen.get_width()) * 1/4,
                y=(self.screen.get_height()) * 3/4,
                width=100,
                height=self.button_font_size * 1.25,
                button_text="Easy",
                on_click_function=test_function,
            )
            self.button_easy.draw()


def test_function():
    print("This button works!")


class Button:
    '''
    Creates clickable buttons. Also defines default themes for clickable buttons.
    '''

    def __init__(self, screen, x, y, width, height, button_text, on_click_function=None, one_press=True, fill_colors=None, font_size=30):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.on_click_function = on_click_function
        self.clicked = False
        self.font_size = font_size
        self.button_text = button_text

        if fill_colors == None:
            self.fill_colors = {
                'normal'  : '#ffffff',
                'hover'   : '#666666',
                'pressed' : '#333333'
            }

    def draw(self):
        # Draw the button
        font = pygame.font.Font(None, self.font_size)
        self.img = font.render(self.button_text, True, (0,0,0))

        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def process(self, event):
        mouse_pos = pygame.mouse.get_pos()
        self.button_surface.fill(self.fill_colors['normal'])

        # If mouse is inside button_rect, change the button color to hover
        if self.button_rect.collidepoint(mouse_pos):
            self.button_surface.fill(self.fill_colors['hover'])

            # If the left mouse button is held down while inside button_rect, call on_click_function() ONCE.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.button_rect.collidepoint(event.pos):
                    self.button_surface.fill(self.fill_colors['pressed'])
                    self.clicked = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.clicked and self.button_rect.collidepoint(event.pos):
                    # Check if button has already been clicked. If it has, do not run the function
                    if not self.clicked:
                        print(self.clicked)
                        self.clicked = True
                        self.on_click_function()
                        print(self.clicked)

        # Render button
        x = (self.button_rect.width - self.img.get_rect().width) * 1/2
        y = (self.button_rect.height - self.img.get_rect().height) * 1/2

        self.button_surface.blit(self.img, [x, y])
        self.screen.blit(self.button_surface, self.button_rect)

    def run(self):
        # Run the function set by self.on_click_function()
        self.on_click_function()

def main():
    pygame.init()

    fps = 60
    fps_clock = pygame.time.Clock()

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    menu = Menu(screen)
    menu.create_main_menu()
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if menu.current_menu == 'main menu':
                menu.main_menu.render_selection_difficulty()
                menu.main_menu.button_easy.process(event)

        # Main menu logic
        if menu.current_menu == "main menu":
            # Difficulty selection
            if menu.main_menu.button_easy.clicked == True:
                i += 1
                menu.main_menu.button_easy.clicked = False
                print(f"Pressed {i} times")
                menu.main_menu.button_easy.run()

        menu.render_main_menu()
        pygame.display.update()
        fps_clock.tick(fps)

if __name__ == '__main__':
    main()