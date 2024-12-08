from pico2d import load_image, draw_rectangle, SDLK_F1
from player import Player
import game_world
import common


class TalkBox:
    def __init__(self):
        self.image = load_image('주먹펴고일어서대화_0.PNG')
        self.left, self.bottom, self.right, self.top = 875, 352, 920, 362
        self.count = 0

    def draw(self):
        if self.count == 1:
            self.image.clip_draw(0, 0, 995, 381, 1280 / 2, 800 / 2, 995*0.65, 381*0.65)
            if common.box_on:
                draw_rectangle(self.left, self.bottom, self.right, self.top)

    def update(self):
        pass

    def get_bb(self):
        return self.left, self.bottom, self.right, self.top
        pass

    def handle_collision(self, group, other):
        pass