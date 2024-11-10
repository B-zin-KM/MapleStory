from pico2d import draw_rectangle, SDLK_F1
import game_world


class Box:
    def __init__(self, player):
        self.player = player
        self.x = player.x
        self.y = player.y
        self.left, self.bottom, self.right, self.top = 0, 0, 0, 0
        self.box_on = True

    def draw(self):
        if self.box_on:
            draw_rectangle(self.left, self.bottom, self.right, self.top)

    def update(self):
        if self.player.air:
            if self.player.dir == -1:
                self.left = self.player.x - 59 // 2 + 20
                self.bottom = self.player.y - 66 // 2 + 1
                self.right = self.player.x + 59 // 2 - 2
                self.top = self.player.y + 70 // 2
            else:
                self.left = self.player.x - 59 // 2 + 21
                self.bottom = self.player.y - 66 // 2 + 1
                self.right = self.player.x + 59 // 2 - 1
                self.top = self.player.y + 70 // 2
        elif not self.player.air:
            if self.player.action == 7:
                self.left = self.player.x - 78 // 2 + 26
                self.bottom = self.player.y - 39 // 2 - 14
                self.right = self.player.x + 78 // 2 + 18
                self.top = self.player.y + 39 // 2 - 12
            elif self.player.action == 8:
                self.left = self.player.x - 78 // 2
                self.bottom = self.player.y - 39 // 2 - 14
                self.right = self.player.x + 78 // 2 - 8
                self.top = self.player.y + 39 // 2 - 12
            else:
                if self.player.dir == -1:
                    self.left = self.player.x - 59 // 2 + 26
                    self.bottom = self.player.y - 66 // 2
                    self.right = self.player.x + 59 // 2 - 11
                    self.top = self.player.y + 70 // 2
                else:
                    self.left = self.player.x - 59 // 2 + 30
                    self.bottom = self.player.y - 66 // 2
                    self.right = self.player.x + 59 // 2 - 7
                    self.top = self.player.y + 70 // 2