import random
import math
import game_world
import common
from pico2d import *


class Stump:

    def __init__(self, player):
        self.x, self.y = random.randint(600, 1200), 217
        self.image_R = load_image('스텀프r.png')
        self.image_L = load_image('스텀프l.png')
        self.frame = random.randint(0, 3)
        self.dir = random.choice([-1,1])
        self.HP = 30
        self.idle_time = 0.3
        self.elapsed_time = 0.0
        self.last_time = get_time()
        self.player = player


    def update(self):
        if common.map == 0:
            current_time = get_time()
            time_difference = current_time - self.last_time
            self.last_time = current_time
            self.elapsed_time += time_difference

            if self.elapsed_time >= self.idle_time:
                self.elapsed_time = 0
                self.frame = (self.frame + 1) % 4

            if self.x > 1400:
                self.dir = -1
            elif self.x < 580:
                self.dir = 1
            self.x = clamp(580, self.x, 1400)

            self.x += self.dir * 0.7


    def draw(self):
        if common.map == 0:
            if self.dir == 1:
                self.image_R.clip_draw(self.frame * 73, 218, 72, 55, self.x - common.scroll_x, self.y - common.scroll_y)
            elif self.dir == -1:
                self.image_L.clip_draw(self.frame * 72, 218, 72, 55, self.x - common.scroll_x, self.y - common.scroll_y)
            if common.box_on:
                draw_rectangle(self.x - 37 - common.scroll_x, self.y - 27 - common.scroll_y, self.x + 37 - common.scroll_x, self.y + 30 - common.scroll_y)


    def get_bb(self):
        if common.map == 1:
            return 0, 0, 0, 0
        elif common.map == 0:
            return  self.x - 37, self.y - 27, self.x + 37, self.y + 30


    def handle_collision(self, group, other):
        if group == 'offense:stump':
            if not hasattr(other, 'handled'):  # 중복 처리 방지
                self.HP -= common.attack_power
                if self.player.x < self.x:
                    self.dir = -1
                    self.x += 15
                else:
                    self.dir = 1
                    self.x -= 15
                if self.HP <= 0:
                    game_world.remove_object(self)
                    other.handled = True
                    self.player.EXP -= 50 // self.player.Lv
                    if self.player.EXP <= 0:
                        self.player.Lv += 1
                        common.attack_power += 1
                        self.player.level_10 = self.player.Lv // 10
                        self.player.level_1 = self.player.Lv % 10
                        self.player.EXP = 184
                        self.player.HP = 0
                        self.player.MP = 0