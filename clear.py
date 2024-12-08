from pico2d import *
import common

class Clear:
    def __init__(self):
        self.image = load_image('Clear.png')
        self.frame = 0
        self.idle_time = 0.2
        self.elapsed_time = 0.0
        self.last_time = get_time()

    def update(self):
        if common.clear:
            current_time = get_time()
            time_difference = current_time - self.last_time
            self.last_time = current_time
            self.elapsed_time += time_difference

            if self.elapsed_time >= self.idle_time:
                self.elapsed_time = 0
                self.frame = (self.frame + 1) % 3

    def draw(self):
        if common.clear:
            self.image.clip_draw(self.frame * 68, 0, 68, 56, 640, 400, 340, 280)