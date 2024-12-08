from pico2d import draw_rectangle, SDLK_F1
from player import Player
from background import Back
import game_world
import common


class NPC:
    def __init__(self):
        self.left, self.bottom, self.right, self.top = 0, 0, 0, 0

    def draw(self):
        if common.box_on:
            draw_rectangle(self.left, self.bottom, self.right, self.top)

    def update(self):
        if common.map == 0:
            self.left, self.bottom, self.right, self.top = 0, 0, 0, 0
        elif common.map == 1:
            self.left, self.bottom, self.right, self.top = 320, 383, 350, 445
        pass

    def get_bb(self):
        return self.left, self.bottom, self.right, self.top
        pass

    def handle_collision(self, group, other):
        pass