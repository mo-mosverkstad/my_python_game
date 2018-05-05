from base_cell_game import Base_cell_game

from general_color_config import *
from general_cell_config import Cell_map
from general_game_config import Game_status
from general_image_config import Image_item

class Simple_cell_game (Base_cell_game):
    CELL_EDGE   = -1
    CELL_GROUND = 0
    CELL_BLOCK  = 1
    CELL_RAT    = 2
    CELL_COLOR_DICT = {CELL_GROUND : COLOR_LIGHTGREEN,
                       CELL_BLOCK  : Image_item('image_block.png'),
                       CELL_EDGE   : COLOR_YELLOW,
                       CELL_RAT    : Image_item('image_mouse.png')}

    def __init__(self, map):
        cell_map = Cell_map(30, 4, map, self.CELL_COLOR_DICT)
        Base_cell_game.__init__(self, "SIMPLE CELL GAME", cell_map)

    def on_mouse_down(self, map, pos, game_status):
            x,y = pos
            if map.get_cell_status(x, y) == self.CELL_GROUND:
                map.set_cell_status(x, y, self.CELL_BLOCK)
                return True
            elif map.get_cell_status(x, y) == self.CELL_BLOCK:
                game_status.set_status(Game_status.GAME_FAIL)
                return True
            elif map.get_cell_status(x, y) == self.CELL_RAT:
                game_status.set_status(Game_status.GAME_WIN)
                return True
            return False


map_0001 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1,  0,  0,  0,  2,  0,  0,  0,  0, -1],
            [-1,  0,  0,  0,  1,  0,  1,  1,  1, -1],
            [-1,  0,  1,  0,  0,  0,  0,  0,  1, -1],
            [-1,  0,  2,  1,  0,  0,  0,  2,  1, -1],
            [-1,  0,  0,  0,  0,  0,  0,  0,  1, -1],
            [-1,  0,  0,  0,  0,  1,  1,  1,  1, -1],
            [-1,  0,  0,  0,  0,  0,  0,  0,  0, -1],
            [-1,  0,  0,  0,  0,  0,  0,  0,  0, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           ]
        
Simple_cell_game(map_0001).run()