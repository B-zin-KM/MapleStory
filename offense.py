from pico2d import *
import game_world

scroll_x = 0
scroll_y = 0

class Offense0:
    image = None

    def __init__(self, x = 400, y = 300, dir = 1):
        # if Ball.image == None:
        #     Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.dir = x, y, dir
        self.removed = False
        self.box_on = False

    def draw(self):
        # self.image.draw(self.x, self.y)
        if self.dir == 1:
            draw_rectangle(self.x + 22 - scroll_x, self.y - 20 - scroll_y, self.x + 62 - scroll_x, self.y + 10 - scroll_y)
        elif self.dir == -1:
            draw_rectangle(self.x - 43 - scroll_x, self.y - 20 - scroll_y, self.x - 3 - scroll_x, self.y + 10 - scroll_y)

    def update(self):
        pass

    def get_bb(self):
        if self.dir == 1:
            return self.x + 22, self.y - 20, self.x + 62, self.y + 10
        elif self.dir == -1:
            return self.x - 43, self.y - 20, self.x - 3, self.y + 10

    def handle_collision(self, group, other):
        pass