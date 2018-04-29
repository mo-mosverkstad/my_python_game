#!/usr/bin/env python
import pygame, sys
from pygame.locals import *

### cell config
from general_color import *
from general_cell_config import Cell_map

# CONSTANTS DEFINITION
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = 'MOS PYGAME CODING'

# VARIABLES DEFINITION
continueFlag = True

### cell config -- begin
CELL_EDGE   = -1
CELL_GROUND = 0
CELL_BLOCK  = 1
CELL_RAT    = 2

CELL_COLOR_DICT = {CELL_GROUND : COLOR_LIGHTGREEN,
                   CELL_BLOCK  : COLOR_GRAY,
                   CELL_EDGE   : COLOR_YELLOW,
                   CELL_RAT    : COLOR_RED}

map_0001 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1,  0,  0,  0,  0,  0,  0,  0,  0, -1],
            [-1,  0,  0,  0,  1,  0,  1,  1,  1, -1],
            [-1,  0,  1,  0,  0,  0,  0,  0,  1, -1],
            [-1,  0,  0,  1,  0,  0,  0,  2,  1, -1],
            [-1,  0,  0,  0,  0,  0,  0,  0,  1, -1],
            [-1,  0,  0,  0,  0,  1,  1,  1,  1, -1],
            [-1,  0,  0,  0,  0,  0,  0,  0,  0, -1],
            [-1,  0,  0,  0,  0,  0,  0,  0,  0, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           ]

cell_map = Cell_map(30, 4, map_0001, CELL_COLOR_DICT)

SCREEN_WIDTH, SCREEN_HEIGHT = cell_map.get_screen_size()

def draw_map(map):
    for row in map.get_map_list():
        for item in row:
            pygame.draw.rect(screen, item.get_color(), item.get_pos())
    pygame.display.update()

### cell config -- end

# PYGAME INITIALISATION
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

draw_map(cell_map)
refresh = False

# PYGAME DEAD LOOP FOR RECEIVING EVENTS
while continueFlag: # main game loop

    # EVENTS HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            continueFlag = False
            print('pygame exit!')
            break
        elif event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if cell_map.get_cell_status(x, y) == CELL_GROUND:
                cell_map.set_cell_status(x, y, CELL_BLOCK)
                refresh = True

    # PAINT THE SCREEN
    if refresh:
        draw_map(cell_map)
        refresh = False

pygame.display.quit()
pygame.quit()