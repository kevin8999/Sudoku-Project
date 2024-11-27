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
    def __init__(self, screen, font_color=(0,0,0), background_color=(255,255,255)):
        self.screen = screen
        self.font_color = font_color
        self.background_color = background_color

        # Checks the current menu that Menu is on
        self.current_menu = ""

    def render_text(self, text: str, font_size: int, pos: (int, int), font_family=None):
        '''
        Render text at position (x, y) with a specific font size
        '''
        # Create font of text
        font = pygame.font.Font(font_family, font_size)
        img = font.render(text, True, self.font_color)

        # Display text to screen
        x, y = pos
        self.screen.blit(img, (x, y))

    def get_img_size(self, text: str, font_size: int, font_family=None):
        # Get the size of a text box's image
        font = pygame.font.Font(font_family, font_size)
        img = font.render(text, True, self.font_color)

        return img.get_width(), img.get_height()


class MainMenu(Menu):
    """
    Display the main menu (or starting menu) of the game when MainMenu.render() is called

    Parameters:
        font_size: changes the font size of the title. Default: 70px

    Returns:
        None
    """

    def __init__(self, screen, button_font_size=30):
        super().__init__(screen)

        self.title = "Welcome to Sudoku!"
        self.select_game_mode = "Select Game Mode:"
        self.button_font_size = button_font_size

    def render(self):
        self.current_menu = "main menu"

        self.screen.fill(self.background_color)

        ##### TITLE #####

        # Render title in the center (for x) and in the top quarter (for y)
        img_width, img_height = self.get_img_size(text=self.title, font_size=70)

        x = (self.screen.get_width() - img_width) / 2
        y = (self.screen.get_height() - img_height) / 4

        self.render_text(
            text = self.title,
            font_size = 70,
            pos = (x, y),
            font_family = None
        )

        ##### DIFFICULTY SELECTION #####
        # Render difficulty selection in the center (for x) and in the middle (for y)
        img_width, img_height = self.get_img_size(text=self.select_game_mode, font_size=50)

        x = (self.screen.get_width() - img_width) / 2
        y = (self.screen.get_height() - img_height) / 2

        self.render_text(
            text = self.select_game_mode,
            font_size = 50,
            pos = (x, y),
            font_family = None
        )

        # Create buttons for easy, medium, and hard
        self.create_buttons()
    
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

        # Draw buttons to screen
        self.button_easy.draw()
        self.button_medium.draw()
        self.button_hard.draw()

    def set_menu(self, Parent, new_menu):
        Parent.current_menu = new_menu

class SudokuMenu(Menu):
    # Draws sudoku board and menu buttons below sudoku board
    def __init__(self, difficulty):
        self.difficulty = difficulty

class GameOverMenu(Menu):
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
    menu.current_menu = 'main menu'

    main_menu = MainMenu(screen)
    main_menu.render()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if menu.current_menu == 'main menu':
                main_menu.button_easy.process(event)
                main_menu.button_medium.process(event)
                main_menu.button_hard.process(event)

        """
        LOGIC FOR ALL MENUS
        
        Each nested if statement ensures that if a button is clicked once, it is run once.
        """

        # Main menu logic
        if menu.current_menu == "main menu":
            # Check if user clicked easy, medium, or hard button
            if main_menu.button_easy.clicked == True:
                main_menu.button_easy.clicked = False
                sudoku_menu = SudokuMenu('easy')
            elif main_menu.button_medium.clicked == True:
                main_menu.button_medium.clicked = False
                sudoku_menu = SudokuMenu('medium')
            elif main_menu.button_hard.clicked == True:
                main_menu.button_hard.clicked = False
                sudoku_menu = SudokuMenu('hard')

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
