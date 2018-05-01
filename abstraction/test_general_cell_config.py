#!/usr/bin/env python
import pygame, sys
from pygame.locals import *

from general_color import *
from general_cell_config import Cell_map
from general_game_config import Game_status, Game_text

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

### cell config -- end

### game status -- begin
game_status = Game_status()
### game status -- end


def draw_map(map):
    for row in map.get_map_list():
        for item in row:
            pygame.draw.rect(screen, item.get_color(), item.get_pos())

def draw_screen(map, game_status):
    draw_map(map)
    if   game_status.get_status() == Game_status.GAME_WIN:  text_you_win.draw()
    elif game_status.get_status() == Game_status.GAME_FAIL: text_you_fail.draw()
    pygame.display.update()



### customerized game code -- begin
def on_mouse_down(map, pos, game_status):
    x,y = pos
    if map.get_cell_status(x, y) == CELL_GROUND:
        map.set_cell_status(x, y, CELL_BLOCK)
        return True
    elif map.get_cell_status(x, y) == CELL_BLOCK:
        game_status.set_status(Game_status.GAME_FAIL)
        return True
    elif map.get_cell_status(x, y) == CELL_RAT:
        game_status.set_status(Game_status.GAME_WIN)
        return True
    return False
### customerized game code -- end

# PYGAME INITIALISATION
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

font_comicSans = pygame.font.SysFont('Comic Sans MS', 30)
text_you_win   = Game_text(screen, font_comicSans, "YOU WIN !!!", COLOR_RED, (0, 0))
text_you_fail  = Game_text(screen, font_comicSans, "YOU FAIL!!!", COLOR_RED, (0, 0))

draw_screen(cell_map, game_status)
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
            if game_status.get_status() != Game_status.GAME_CONTINUE: continue
            refresh = on_mouse_down(cell_map, event.pos, game_status)

    # PAINT THE SCREEN
    if refresh:
        draw_screen(cell_map, game_status)
        refresh = False



pygame.display.quit()
pygame.quit()