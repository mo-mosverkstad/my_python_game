#!/usr/bin/env python
import pygame
from pygame.locals import *

import sys
from general_color import *
from general_game_config import Game_status

class Base_cell_game:
    def __init__(self, scTitle, blocksize, edgesize, w_cells, h_cells, cell_dict, images, map_list):
        # CONSTANTS DEFINITION
        self.TITLE              = scTitle

        # CONFIGURATION OF SIZE
        self.IMAGES             = images

        # CONFIGURATION OF CELL STATUS
        self.CELLDICT           = cell_dict

        # CONFIGURATION OF GAME STATUS
        self.GAME_STATUS        = Game_status()

        # CONFIGURATIONS OF OTHER STUFFS
        self.MAP_LIST = map_list

    def font_writeout(self, display, text, color, textsize, dest):
        font = pygame.font.SysFont('Comic Sans MS', textsize)
        text = font.render(text, False, color)
        display.blit(text, dest)

    def img_load(self, images):
        img = []
        for item in images:
            img.append(pygame.image.load(item))
        return img_load

    def pos(self, pos_index):
        x = EDGE_SIZE + SEGMENT_SIZE * pos_index[0]
        y = EDGE_SIZE + SEGMENT_SIZE * pos_index[1]
        return (x, y)

    def index(self, position):
        x_index = int((position[0]-EDGE_SIZE)/SEGMENT_SIZE)
        y_index = int((position[1]-EDGE_SIZE)/SEGMENT_SIZE)
        return (x_index, y_index)

    def draw_map(self):
        for x_index in range(len(self.MAP_LIST[y_index])):
            cell_status = self.MAP_LIST[y_index][x_index]
            pygame.draw.rect(screen,
                             CELL_COLOR_DICT[cell_status],
                             self.pos(x_index, y_index), self.CELLSIZE, self.CELLSIZE)


    def run(self, game_status_pos):
        # VARIABLES DEFINITION
        continueFlag = True
        refresh = False

        # PYGAME INITIALISATION
        pygame.init()
        pygame.font.init()

        # PYGAME INITIALISATION
        pygame.init()
        pygame.font.init()

        # PYGAME BEGINNING
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.TITLE)

        # LOADING THESE IMAGES
        self.img_load(self.IMAGES)

        game_status.set_status(Game_status.GAME_CONTINUE)
