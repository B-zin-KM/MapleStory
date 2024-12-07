from pico2d import *
import game_world

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
        draw_rectangle(*self.get_bb())

    def update(self):
        # if self.x < 25 or self.x > 1600 - 25:
        #     game_world.remove_object(self)
        pass

    def get_bb(self):
        if self.dir == 1:
            return self.x + 22, self.y - 20, self.x + 62, self.y + 10
        elif self.dir == -1:
            return self.x - 43, self.y - 20, self.x - 3, self.y + 10

    def handle_collision(self, group, other):
        pass