from pico2d import load_image, draw_rectangle
from common import coordinates
from player import Player

class Back:
    line_on = False
    loc = 0

    def __init__(self, player):
        self.image0 = load_image('페리온 북쪽령.png')
        self.image1 = load_image('전사의 성전.png')
        self.player = player
        self.scroll_x = 0
        self.scroll_y = 0

        # 맵 크기 및 캔버스 크기 설정
        self.map_width = 2763
        self.map_height = 1610
        self.canvas_width = 1280
        self.canvas_height = 800

    def update(self):
        """배경 스크롤 계산 및 플레이어 화면 내 위치 갱신"""
        half_width = self.canvas_width // 2
        half_height = self.canvas_height // 2

        # 스크롤링 계산
        self.scroll_x = max(0, min(self.player.x - half_width, self.map_width - self.canvas_width))
        self.scroll_y = max(0, min(self.player.y - half_height, self.map_height - self.canvas_height))

        # 플레이어 화면 내 위치 계산
        if self.scroll_x == 0:  # 맵 왼쪽 끝
            self.player.screen_x = self.player.x
        elif self.scroll_x == self.map_width - self.canvas_width:  # 맵 오른쪽 끝
            self.player.screen_x = self.player.x - self.scroll_x
        else:
            self.player.screen_x = half_width  # 화면 중앙

        if self.scroll_y == 0:  # 맵 아래쪽 끝
            self.player.screen_y = self.player.y
        elif self.scroll_y == self.map_height - self.canvas_height:  # 맵 위쪽 끝
            self.player.screen_y = self.player.y - self.scroll_y
        else:
            self.player.screen_y = half_height  # 화면 중앙

    def draw(self):
        if Back.loc == 0:
            self.image0.clip_draw(
                int(self.scroll_x), int(self.scroll_y), self.canvas_width, self.canvas_height,
                self.canvas_width // 2, self.canvas_height // 2
            )
        elif Back.loc == 1:
            self.image1.clip_draw(0, 0, 1280, 800, 1280 / 2, 800 / 2)


if Back.loc == 0:
    coordinates[:] = [
        (10, 190, 2063, 190),
    ]
elif Back.loc == 1:
    coordinates[:] = [
        (260, 202, 1020, 202),
        (850, 277, 925, 277),
        (830, 255, 910, 255),
        (810, 234, 910, 234),
        (385, 250, 450, 250),
        (360, 275, 430, 275),
        (330, 305, 415, 305),
        (310, 383, 395, 383)
    ]

class Platform:
    instance_count = 0

    def __init__(self):
        if Platform.instance_count < len(coordinates):
            self.left, self.bottom, self.right, self.top = coordinates[Platform.instance_count]
        else:
            self.left, self.bottom, self.right, self.top = 0, 0, 0, 0
        Platform.instance_count += 1
        pass

    def draw(self):
        if Back.line_on:
            draw_rectangle(self.left, self.bottom, self.right, self.top)
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.left, self.bottom, self.right, self.top

    def handle_collision(self, group, other):
        pass