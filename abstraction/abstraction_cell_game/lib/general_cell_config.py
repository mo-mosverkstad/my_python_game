class Cell_item:
    def __init__(self, status, color_dict, pos):
        self.status = status
        self.COLOR_DICT = color_dict
        self.pos = pos

    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_color(self): return self.COLOR_DICT[self.status]
    def get_pos(self): return self.pos

class Cell_map:
    def __init__(self, blockSize, edgeSize, map_list, color_dict):
        self.CELL_SIZE     = blockSize
        self.EDGE_SIZE     = edgeSize
        self.CELLS_HEIGHT  = len(map_list)
        self.CELLS_WIDTH   = len(map_list[0]) if self.CELLS_HEIGHT > 0 else 0
        self.SEGMENT_SIZE  = self.EDGE_SIZE + self.CELL_SIZE
        self.SCREEN_WIDTH  = self.EDGE_SIZE + self.SEGMENT_SIZE * self.CELLS_WIDTH
        self.SCREEN_HEIGHT = self.EDGE_SIZE + self.SEGMENT_SIZE * self.CELLS_HEIGHT
        self.map_list      = self.generate_map_list(map_list, color_dict)
        
    def generate_map_list(self, map_list, color_dict):
        new_map_list = list()
        for y_index in range(len(map_list)):
            new_map_list.append(list())
            for x_index in range(len(map_list[y_index])):
                new_map_list[y_index].append(
                    Cell_item(map_list[y_index][x_index], color_dict,
                              self.__gen_pos_by_index(x_index, y_index)))
        return new_map_list

    def __gen_pos_by_index(self, x_index, y_index):
        x = self.EDGE_SIZE + self.SEGMENT_SIZE * x_index
        y = self.EDGE_SIZE + self.SEGMENT_SIZE * y_index
        return [x, y, self.CELL_SIZE, self.CELL_SIZE]

    def get_map_list(self): return self.map_list

    def get_screen_size(self): return self.SCREEN_WIDTH, self.SCREEN_HEIGHT

    def get_index(self, x, y): return self.__gen_index_by_pos(x, y)

    def __gen_index_by_pos(self, x, y):
        x_index = int((x - self.EDGE_SIZE) / self.SEGMENT_SIZE)
        y_index = int((y - self.EDGE_SIZE) / self.SEGMENT_SIZE)
        return x_index, y_index

    def set_cell_status(self, x, y, status):
        self.map_list[y][x].set_status(status)

    def get_cell_status(self, x, y):
        return self.map_list[y][x].get_status()