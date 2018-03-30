#!/usr/bin/env python
from tests import canvas
import pygame, sys
from pygame.locals import *

# CONSTANTS DEFINITION
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = 'MOS PYGAME CODING'

# VARIABLES DEFINITION
continueFlag = True

def painter(the_list):
    for y in range(0,len(the_list)):
        for x in range(len(the_list[y])):
            screen.set_at((x,y),the_list[y][x])

# PYGAME INITIALISATION
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)


# PYGAME DEAD LOOP FOR RECEIVING EVENTS
while continueFlag: # main game loop

    # EVENTS HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            continueFlag = False
            print('pygame exit!')
            break

    # PAINT THE SCREEN
    painter(canvas)

    screen.set_at((122,125),(255,255,255))
pygame.display.quit()
pygame.quit()