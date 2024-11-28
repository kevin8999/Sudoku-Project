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

        cell_width = width//9
        cell_height = height//9
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

