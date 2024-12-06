from pico2d import load_image, draw_rectangle, SDLK_F1
from player import Player
import game_world


class Inven:
    def __init__(self):
        self.image = load_image('inven.png')
        self.left, self.bottom, self.right, self.top = 588, 645, 805, 690
        self.inven_on = -1   # -1 off / 0 장비 / 1 소비 / 2 기타
        self.box_on = False

    def draw(self):
        if self.inven_on != -1:
            self.image.clip_draw(self.inven_on * 330, 0, 330, 547, 700, 500, 240, 400)
            if self.box_on:
                draw_rectangle(self.left, self.bottom, self.right, self.top)

    def update(self):
        pass

    def get_bb(self):
        if self.inven_on == -1:
            return 0, 0, 0, 0
        return self.left, self.bottom, self.right, self.top
        pass

    def handle_collision(self, group, other):
        pass