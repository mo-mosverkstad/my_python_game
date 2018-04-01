#!/usr/bin/env python
import pygame, sys
from pygame.locals import *
import sys
sys.path.append('../my_canvas/')
from my_color import *
from my_canvas_lib import *

# CONSTANTS DEFINITION
SCREEN_TITLE = 'MOS PYGAME CODING'
BLOCK_SIZE = 30
EDGE_SIZE = 4
BLOCKS = 15
EDGES = 1
SCREEN_WIDTH = EDGE_SIZE+(BLOCK_SIZE+EDGE_SIZE)*BLOCKS
SCREEN_HEIGHT = EDGE_SIZE+(BLOCK_SIZE+EDGE_SIZE)*BLOCKS

CELL_EDGE = -1
CELL_GROUND = 0
CELL_BLOCK = 1
SEGMENT = EDGE_SIZE + BLOCK_SIZE

# VARIABLES DEFINITION
continueFlag = True
refresh = False


# PYGAME INITIALISATION
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
mouse_img = pygame.image.load('mouse.png')
mouse_img.set_colorkey(COLOR_WHITE, RLEACCEL)
mouse_img_size = mouse_img.get_rect().size

def drawer(longlist):
    for item in longlist:
        cell_pos, cell_status = item
        if cell_status == CELL_GROUND: cell_color = COLOR_LIGHTGREEN
        elif cell_status == CELL_BLOCK: cell_color = COLOR_GRAY
        elif cell_status == CELL_EDGE: cell_color = COLOR_YELLOW
        pygame.draw.rect(screen, cell_color, cell_pos)

def gen_data_list():
    data_list = []
    for y_index in range(BLOCKS):
        for x_index in range(BLOCKS):
            x = EDGE_SIZE + SEGMENT*x_index
            y = EDGE_SIZE + SEGMENT*y_index
            if (x_index < EDGES) or ((BLOCKS-1-EDGES) < x_index) or (y_index < EDGES) or ((BLOCKS-1-EDGES) < y_index):
                cell_status = CELL_EDGE
            else:
                cell_status = CELL_GROUND

            data_list.append(([x,y,BLOCK_SIZE,BLOCK_SIZE], cell_status))
    return data_list


def sensor(longlist, x, y):
    x_index = int(x / (EDGE_SIZE + BLOCK_SIZE))
    y_index = int(y / (EDGE_SIZE + BLOCK_SIZE))
    cell_pos, cell_status = longlist[y_index * BLOCKS + x_index]
    if cell_status == CELL_GROUND:
        longlist[y_index * BLOCKS + x_index] = (cell_pos, CELL_BLOCK)
        return True
    else:
        return False


data_list = gen_data_list()
drawer(data_list)
screen.blit(mouse_img,(EDGE_SIZE,EDGE_SIZE))
pygame.display.update()

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
            refresh = sensor(data_list, x, y)

    # PAINT THE SCREEN
    if refresh:
        drawer(data_list)
        pygame.display.update()
        refresh = False


    

pygame.display.quit()
pygame.quit()
