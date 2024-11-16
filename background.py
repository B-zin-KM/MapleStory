from pico2d import load_image
import pico2d


class Back:
    def __init__(self):
        self.image = load_image('전사의 성전.png')

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 800 / 2, 600 / 2)

    def update(self):
        pass