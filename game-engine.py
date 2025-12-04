import pygame
import copy
import random


def loadImage(path , size ):
    pass


import pygame
import copy
import random
import sys

def loadImage(path, size):
    return None

def loadsheet(path, rows, columns, size):
    return []

class Grid:
    def __init__(self, rows, columns, cell_size, main):
        self.main = main
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.board_origin = (50, 50)
        self.grid = self.grid_gen(rows, columns)

    def grid_gen(self, rows, columns):
        return [[None for _ in range(columns)] for _ in range(rows)]

    def draw(self, screen):
        origin_x, origin_y = self.board_origin
        cell_w, cell_h = self.cell_size
        for r in range(self.rows):
            for c in range(self.columns):
                x = origin_x + c * cell_w
                y = origin_y + r * cell_h
                rect = pygame.Rect(x, y, cell_w - 2, cell_h - 2)
                pygame.draw.rect(screen, (0, 100, 0), rect)
                val = self.grid[r][c]
                if val == 'B':
                    pygame.draw.circle(screen, (0, 0, 0), rect.center, min(cell_w, cell_h)//2 - 6)
                elif val == 'W':
                    pygame.draw.circle(screen, (255, 255, 255), rect.center, min(cell_w, cell_h)//2 - 6)

    def handle_click(self, pos):
        mx, my = pos
        ox, oy = self.board_origin
        cw, ch = self.cell_size
        if mx < ox or my < oy:
            return
        c = (mx - ox) // cw
        r = (my - oy) // ch
        if 0 <= r < self.rows and 0 <= c < self.columns:
            current = self.grid[r][c]
            if current is None:
                self.grid[r][c] = 'B'
            elif current == 'B':
                self.grid[r][c] = 'W'
            else:
                self.grid[r][c] = None

    def print_gamelogic(self):
        print(' | A | B | C | D | E | F | G | H |')
        for i, row in enumerate(self.grid):
            print('---------------------------------')
            row_str = f'{i+1} |'
            for cell in row:
                if cell is None:
                    row_str += '   |'
                else:
                    row_str += f' {cell} |'
            print(row_str)

class Othello:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Othello Game')
        self.clock = pygame.time.Clock()
        self.rows = 8
        self.columns = 8
        cell_size = (60, 60)
        self.grid = Grid(self.rows, self.columns, cell_size, self)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.grid.handle_click(pos)

            self.screen.fill((0, 128, 0))
            self.grid.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def printGamelogic(self):
        self.grid.print_gamelogic()

    def quit(self):
        pygame.quit()

if __name__ == '__main__':
    game = Othello()
    game.run()
    game.printGamelogic()
    game.quit()

