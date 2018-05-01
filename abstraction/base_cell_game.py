#!/usr/bin/env python
import pygame, sys
from pygame.locals import *

from general_color import *
from general_cell_config import Cell_map
from general_game_config import Game_status, Game_text

class Base_cell_game:
    def __init__(self, title, cell_map):
        self.screen_title = title
        self.continueFlag = True
        self.refresh = bool() # default value is False
        self.cell_map = cell_map
        self.screen_width, self.screen_height = self.cell_map.get_screen_size()
        self.game_status = Game_status()

        self.screen, self.text_you_win, self.text_you_fail = self.__pygame_init()
        self.__draw_screen()

    def __pygame_init(self):
        # PYGAME INITIALISATION
        pygame.init()
        pygame.font.init()
        
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.screen_title)
        
        font_comicSans = pygame.font.SysFont('Comic Sans MS', 30)
        text_you_win   = Game_text(screen, font_comicSans, "YOU WIN !!!", COLOR_RED, (0, 0))
        text_you_fail  = Game_text(screen, font_comicSans, "YOU FAIL!!!", COLOR_RED, (0, 0))
        
        return screen, text_you_win, text_you_fail

    def __draw_map(self):
        for row in self.cell_map.get_map_list():
            for item in row:
                pygame.draw.rect(self.screen, item.get_color(), item.get_pos())

    def __draw_screen(self):
        self.__draw_map()
        if   self.game_status.get_status() == Game_status.GAME_WIN:  self.text_you_win.draw()
        elif self.game_status.get_status() == Game_status.GAME_FAIL: self.text_you_fail.draw()
        pygame.display.update()

    ### customerized game code -- begin
    def on_mouse_down(self, map, pos, game_status):
        return False
    ### customerized game code -- end


    def run(self):
        # PYGAME DEAD LOOP FOR RECEIVING EVENTS
        while self.continueFlag: # main game loop
        
            # EVENTS HANDLING
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.continueFlag = False
                    print('pygame exit!')
                    break
                elif event.type == MOUSEBUTTONDOWN:
                    if self.game_status.get_status() != Game_status.GAME_CONTINUE: continue
                    self.refresh = self.on_mouse_down(self.cell_map, event.pos, self.game_status)
        
            # PAINT THE SCREEN
            if self.refresh:
                self.__draw_screen()
                self.refresh = False
        
        pygame.display.quit()
        pygame.quit()