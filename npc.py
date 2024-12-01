from pico2d import draw_rectangle, SDLK_F1
from player import Player
import game_world


class NPC:
    def __init__(self):
        self.left, self.bottom, self.right, self.top = 76, 283, 120, 350
        self.box_on = False

    def draw(self):
        if self.box_on:
            draw_rectangle(self.left, self.bottom, self.right, self.top)

    def update(self):
        pass

    def get_bb(self):
        return self.left, self.bottom, self.right, self.bottom
        pass

    def handle_collision(self, group, other):
        if group == 'mouse:npc':
            print('asd')
        pass