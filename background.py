from pico2d import load_image, draw_rectangle, load_music

import common
import offense
from common import coordinates_list
from player import Player
from bounding_box import Box

class Back:
    def __init__(self, player):
        self.image0 = load_image('페리온 북쪽령.png')
        self.image1 = load_image('전사의 성전.png')

        self.bgm = load_music('bgm1.mp3')
        self.bgm.set_volume(50)

        self.player = player
        self.scroll_x = 0
        self.scroll_y = 0

        self.map_width = 2073
        self.map_height = 1610
        self.canvas_width = 1280
        self.canvas_height = 800

    def update(self):
        if common.map == 0:
            self.map_width = 2073
            self.map_height = 1610
        elif common.map == 1:
            self.map_width = 1280
            self.map_height = 800
        half_width = self.canvas_width // 2
        half_height = self.canvas_height // 2
        self.scroll_x = max(0, min(self.player.x - half_width, self.map_width - self.canvas_width))
        self.scroll_y = max(0, min(self.player.y - half_height, self.map_height - self.canvas_height))
        self.player.screen_x = self.player.x - self.scroll_x
        self.player.screen_y = self.player.y - self.scroll_y

        common.scroll_x = self.scroll_x
        common.scroll_y = self.scroll_y

    def draw(self):
        if common.map == 0:
            self.image0.clip_draw(
                int(self.scroll_x), int(self.scroll_y), self.canvas_width, self.canvas_height,
                self.canvas_width // 2, self.canvas_height // 2
            )
        elif common.map == 1:
            self.image1.clip_draw(
                int(self.scroll_x), int(self.scroll_y), self.canvas_width, self.canvas_height,
                self.canvas_width // 2, self.canvas_height // 2
            )

    def get_scroll(self):
        """스크롤 값 반환"""
        return self.scroll_x, self.scroll_y


class Platform0:
    instance_count = 0

    def __init__(self, back):
        self.back = back
        if Platform0.instance_count < len(coordinates_list[0]):
            self.left, self.bottom, self.right, self.top = coordinates_list[0][Platform0.instance_count]
        else:
            self.left, self.bottom, self.right, self.top = 0, 0, 0, 0
        Platform0.instance_count += 1

    def draw(self):
        scroll_x, scroll_y = self.back.get_scroll()
        if common.map == 0:
            if common.box_on:
                draw_rectangle(
                    self.left - scroll_x,
                    self.bottom - scroll_y,
                    self.right - scroll_x,
                    self.top - scroll_y
                )
        pass

    def update(self):
        pass

    def get_bb(self):
        scroll_x, scroll_y = self.back.get_scroll()
        return (
            self.left - scroll_x,
            self.bottom - scroll_y,
            self.right - scroll_x,
            self.top - scroll_y
        )

    def handle_collision(self, group, other):
        pass

class Platform1:
    instance_count = 0

    def __init__(self, back):
        self.back = back
        if Platform1.instance_count < len(coordinates_list[1]):
            self.left, self.bottom, self.right, self.top = coordinates_list[1][Platform1.instance_count]
        else:
            self.left, self.bottom, self.right, self.top = 0, 0, 0, 0
        Platform1.instance_count += 1

    def draw(self):
        scroll_x, scroll_y = self.back.get_scroll()
        if common.map == 1:
            if common.box_on:
                draw_rectangle(
                    self.left - scroll_x,
                    self.bottom - scroll_y,
                    self.right - scroll_x,
                    self.top - scroll_y
                )
        pass

    def update(self):
        pass

    def get_bb(self):
        scroll_x, scroll_y = self.back.get_scroll()
        return (
            self.left - scroll_x,
            self.bottom - scroll_y,
            self.right - scroll_x,
            self.top - scroll_y
        )

    def handle_collision(self, group, other):
        pass