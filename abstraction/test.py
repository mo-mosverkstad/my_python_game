from bases import Base_pygame
import sys
sys.path.append('../my_canvas/')
from my_canvas_lib import*
from my_color import *

class Example(Base_pygame):
    def canvas_update(self):
        self.canvas.add(Block(0,0,100,100,(0,255,0)))
        
obj = Example('My test', 400, 400, COLOR_GRAY)
obj.run()