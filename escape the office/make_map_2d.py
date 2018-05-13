#!/usr/bin/env python
import pygame, sys
from pygame.locals import *

# CONFIGURATION OF SIZE
BLOCK_SIZE = 30
EDGE_SIZE = 10
BLOCKS_WIDTH = 5
BLOCKS_HEIGHT = 5

# CONFIGURATION OF BLOCK AND EDGE TYPE
COLOR_BLACK    = (   0,   0,   0)
COLOR_GRAY     = ( 127, 127, 127)
COLOR_WHITE    = ( 255, 255, 255)
COLOR_GREEN    = (   0, 255,   0)
COLOR_RED      = ( 255,   0,   0)
COLOR_YELLOW   = ( 255, 255,   0)
COLOR_OLIVE    = ( 150, 150,   0)
COLOR_BLUE     = (   0,   0, 255)
COLOR_LIGHTGREEN = (155, 255,155)

COLOR_NONE  = COLOR_BLACK
COLOR_EMPTY = COLOR_WHITE
COLOR_WALL  = ( 63,  63,  63)

TYPE_NONE  = -2
TYPE_WALL  = -1
TYPE_EMPTY = 0
TYPE_KEY_1 = 1
TYPE_KEY_2 = 2
TYPE_KEY_3 = 3
TYPE_KEY_4 = 4

TYPE_VALID_SEGMENT = 6
TYPE_VALID_OFFSET  = -1

TYPE_TEST = 200

DICT_COLOR = {TYPE_NONE : COLOR_NONE,
              TYPE_EMPTY: COLOR_EMPTY,
              TYPE_WALL : COLOR_WALL,
              TYPE_EMPTY: COLOR_EMPTY,
              TYPE_KEY_1: COLOR_RED,
              TYPE_KEY_2: COLOR_GREEN,
              TYPE_KEY_3: COLOR_BLUE,
              TYPE_KEY_4: COLOR_YELLOW,
              TYPE_TEST : COLOR_GRAY,
             }

DEFAULT_MAP_BLOCK = [[TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY],
                     [TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY],
                     [TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY],
                     [TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY],
                     [TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY, TYPE_EMPTY],
                    ]

DEFAULT_MAP_EDGE_V = [[TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                     ]

DEFAULT_MAP_EDGE_H = [[TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                      [TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL, TYPE_WALL],
                     ]

TYPE_STRING_BLOCK  = 'BLOCK'
TYPE_STRING_EDGE_V = 'EDGE_V'
TYPE_STRING_EDGE_H = 'EDGE_H'


# CONSTANTS DEFINITION
SEGMENT_SIZE  = EDGE_SIZE + BLOCK_SIZE
SCREEN_WIDTH  = EDGE_SIZE + SEGMENT_SIZE * BLOCKS_WIDTH
SCREEN_HEIGHT = EDGE_SIZE + SEGMENT_SIZE * BLOCKS_HEIGHT
SCREEN_TITLE = 'MOS PYGAME CODING'


#FUNCTIONS
def gen_pos_by_index(x_index, y_index):
    x = EDGE_SIZE + SEGMENT_SIZE * x_index
    y = EDGE_SIZE + SEGMENT_SIZE * y_index
    return [x, y, BLOCK_SIZE, BLOCK_SIZE]

def gen_pos_edge_v_by_index(x_index, y_index):
    x = EDGE_SIZE + SEGMENT_SIZE * x_index
    y = SEGMENT_SIZE * y_index
    return [x, y, BLOCK_SIZE, EDGE_SIZE]

def gen_pos_edge_h_by_index(x_index, y_index):
    x = SEGMENT_SIZE * x_index
    y = EDGE_SIZE + SEGMENT_SIZE * y_index
    return [x, y, EDGE_SIZE, BLOCK_SIZE]

DICT_FUNC = {TYPE_STRING_BLOCK : gen_pos_by_index,
             TYPE_STRING_EDGE_V: gen_pos_edge_v_by_index,
             TYPE_STRING_EDGE_H: gen_pos_edge_h_by_index,
            }

def gen_index_by_pos(x, y):
    type_string_x, type_string_y = 'None', 'None'
    index_x, index_y = 0, 0
    if y < EDGE_SIZE:
        type_string_x, index_x = gen_index_x(x)
        type_string_y = TYPE_STRING_EDGE_V
        index_y = 0
    elif x < EDGE_SIZE:
        type_string_y, index_y = gen_index_y(y)
        type_string_x = TYPE_STRING_EDGE_H
        index_x = 0
    else:
        type_string_x, index_x = gen_index_x(x)
        type_string_y, index_y = gen_index_y(y)
    #print(type_string_x, type_string_y, index_x, index_y)
    return DICT_MAP[type_string_x][type_string_y], index_x, index_y

    

def gen_index_x(x):
    index = int(x / SEGMENT_SIZE)
    rem   = int(x % SEGMENT_SIZE)
    if rem >= EDGE_SIZE: return TYPE_STRING_BLOCK, index
    else: return TYPE_STRING_EDGE_H, index

def gen_index_y(y):
    index = int(y / SEGMENT_SIZE)
    rem   = int(y % SEGMENT_SIZE)
    if rem >= EDGE_SIZE: return TYPE_STRING_BLOCK, index
    else: return TYPE_STRING_EDGE_V, index

def draw_map(screen, map_list, func_type):
    for y_index in range(len(map_list)):
        for x_index in range(len(map_list[y_index])):
            cell_status = map_list[y_index][x_index]
            pygame.draw.rect(screen,
                             DICT_COLOR[cell_status],
                             DICT_FUNC[func_type](x_index, y_index))

def draw_screen(screen, block_list, edge_v_list, edge_h_list):
    draw_map(screen, block_list,  TYPE_STRING_BLOCK)
    draw_map(screen, edge_v_list, TYPE_STRING_EDGE_V)
    draw_map(screen, edge_h_list, TYPE_STRING_EDGE_H)
    
    pygame.display.update()


def write_map_to_file(file, block_list, edge_v_list, edge_h_list):
    with open(file, 'w') as file_handler:
        file_handler.write("{}\n".format(block_list))
        file_handler.write("{}\n".format(edge_v_list))
        file_handler.write("{}\n".format(edge_h_list))

def load_map_to_file(file):
    block_list, edge_v_list, edge_h_list = None, None, None
    try:
        with open(file, 'r') as file_handler:
            lists = file_handler.readlines()
            return eval(lists[0].rstrip()), eval(lists[1].rstrip()), eval(lists[2].rstrip())
    except FileNotFoundError:
        return DEFAULT_MAP_BLOCK, DEFAULT_MAP_EDGE_V, DEFAULT_MAP_EDGE_H


# VARIABLES DEFINITION
continueFlag = True
refresh = False


# PYGAME INITIALISATION
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

MAP_BLOCK, MAP_EDGE_V, MAP_EDGE_H = load_map_to_file('map.txt')

DICT_MAP = {TYPE_STRING_BLOCK:  {TYPE_STRING_BLOCK : MAP_BLOCK,
                                 TYPE_STRING_EDGE_V: MAP_EDGE_V,
                                 TYPE_STRING_EDGE_H: None},
            TYPE_STRING_EDGE_V: {TYPE_STRING_BLOCK : None,
                                 TYPE_STRING_EDGE_V: None,
                                 TYPE_STRING_EDGE_H: None},
            TYPE_STRING_EDGE_H: {TYPE_STRING_BLOCK : MAP_EDGE_H,
                                 TYPE_STRING_EDGE_V: None,
                                 TYPE_STRING_EDGE_H: None},
           }

draw_screen(screen, MAP_BLOCK, MAP_EDGE_V, MAP_EDGE_H)

# PYGAME DEAD LOOP FOR RECEIVING EVENTS
while continueFlag: # main game loop

    # EVENTS HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            continueFlag = False
            write_map_to_file('map.txt', MAP_BLOCK, MAP_EDGE_V, MAP_EDGE_H)
            print('pygame exit!')
            break
        elif event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            map, index_x, index_y = gen_index_by_pos(x, y)
            if map != None:
                map[index_y][index_x] = (map[index_y][index_x] - TYPE_VALID_OFFSET + 1) % TYPE_VALID_SEGMENT + TYPE_VALID_OFFSET
                refresh = True
            
            

    # PAINT THE SCREEN
    if refresh:
        draw_screen(screen, MAP_BLOCK, MAP_EDGE_V, MAP_EDGE_H)
        refresh = False

pygame.display.quit()
pygame.quit()