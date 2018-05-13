#!/usr/bin/env python
import pygame, sys
from pygame.locals import *
import sys
sys.path.append('../my_canvas/')
from my_color import *    

# CONSTANTS DEFINITION

# Configurations --begin--

EDGESIZE  = 10
BLOCKSIZE = 70
BLOCKS    = 3
SEGMENT   = BLOCKSIZE + EDGESIZE
SCREEN_WIDTH = EDGESIZE + SEGMENT*BLOCKS
SCREEN_HEIGHT = EDGESIZE + SEGMENT*BLOCKS
SCREEN_TITLE = 'MOS PYGAME CODING'
# Script --begin--

SCRIPT_ROOM = [[0,0,4],
               [0,5,2],
               [1,3,0]]
SCRIPT_EDGE = [[0,3],
               [0,5,2],
               [5,0],
               [0,0,5],
               [5,1]]
myposition = (1,1)



BLOCKSDICT       = {0: COLOR_WHITE, 1:COLOR_GREEN ,     2:COLOR_RED     , 3:COLOR_YELLOW,      4:COLOR_GRAY,       5: COLOR_OLIVE}
EDGESDICT        = {0: COLOR_LIGHT, 1:COLOR_LIGHTGREEN, 2:COLOR_LIGHTRED, 3:COLOR_LIGHTYELLOW, 4: COLOR_LIGHTGRAY, 5: COLOR_LIGHTOLIVE}

# Script --end--
# Game status --begin--
GAME_STATUS_WIN      = 1
GAME_STATUS_FAIL     = -1
GAME_STATUS_CONTINUE = 0

GAME_STATUS_DICT = {GAME_STATUS_CONTINUE: '', GAME_STATUS_WIN: 'You escaped!'}

# Game status    --end--
# Configurations --end--
# fixed         --begin--

# VARIABLES DEFINITION
continueFlag = True
refresh      = False
game_status  = GAME_STATUS_CONTINUE

# Functions definition


# PYGAME INITIALISATION
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
def gen_pos_by_index(x_index, y_index):
    x = EDGESIZE + SEGMENT * x_index
    y = EDGESIZE + SEGMENT * y_index
    return [x, y, BLOCKSIZE, BLOCKSIZE]

def gen_index_by_pos(x, y):
    x_index = int((x-EDGESIZE)/SEGMENT)
    y_index = int((y-EDGESIZE)/SEGMENT)
    return x_index, y_index


def writemap(screen, myposition):
    # drawing the blocks
    for y_index in range(BLOCKS):
        for x_index in range(BLOCKS):
            pygame.draw.rect(screen, BLOCKSDICT[SCRIPT_ROOM[y_index][x_index]], gen_pos_by_index(x_index, y_index))
    # drawing my position
    pygame.draw.rect(screen, COLOR_RED,gen_pos_by_index(myposition[0],myposition[1])[0:2] + [20,20])
    # drawing the edges in vertical
    for y in range(0,len(SCRIPT_EDGE),2):
        for x in range(BLOCKS - 1):
            pygame.draw.rect(screen, EDGESDICT[SCRIPT_EDGE[y][x]], [SEGMENT*(x+1), EDGESIZE + SEGMENT * y/2, EDGESIZE, BLOCKSIZE])
    # drawing the edges in horizontal
    for y in range(1, len(SCRIPT_EDGE), 2):
        for x in range(BLOCKS):
            pygame.draw.rect(screen, EDGESDICT[SCRIPT_EDGE[y][x]], [EDGESIZE + SEGMENT * x, int(SEGMENT * (y-1)/2 ) + SEGMENT, BLOCKSIZE, EDGESIZE])
            print([EDGESIZE + SEGMENT * x, int(SEGMENT * (y-1)/2 ) + SEGMENT, EDGESIZE])

def textdisplay(screen, text, fontsize, color, dest):
    font = pygame.font.SysFont('Comic Sans MS', fontsize)
    text = font.render(text, False, color)
    screen.blit(text, dest)

def screen_display(screen, myposition,game_status, gsd):
    writemap(screen, myposition)
    displaying = gsd.get(game_status, '')
    if displaying != '':
        textdisplay(screen, displaying, 30, COLOR_RED, (0,0))

# fixed --end--
screen_display(screen, myposition, game_status, GAME_STATUS_DICT)
#textdisplay(screen,'Text', 30, COLOR_GREEN,(0,0))
pygame.display.update()


# PYGAME DEAD LOOP FOR RECEIVING EVENTS
while continueFlag: # main game loop

    # EVENTS HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            continueFlag = False
            print('pygame exit!')
            break
        #elif event.type == MOUSEBUTTONDOWN

    # PAINT THE SCREEN

pygame.display.quit()
pygame.quit()