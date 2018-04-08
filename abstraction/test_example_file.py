#!/usr/bin/env python
import pygame, sys
from pygame.locals import *

# CONSTANTS DEFINITION
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = 'MOS PYGAME CODING'

# VARIABLES DEFINITION
continueFlag = True


# PYGAME INITIALISATION
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

pygame.draw.polygon(screen,(255,255,255),[(0,0),(12,12),(24,12),(50,20)])

# PYGAME DEAD LOOP FOR RECEIVING EVENTS
while continueFlag: # main game loop

    # EVENTS HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            continueFlag = False
            print('pygame exit!')
            break

    # PAINT THE SCREEN
    pygame.display.update()
pygame.display.quit()
pygame.quit()