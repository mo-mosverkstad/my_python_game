class Stack:
  def __init__(self):
    self.__storage = []

  def isEmpty(self):
    return len(self.__storage) == 0

  def push(self, data):
    self.__storage.append(data)

  def pop(self):
    return self.__storage.pop()

import copy
MAP_MOUSE_TRACK = 100
MAP_GROUND = 0
MAP_BLOCK = 1
MAP_EDGE = -1

STEP_NONE  = ( 0,  0)
STEP_UP    = ( 0, -1)
STEP_RIGHT = (+1,  0)
STEP_DOWN  = ( 0, +1)
STEP_LEFT  = (-1,  0)

MAX_STEPS = 50

def is_valid(map_track, pos):
    x, y = pos
    return map_track[y][x] == MAP_GROUND

def is_edge(map_track, pos):
    x, y = pos
    return map_track[y][x] == MAP_EDGE

def is_tracked(map_track, pos):
    x, y = pos
    return map_track[y][x] == MAP_MOUSE_TRACK

def new_pos(pos, step):
    x, y = pos
    step_x, step_y = step
    return (x + step_x, y + step_y)

def map_mouse_track(map_track, pos):
    x, y = pos
    map_track[y][x] = MAP_MOUSE_TRACK

def print_path(path):
    path_string = 'One solution:'
    for item in path:
        last_step, last_pos = item
        path_string += str(last_pos) + ', '
    print(path_string)

def get_key(item): return item[0]

def look_for_path(solution_path, mouse_pos):
    possible_path = list()
    for path in solution_path:
        for i in range(len(path)):
            step, pos = path[i]
            if pos == mouse_pos:
                possible_path.append((len(path[i:]), path[i:]))
    if len(possible_path) == 0:
        return None
    else:
        length, path = list(sorted(possible_path, key=get_key))[0]
        return path

def sort_path(solution_path):
    new_path = [(len(path), path) for path in solution_path]
    return [path for length, path in list(sorted(new_path, key=get_key))]

def mouse_step_next(map_track, all_path_stack, solution_path, path, step):
    last_step, last_pos = path[-1]
    new_mouse_pos = new_pos(last_pos, step)
    if is_valid(map_track, new_mouse_pos):
        map_mouse_track(map_track, new_mouse_pos)
        path.append((step, new_mouse_pos))
        all_path_stack.push(path)
        mouse_step(map_track, all_path_stack, solution_path)
    elif is_tracked(map_track, new_mouse_pos):
        remaining_path = look_for_path(solution_path, new_mouse_pos)
        if remaining_path != None:
            solution_path.append(path + remaining_path)
    elif is_edge(map_track, new_mouse_pos):
        solution_path.append(path)

def mouse_step(map_track, all_path_stack, solution_path):
    if not all_path_stack.isEmpty():
        path = all_path_stack.pop()
        if len(path) < MAX_STEPS:
            mouse_step_next(map_track, all_path_stack, solution_path, copy.deepcopy(path), STEP_UP)
            mouse_step_next(map_track, all_path_stack, solution_path, copy.deepcopy(path), STEP_RIGHT)
            mouse_step_next(map_track, all_path_stack, solution_path, copy.deepcopy(path), STEP_DOWN)
            mouse_step_next(map_track, all_path_stack, solution_path, copy.deepcopy(path), STEP_LEFT)

def mouse_opt_path(map, mouse_pos):
    map_track = copy.deepcopy(map)
    map_mouse_track(map_track, mouse_pos)
    MAX_STEPS = len(map_track) + len(map_track[0])

    all_path_stack = Stack()
    
    path = list()
    path.append((STEP_NONE, mouse_pos))
    all_path_stack.push(path)

    solution_path = list()
    mouse_step(map_track, all_path_stack, solution_path)
    
    return [path for step, path in sort_path(solution_path)[0]]
    
    
map = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [-1,  0,  0,  0,  0,  0,  0,  0,  0, -1],
       [-1,  0,  0,  0,  1,  0,  1,  1,  1, -1],
       [-1,  0,  1,  0,  0,  0,  0,  0,  1, -1],
       [-1,  0,  0,  1,  0,  0,  0,  0,  1, -1],
       [-1,  0,  0,  0,  0,  0,  0,  0,  1, -1],
       [-1,  0,  0,  0,  0,  1,  1,  1,  1, -1],
       [-1,  0,  0,  0,  0,  0,  0,  0,  0, -1],
       [-1,  0,  0,  0,  0,  0,  0,  0,  0, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       ]

print(mouse_opt_path(map, (7, 5)))
