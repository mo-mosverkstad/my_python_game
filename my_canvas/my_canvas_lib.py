class Block:
    def __init__(self, left, top, width, height, color):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color

    def is_in_scope(self, x, y):
        return (x >= self.left and x < self.left + self.width) and (y >= self.top and y < self.top + self.height)

class line:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.special = (x1 == x2)
        self.k = (y1-y2)/(x1-x2) if not self.special else 0
        self.b = (x1*y2-x2*y1)/(x1-x2) if not self.special else 0
        self.color = color

    def is_in_scope(self,x,y):
        if self.special:
            return x == self.x1 and y >= self.y1 and y < self.y2
        else:
            return int(x*self.k+self.b) == y and self.x1 <= x and x < self.x2


class Canvas:
    def __init__(self, width, height, color):
        self.form_list = []
        self.width = int(width)
        self.height = int(height)
        self.color = color

    def add(self, form):
        self.form_list.insert(0, form)
        return self

    def __get_color(self, x, y):
        for b in self.form_list:
            if b.is_in_scope(x, y): return b.color
        return self.color

    def __generate_canvas(self):
        canvas_display = []
        for y in range(self.height):
            canvas_row = []
            for x in range(self.width):
                canvas_row.append(self.__get_color(x, y))
            canvas_display.append(canvas_row)
        return canvas_display

    def draw(self, screen):
        canvas_display = self.__generate_canvas()
        for y in range(self.height):
            for x in range(self.width):
                screen.set_at((x, y), canvas_display[y][x])
