from pico2d import load_image, draw_rectangle, SDLK_F1

from player import Player
import game_world
import common


class UI:
    def __init__(self):
        self.image1 = load_image('statusUI.png')
        self.image2 = load_image('gauge.gray.png')
        self.image3 = load_image('gauge.graduation.png')
        self.image4 = load_image('Lv.png')
        self.left, self.bottom, self.right, self.top = 1035, 73, 1185, 89
        self.player = Player()
        self.HPgauge = 0        #min 168
        self.MPgauge = 0        #min 168
        self.EXPgauge = 184     #min 184

    def draw(self):
        self.image1.clip_draw(0, 0, 1280, 71, 1280 / 2, 54, 1280, 108)
        self.image2.clip_draw_to_origin(0, 0, 1, 16, int(517 - self.HPgauge), 8, int(self.HPgauge), 21)     #HP
        self.image2.clip_draw_to_origin(0, 0, 1, 16, int(690 - self.MPgauge), 8, int(self.MPgauge), 21)     #MP
        self.image2.clip_draw_to_origin(0, 0, 1, 16, int(886 - self.EXPgauge), 8, int(self.EXPgauge), 21)   #EXP
        self.image3.clip_draw(0, 0, 340, 31, 617, 30, 544, 48)
        self.image4.clip_draw(11 * self.player.level_1, 0, 11, 13, 97, 27, 17, 20)
        if self.player.level_10 == 0:
            self.image4.clip_draw(110, 0, 11, 13, 78, 27, 17, 20)
        else:
            self.image4.clip_draw(11 * self.player.level_10, 0, 11, 13, 78, 27, 17, 20)
        if common.box_on:
            draw_rectangle(self.left, self.bottom, self.right, self.top)

    def update(self):
        self.HPgauge = self.player.HP
        self.MPgauge = self.player.MP
        self.EXPgauge = self.player.EXP
        pass

    def get_bb(self):
        return self.left, self.bottom, self.right, self.top
        pass

    def handle_collision(self, group, other):
        pass