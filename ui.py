from pico2d import load_image, draw_rectangle, SDLK_F1
from player import Player
import game_world


class UI:
    def __init__(self):
        self.image1 = load_image('statusUI.png')
        self.image2 = load_image('gauge.gray.png')
        self.image3 = load_image('gauge.graduation.png')
        self.left, self.bottom, self.right, self.top = 0, 0, 0, 0
        self.box_on = False

    def draw(self):
        self.image1.clip_draw(0, 0, 1280, 71, 1280 / 2, 71, 1280, 142)
        # self.image2.clip_draw(0, 0, 1, 16, 1280 / 2, 60, 1280, 120)
        self.image3.clip_draw(0, 0, 340, 31, 618, 39, 544, 62)
        if self.box_on:
            draw_rectangle(self.left, self.bottom, self.right, self.top)

    def update(self):
        pass

    def get_bb(self):
        return self.left, self.bottom, self.right, self.top
        pass

    def handle_collision(self, group, other):
        pass