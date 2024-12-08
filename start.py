from pico2d import *

class Start:
    def __init__(self):
        self.image = load_image('시작화면.PNG')
        self.bgm = load_music('시작화면.mp3')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()

    def __del__(self):
        self.bgm.stop()

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 1280, 799, 640, 400, 1280, 800)

    def get_bb(self):
        return 880, 160, 1060, 230
        pass