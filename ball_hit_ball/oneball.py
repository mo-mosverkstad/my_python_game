#!/usr/bin/env python
import pygame, sys
from pygame.locals import *
from time import sleep

# CONSTANTS DEFINITION
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = 'MOS PYGAME CODING'

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255, 255, 255)

TIMER_SLEEP = 0.02
MOVE_STEP = 1

# VARIABLES DEFINITION
continueFlag = True
move_up = False
move_dn = False
move_lt = False
move_rt = False
x = 0
y = 0
ball_x = int(SCREEN_WIDTH/2)
ball_y = int(SCREEN_HEIGHT/2)

# PYGAME INITIALISATION
pygame.init()
ball_image = pygame.image.load('ball.png')
ball_image_size = ball_image.get_rect().size
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
        elif event.type == KEYDOWN:
            if event.key in (K_UP,K_w):
                move_up = True
                move_dn = False
            elif event.key in (K_DOWN,K_s):
                move_up = False
                move_dn = True
            elif event.key in (K_LEFT,K_a):
                move_lt = True
                move_rt = False
            elif event.key in (K_RIGHT,K_d):
                move_lt = False
                move_rt = True
        elif event.type == KEYUP:
            if event.key in (K_UP,K_w):
                move_up = False
            elif event.key in (K_DOWN,K_s):
                move_dn = False
            elif event.key in (K_LEFT,K_a):
                move_lt = False
            elif event.key in (K_RIGHT,K_d):
                move_rt = False

    # UPDATE THE BALL POSITION
    if move_up:
        ball_y = ball_y - MOVE_STEP
        if ball_y < 0: ball_y = 0
    elif move_dn:
        ball_y = ball_y + MOVE_STEP
        if ball_y > SCREEN_HEIGHT-ball_image_size[1]: ball_y = SCREEN_HEIGHT-ball_image_size[1]
    elif move_lt:
        ball_x = ball_x - MOVE_STEP
        ball_x = 0 if ball_x < 0 else ball_x
    elif move_rt:
        ball_x = ball_x + MOVE_STEP
        ball_x = SCREEN_WIDTH-ball_image_size[0] if ball_x > SCREEN_WIDTH-ball_image_size[0] else ball_x

    #print(pygame.mouse.get_pos())
    # PAINT THE SCREEN
    screen.fill(COLOR_WHITE)
    screen.blit(ball_image,(ball_x,ball_y))
    sleep(TIMER_SLEEP)
    pygame.display.update()

pygame.display.quit()
pygame.quit()