from pico2d import draw_rectangle, SDLK_F1
import game_world
import common


class Box:

    def __init__(self, player):
        self.player = player
        self.left, self.bottom, self.right, self.top = 0, 0, 0, 0
        self.LEFT, self.BOTTOM, self.RIGHT, self.TOP = 0, 0, 0, 0

    def draw(self):
        if common.box_on:
            draw_rectangle(self.left,
                           self.bottom + self.player.velocity,
                           self.right,
                           self.bottom + 1)

    def update(self):
        if self.player.air:
            if self.player.dir == -1:
                self.left = self.player.screen_x - 59 // 2 + 20
                self.bottom = self.player.screen_y - 66 // 2 + 1
                self.right = self.player.screen_x + 59 // 2 - 2
                self.top = self.player.screen_y + 70 // 2
            else:
                self.left = self.player.screen_x - 59 // 2 + 21
                self.bottom = self.player.screen_y - 66 // 2 + 1
                self.right = self.player.screen_x + 59 // 2 - 1
                self.top = self.player.screen_y + 70 // 2
        elif not self.player.air:
            if self.player.action == 7:
                self.left = self.player.screen_x - 78 // 2 + 40
                self.bottom = self.player.screen_y - 39 // 2 - 14
                self.right = self.player.screen_x + 78 // 2 + 18
                self.top = self.player.screen_y + 39 // 2 - 14
            elif self.player.action == 8:
                self.left = self.player.screen_x - 78 // 2
                self.bottom = self.player.screen_y - 39 // 2 - 14
                self.right = self.player.screen_x + 78 // 2 - 21
                self.top = self.player.screen_y + 39 // 2 - 14
            else:
                if self.player.dir == -1:
                    self.left = self.player.screen_x - 59 // 2 + 26
                    self.bottom = self.player.screen_y - 66 // 2
                    self.right = self.player.screen_x + 59 // 2 - 11
                    self.top = self.player.screen_y + 70 // 2 - 2
                else:
                    self.left = self.player.screen_x - 59 // 2 + 30
                    self.bottom = self.player.screen_y - 66 // 2
                    self.right = self.player.screen_x + 59 // 2 - 7
                    self.top = self.player.screen_y + 70 // 2 - 2


    def get_bb(self):
        return self.left, self.bottom + self.player.velocity, self.right, self.bottom + 1
        pass

    def handle_collision(self, group, other):

        if common.map == 0:
            if group == 'player:platform0':
                self.player.air = False
                self.player.velocity = 0
                _, _, _, top = other.get_bb()
                adjusted_top = top + common.scroll_y
                self.player.y = adjusted_top + 33

        elif common.map == 1:
            if group == 'player:platform1':
                self.player.air = False
                self.player.velocity = 0
                _, _, _, top = other.get_bb()
                adjusted_top = top + common.scroll_y
                self.player.y = adjusted_top + 33