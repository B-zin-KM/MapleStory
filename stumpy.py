import random
import math
import game_world
import common
from pico2d import *


class Stumpy:

    def __init__(self, player):
        self.x, self.y = random.randint(990, 1300), 890
        self.image_R = load_image('스텀피R.png')
        self.image_L = load_image('스텀피L.png')
        self.frame = random.randint(0, 3)
        self.dir = random.choice([-1,1])
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
                self.frame = (self.frame + 1) % 6

            if self.x > 1300:
                self.dir = -1
            elif self.x < 990:
                self.dir = 1
            self.x = clamp(990, self.x, 1300)

            self.x += self.dir * 0.7


    def draw(self):
        if common.map == 0:
            if self.dir == 1:
                self.image_R.clip_draw(2510 + self.frame * 200, 1530, 200, 180, self.x - common.scroll_x, self.y - common.scroll_y)
            elif self.dir == -1:
                self.image_L.clip_draw(self.frame * 200, 1530, 200, 180, self.x - common.scroll_x, self.y - common.scroll_y)


    def get_bb(self):
        if common.map == 0:
            return 0, 0, 0, 0



    def handle_collision(self, group, other):
        pass