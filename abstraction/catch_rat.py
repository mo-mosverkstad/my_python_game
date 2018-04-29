#!/usr/bin/env python
import pygame
from pygame.locals import *

import sys
sys.path.append('../my_canvas/')
from my_color import *
from random import randint

from rat_map import rat_map_dict
from rat_path import mouse_opt_path

# CONSTANTS DEFINITION
SCREEN_TITLE = 'MOS PYGAME CODING'

# CONFIGURATION OF SIZE
BLOCK_SIZE = 30
EDGE_SIZE = 4
BLOCKS_WIDTH = 11
BLOCKS_HEIGHT = 11
EDGES = 1
SEGMENT_SIZE  = EDGE_SIZE + BLOCK_SIZE
SCREEN_WIDTH  = EDGE_SIZE + SEGMENT_SIZE * (BLOCKS_WIDTH-1)
SCREEN_HEIGHT = EDGE_SIZE + SEGMENT_SIZE * (BLOCKS_HEIGHT-1)

# CONFIGURATION OF CELL STATUS
CELL_EDGE   = -1
CELL_GROUND = 0
CELL_BLOCK  = 1
CELL_RAT    = 2

CELL_COLOR_DICT = {CELL_GROUND : COLOR_LIGHTGREEN,
                   CELL_BLOCK  : COLOR_GRAY,
                   CELL_EDGE   : COLOR_YELLOW,
                   CELL_RAT    : COLOR_LIGHTGREEN}

# CONFIGURATION OF GAME STATUS
GAME_CONTINUE = 0
GAME_FAIL     = -1
GAME_WIN      = 1

# VARIABLES DEFINITION
continueFlag = True
refresh = False
rat_pos_index, map_list = rat_map_dict["#0001"]


# PYGAME INITIALISATION
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font_comicSans = pygame.font.SysFont('Comic Sans MS', 30)
text_you_win   = font_comicSans.render('YOU WIN!!!', False, COLOR_RED)
text_you_fail  = font_comicSans.render('YOU FAIL!!', False, COLOR_RED)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
rat_img = pygame.image.load('mouse.png')
rat_img.set_colorkey(COLOR_WHITE, RLEACCEL)
rat_img_size = rat_img.get_rect().size

def gen_pos_by_index(x_index, y_index):
    x = EDGE_SIZE + SEGMENT_SIZE * x_index
    y = EDGE_SIZE + SEGMENT_SIZE * y_index
    return [x, y, BLOCK_SIZE, BLOCK_SIZE]

def gen_index_by_pos(x, y):
    x_index = int((x-EDGE_SIZE)/SEGMENT_SIZE)
    y_index = int((y-EDGE_SIZE)/SEGMENT_SIZE)
    return x_index, y_index

def draw_map(map_list):
    for y_index in range(len(map_list)):
        for x_index in range(len(map_list[y_index])):
            cell_status = map_list[y_index][x_index]
            pygame.draw.rect(screen,
                             CELL_COLOR_DICT[cell_status],
                             gen_pos_by_index(x_index, y_index))

def draw_screen(map_list, rat_pos_index, game_status):
    draw_map(map_list)
    rat_x_index, rat_y_index = rat_pos_index
    screen.blit(rat_img, gen_pos_by_index(rat_x_index, rat_y_index))
    if game_status == GAME_WIN:
        screen.blit(text_you_win, (0,0))
    if game_status == GAME_FAIL:
        screen.blit(text_you_fail,(0,0))
    pygame.display.update()



game_status = GAME_CONTINUE
draw_screen(map_list, rat_pos_index, game_status)

# PYGAME DEAD LOOP FOR RECEIVING EVENTS
while continueFlag: # main game loop

    # EVENTS HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            continueFlag = False
            print('pygame exit!')
            break
        elif event.type == MOUSEBUTTONDOWN:
            if game_status != GAME_CONTINUE: continue

            x,y = event.pos
            x_index, y_index = gen_index_by_pos(x, y)
            rat_x_index, rat_y_index = rat_pos_index
            if (map_list[y_index][x_index] == CELL_GROUND):
                map_list[y_index][x_index] = CELL_BLOCK
                rat_path = mouse_opt_path(map_list, rat_pos_index)
                if len(rat_path) > 1:
                    map_list[rat_y_index][rat_x_index] = CELL_GROUND
                    instruction_x, instruction_y = rat_path[1]
                    map_list[instruction_y][instruction_x] = CELL_RAT
                    rat_pos_index = (instruction_x, instruction_y)
                    print('Rat path is ' + str(rat_path))
                    print('The map is ' + str(map_list))
                    game_status = GAME_CONTINUE
                elif len(rat_path) == 1:
                    print("rat win!")
                    game_status = GAME_FAIL
                elif len(rat_path) == 0:
                    print("you win!")
                    game_status = GAME_WIN
                refresh = True
            

    # PAINT THE SCREEN
    if refresh:
        draw_screen(map_list, rat_pos_index, game_status)
        refresh = False
        

    

pygame.display.quit()
pygame.quit()
