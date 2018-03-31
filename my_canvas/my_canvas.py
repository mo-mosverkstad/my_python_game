#!/usr/bin/env python
import pygame, sys
from pygame.locals import *
from my_canvas_lib import *
from my_color import *

# CONSTANTS DEFINITION
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = 'MOS PYGAME CODING'

# VARIABLES DEFINITION
continueFlag = True
canvasFlag = False
x = 0
y = 0

# PYGAME INITIALISATION
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

canvas = Canvas(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, COLOR_GRAY)
'''
canvas.add(Block(15, 30, 90, 20, COLOR_YELLOW))
canvas.add(Block(10, 20, 60, 40, COLOR_RED))
'''
canvas.add(Block(54, 44, 100, 100, COLOR_YELLOW))
canvas.add(Block(94, 5, 12, 38, COLOR_RED))
canvas.add(line(94, 50, 94, 100, COLOR_BLUE))

# INIT THE SCREEN
screen.fill(COLOR_BLACK)
canvas.draw(screen)
pygame.display.update()


# PYGAME DEAD LOOP FOR RECEIVING EVENTS
while continueFlag: # main game loop

    # EVENTS HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueFlag = False
            print('pygame exit')
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]

    # PAINT THE SCREEN
    if canvasFlag:
        screen.fill(COLOR_BLACK)
        canvas.draw(screen)
        pygame.display.update()
        canvasFlag = False

pygame.display.quit()
pygame.quit()