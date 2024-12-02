import pygame


class Cell:
    def __init__(self, value, row, col, screen, width, height):
        self.value = value
        self.row= row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.width = width
        self.height = height
        self.is_initial = value != 0


    #Setter for this cell’s value
    def set_cell_value(self, value):
        self.value = value


    #Setter for this cell’s sketched value
    def set_sketched_value(self, value):
        self.sketched_value = value



    ''' Draws this cell, along with the value inside it.
    If this cell has a nonzero value, that value is displayed.
    Otherwise, no value is displayed in the cell.
    The cell is outlined red if it is currently selected.'''
    def draw(self):
        font = pygame.font.Font(None, 40)
        x = self.col*self.width
        y = self.row*self.height

        if self.selected:
            pygame.draw.rect(self.screen, (255,0,0), (x, y, self.width, self.height), 3)
            
            
        if self.value != 0:
            text = font.render(str(self.value), 1, (0,0,0))
            self.screen.blit(text, (x + self.width//2 - text.get_width()//2,
                                    y + self.height//2 - text.get_height()//2))

        elif self.sketched_value != 0:
            text = font.render(str(self.sketched_value), 1, (120,120,120))
            self.screen.blit(text, (x+5, y+5))
    
    def erase(self):
        x = self.col * self.width
        y = self.row * self.height
        
        self.selected = False
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.width, self.height), 3)
        