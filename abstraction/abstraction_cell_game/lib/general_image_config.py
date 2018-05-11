#!/usr/bin/env python
import pygame
from pygame.locals import *
from lib.general_color_config import *

class Image_item:
    def __init__(self, image_file_name):
        self.img = pygame.image.load(image_file_name)
        self.img.set_colorkey(COLOR_WHITE, RLEACCEL)
        self.img_size = self.img.get_rect().size

    def get_image(self): return self.img