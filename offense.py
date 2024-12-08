from pico2d import *
import game_world
import common


class Offense0:
    image = None

    def __init__(self, x = 400, y = 300, dir = 1):
        self.x, self.y, self.dir = x, y, dir
        self.removed = False

    def draw(self):
        if common.box_on:
            if self.dir == 1:
                draw_rectangle(self.x + 22 - common.scroll_x, self.y - 20 - common.scroll_y, self.x + 62 - common.scroll_x, self.y + 10 - common.scroll_y)
            elif self.dir == -1:
                draw_rectangle(self.x - 43 - common.scroll_x, self.y - 20 - common.scroll_y, self.x - 3 - common.scroll_x, self.y + 10 - common.scroll_y)

    def update(self):
        pass

    def get_bb(self):
        if self.dir == 1:
            return self.x + 22, self.y - 20, self.x + 62, self.y + 10
        elif self.dir == -1:
            return self.x - 43, self.y - 20, self.x - 3, self.y + 10

    def handle_collision(self, group, other):
        pass