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

        # Checks the current menu that Menu is on
        self.current_menu = "main menu"

    def create_main_menu(self):
        self.current_menu = "main menu"

        self.screen.fill(self.background_color)

        # Render text of main menu
        self.main_menu = self.MainMenu(self.screen, self.font_color, self.background_color, self.button_font_size)
        self.main_menu.render_title()
        self.main_menu.render_selection_difficulty()
        self.main_menu.create_buttons()

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
            height = self.button_font_size * 1.25
            width = 100
            self.button_easy = Button(
                screen=self.screen,
                x=(self.screen.get_width() * 1/4) - 0.5*width,
                y=(self.screen.get_height() * 3/4) - height,
                width=width,
                height=self.button_font_size * 1.25,
                button_text="Easy",
                on_click_function=test_function  # TODO: CHANGE SO THAT BUTTONS CAN RUN A GAME
            )

            self.button_medium = Button(
                screen=self.screen,
                x=(self.screen.get_width() * 1/2) - 0.5*width,
                y=(self.screen.get_height() * 3/4) - height,
                width=width,
                height=self.button_font_size * 1.25,
                button_text="Medium",
                on_click_function=test_function  # TODO: CHANGE SO THAT BUTTONS CAN RUN A GAME
            )

            self.button_hard = Button(
                screen=self.screen,
                x=(self.screen.get_width() * 3/4) - 0.5*width,
                y=(self.screen.get_height() * 3/4) - height,
                width=width,
                height=self.button_font_size * 1.25,
                button_text="Hard",
                on_click_function=test_function  # TODO: CHANGE SO THAT BUTTONS CAN RUN A GAME
            )

            self.button_easy.draw()
            self.button_medium.draw()
            self.button_hard.draw()

    class Sudoku:
        # Draws sudoku board and menu buttons below sudoku board
        def __init__(self):
            pass

    class GameOver:
        def __init__(self, user_won: bool):
            self.user_won = user_won

        def render_text(self, font_size=30):
            '''
            Renders game over text to user. The game over text will depend on if the user won or lost
            '''
            text = ''
            if user_won:
                text = 'Game Won!'
            else:
                text = 'Game Over :('

            # Create font of text
            font = pygame.font.Font(None, font_size)
            img = font.render(text, True, text)

            # Render title in the center (for x) and in the top quarter (for y)
            x = (self.screen.get_width() - img.get_width()) / 2
            y = (self.screen.get_height() - img.get_height()) / 4

            self.screen.blit(img, (x, y))

def test_function(difficulty):
    print(difficulty)


class Button:
    '''
    Creates clickable buttons. Also defines default themes for clickable buttons.
    '''

    def __init__(self, screen, x, y, width, height, button_text, on_click_function=None, one_press=True, fill_colors=None, font_size=30, font_color=(0,0,0)):
        self.screen = screen
        self.x = x # Temporary x
        self.y = y # Temporary y
        self.width = width
        self.height = height
        self.on_click_function = on_click_function
        self.clicked = False
        self.font_size = font_size
        self.button_text = button_text
        self.font_color = font_color

        if fill_colors == None:
            self.fill_colors = {
                'normal'  : '#4ad827',
                'hover'   : '#1d2cf9',
                'pressed' : '#d82c27'
            }

    def draw(self):
        # Draw the button
        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_surface.fill(self.fill_colors['normal'])

        # Create text for button
        font = pygame.font.Font(None, self.font_size)
        self.img = font.render(self.button_text, True, self.font_color)

        # Calculate text position to center it within the button
        self.text_x = (self.width - self.img.get_width()) // 2
        self.text_y = (self.height - self.img.get_height()) // 2

        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Permanently assign x and y to take img height and width into consideration
        self.x = self.x - self.img.get_width()
        self.y = self.y - self.img.get_height()

        self.button_surface.blit(self.img, (self.text_x, self.text_y))
        self.screen.blit(self.button_surface, self.button_rect)

    def process(self, event):
        mouse_pos = pygame.mouse.get_pos()
        self.button_surface.fill(self.fill_colors['normal'])

        # If mouse is inside button_rect, change the button color to hover
        if self.button_rect.collidepoint(mouse_pos):
            self.button_surface.fill(self.fill_colors['hover'])

            # If clicked, color the button as if it were pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.button_rect.collidepoint(event.pos):
                    self.button_surface.fill(self.fill_colors['pressed'])
                    self.clicked = True

            if event.type == pygame.MOUSEBUTTONUP:
                if self.clicked and self.button_rect.collidepoint(event.pos):
                    # Check if button has already been clicked. If it has, do not run the function
                    self.clicked = False
                    print(self.clicked)

        # Render button (useful in case the user hovers over the button and the fill color must be changed)
        self.button_surface.blit(self.img, (self.text_x, self.text_y))
        self.screen.blit(self.button_surface, self.button_rect)

    def run(self, *args):
        # Run the function set by self.on_click_function()
        self.on_click_function(*args)

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
                menu.main_menu.button_easy.process(event)
                menu.main_menu.button_medium.process(event)
                menu.main_menu.button_hard.process(event)

        """
        LOGIC FOR ALL MENUS
        
        Each nested if statement ensures that if a button is clicked once, it is run once.
        """

        # Main menu logic
        if menu.current_menu == "main menu":
            # Check if user clicked easy, medium, or hard button
            if menu.main_menu.button_easy.clicked == True:
                menu.main_menu.button_easy.clicked = False
                menu.main_menu.button_easy.run('easy')
            elif menu.main_menu.button_medium.clicked == True:
                menu.main_menu.button_medium.clicked = False
                menu.main_menu.button_medium.run('medium')
            elif menu.main_menu.button_hard.clicked == True:
                menu.main_menu.button_hard.clicked = False
                menu.main_menu.button_hard.run('hard')

        # Sudoku board
        elif menu.current_menu == 'sudoku board':
            pass

        # Game over (win screen) logic
        elif menu.current_menu == 'game over win':
            pass
        
        # Game over (lose screen) logic
        elif menu.current_menu == 'game over lose':
            pass

        pygame.display.flip()
        fps_clock.tick(fps)

if __name__ == '__main__':
    main()
