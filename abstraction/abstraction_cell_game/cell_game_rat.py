from lib.base_cell_game import Base_cell_game
from lib.general_color_config import *
from lib.general_cell_config import Cell_map
from lib.general_game_config import Game_status
from lib.general_image_config import Image_item

from rat_path import mouse_opt_path
from rat_map import rat_map_dict

class rat_game(Base_cell_game):
    CELL_EDGE   = -1
    CELL_GROUND = 0
    CELL_BLOCK  = 1
    CELL_RAT    = 2
    CELL_COLOR_DICT = {CELL_GROUND : COLOR_LIGHTGREEN,
                       CELL_BLOCK  : Image_item('res\image_block.png'),
                       CELL_EDGE   : COLOR_YELLOW,
                       CELL_RAT    : Image_item('res\image_mouse.png')}
    def __init__(self, rat_map_dict):
        self.rat_pos_index, self.map = rat_map_dict["#0001"]
        self.cell_map = Cell_map(30, 4, self.map, self.CELL_COLOR_DICT)
        Base_cell_game.__init__(self, "The_rat_game", self.cell_map)

    def on_mouse_down(self, map, pos, game_status):
        x_index, y_index = pos
        rat_x_index, rat_y_index = self.rat_pos_index
        map_list = self.cell_map.get_map_list()
        if (map_list[y_index][x_index].get_status() == self.CELL_GROUND):
            map_list[y_index][x_index].set_status(self.CELL_BLOCK)
            rat_path = mouse_opt_path(map_list, self.rat_pos_index)
            if len(rat_path) > 1:
                map_list[rat_y_index][rat_x_index].set_status(self.CELL_GROUND)
                instruction_x, instruction_y = rat_path[1]
                map_list[instruction_y][instruction_x].set_status(self.CELL_RAT)
                self.rat_pos_index = (instruction_x, instruction_y)
                game_status.set_status(Game_status.GAME_CONTINUE)
                return True
            elif len(rat_path) == 1:
                game_status.set_status(Game_status.GAME_FAIL)
                return True
            elif len(rat_path) == 0:
                game_status.set_status(Game_status.GAME_WIN)
                return True
        else:
            return False

rat_game(rat_map_dict).run()