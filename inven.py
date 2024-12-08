from pico2d import load_image, draw_rectangle, SDLK_F1
from player import Player
import game_world
import common


class Inven:
    def __init__(self):
        self.image = load_image('inven.png')
        self.image1 = load_image('검.png')
        self.left, self.bottom, self.right, self.top = 588, 645, 805, 690
        self.inven_on = -1   # -1 off / 0 장비 / 1 소비 / 2 기타
        self.sword = 0
        self.box_on = False

    def draw(self):
        if self.inven_on != -1:
            self.image.clip_draw(self.inven_on * 330, 0, 330, 547, 700, 500, 240, 400)
            if self.inven_on == 0 and self.sword == 1:
                self.image1.clip_draw(0, 0, 31, 30, 615, 608)
            if common.box_on:
                draw_rectangle(self.left, self.bottom, self.right, self.top)

    def update(self):
        if self.inven_on == -1:
            self.left, self.bottom, self.right, self.top = 0, 0, 0, 0
        elif self.sword == 1:
            self.left, self.bottom, self.right, self.top = 588, 590, 805, 690
        else:
            self.left, self.bottom, self.right, self.top = 588, 645, 805, 690
        pass

    def get_bb(self):
        return self.left, self.bottom, self.right, self.top

    def handle_collision(self, group, other):
        pass