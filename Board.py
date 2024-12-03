import pygame
from sudoku_generator import generate_sudoku
from constants import *
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.cells = []
        self.selected_cell = None

        difficulty_cells = {"EASY": 30, "MEDIUM": 40, "HARD": 50}
        removed_cells = difficulty_cells[difficulty]
        self.board = generate_sudoku(9, removed_cells)

        cell_width = width/9
        cell_height = height/9
        for i in range(9):
            row = []
            for j in range(9):
                row.append(Cell(self.board[i][j], i, j, self.screen, cell_width, cell_height))
            self.cells.append(row)
    def draw(self):
        #Draw grid lines
        for i in range(1,10):
            if i % 3 == 0:
                line_width = 4
            else:
                line_width = 1
            pygame.draw.line(self.screen, (0,0,0),(0,i*self.height//9),(self.width,i*self.height//9),line_width)
            pygame.draw.line(self.screen, (0,0,0), (i*self.width//9,0),(i*self.width//9,self.height),line_width)

        #Draw cells
        for row in self.cells:
            for cell in row:
                cell.draw()
    def drawgrid(self):
        for i in range(1,10):
            if i % 3 == 0:
                line_width = 4
            else:
                line_width = 1
            pygame.draw.line(self.screen, (0,0,0),(0,i*self.height//9),(self.width,i*self.height//9),line_width)
            pygame.draw.line(self.screen, (0,0,0), (i*self.width//9,0),(i*self.width//9,self.height),line_width)
            
    def select(self, row, col):
        if row in range(0,9) and col in range(0,9) :
            self.selected_cell = self.cells[row][col]
            self.selected_cell.selected = True
            self.draw()
        else:
            self.draw()
            pass
            
    def click(self, row, col):
        cell_width = self.width // 9
        cell_height = self.height // 9
        if row // cell_width in range(len(self.cells)) and col // cell_height in range (len(self.cells[0])):
            return row // cell_width, col // cell_height
        return None
            
        
                    
        
    
    def clear(self):
        if self.selected_cell and not self.selected_cell.is_initial:
            self.selected_cell.value = 0
        return self.selected_cell
    
    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)
        
        
    def place_number(self, value):
        self.selected_cell.set_cell_value(value)
        
    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                if not cell.is_initial:
                    cell.set_cell_value(0)
                    cell.set_sketched_value(0)

        
                    
                
                    
        
        
    def is_full(self):
        cellcount = 0
        for i in self.cells:
            for cell in i:
                if cell.value != 0:
                    cellcount += 1
        if cellcount == 81:
            return True
        return False
                
    def update_board(self):
        row = self.selected_cell.row
        col = self.selected_cell.col
        self.cells[row][col].value = self.selected_cell.value
        
    def find_empty(self):
        for i in self.cells:
            for cell in i:
                if cell.value == 0:
                    return cell.row, cell.col
    
    def check_board(self):
        # Check rows
        for row in self.board:
            if not self.is_valid_group([cell.value for cell in row]):
                return False
        
    
        for col in range(9):
            if not self.is_valid_group([self.board[row][col].value for row in range(9)]):
                return False
        

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [self.board[x][y].value for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid_group(box):
                    return False
        
        return True
    
    def is_valid_group(self, group):
        filled = [num for num in group if num != 0]
        return len(filled) == len(set(filled)) and all(1 <= num <= 9 for num in filled)
        
    