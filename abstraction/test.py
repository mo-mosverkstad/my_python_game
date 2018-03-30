from bases import base_pygame
import sys
sys.path.insert(0, '../my_canvas/')
from my_canvas_lib import*
from my_color import *

class example(base_pygame):
    def canvas_update(self):
        self.canvas.add(Block(0,0,100,100,(0,255,0)))
        

obj = example('My test', 400, 400, COLOR_GRAY)
obj.run()