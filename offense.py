from pico2d import *
import game_world
import common


# class Offense0:
#     def __init__(self, x = 400, y = 300, dir = 1):
#         self.x, self.y, self.dir = x, y, dir
#         self.removed = False
#
#     def draw(self):
#         if common.box_on:
#             if self.dir == 1:
#                 draw_rectangle(self.x + 22 - common.scroll_x, self.y - 20 - common.scroll_y, self.x + 62 - common.scroll_x, self.y + 10 - common.scroll_y)
#             elif self.dir == -1:
#                 draw_rectangle(self.x - 43 - common.scroll_x, self.y - 20 - common.scroll_y, self.x - 3 - common.scroll_x, self.y + 10 - common.scroll_y)
#
#     def update(self):
#         pass
#
#     def get_bb(self):
#         if self.dir == 1:
#             return self.x + 22, self.y - 20, self.x + 62, self.y + 10
#         elif self.dir == -1:
#             return self.x - 43, self.y - 20, self.x - 3, self.y + 10
#
#     def handle_collision(self, group, other):
#         pass


class Offense0:
    def __init__(self, x = 400, y = 300, dir = 1):
        self.x, self.y, self.dir = x, y, dir
        self.image0 = load_image('파스0.png')
        self.image1 = load_image('파스1.png')
        self.image2 = load_image('파스2.png')
        self.image3 = load_image('파스3.png')
        self.image4 = load_image('파스4.png')
        self.image5 = load_image('파스5.png')
        # self.image6 = load_image('파스스윙.png')
        self.frame = 0
        self.count = 0

        self.idle_time = 0.1
        self.elapsed_time = 0.0
        self.last_time = get_time()


    def draw(self):

        if self.frame == 0:
            self.image0.clip_draw(0, 0, 164, 156, self.x - common.scroll_x, self.y - common.scroll_y)
        elif self.frame == 1:
            self.image1.clip_draw(0, 0, 164, 151, self.x - common.scroll_x, self.y - common.scroll_y)
        elif self.frame == 2:
            self.image2.clip_draw(0, 0, 162, 144, self.x - common.scroll_x, self.y - common.scroll_y)
        elif self.frame == 3:
            self.image3.clip_draw(0, 0, 143, 134, self.x - common.scroll_x, self.y - common.scroll_y)
        elif self.frame == 4:
            self.image4.clip_draw(0, 0, 118, 103, self.x - common.scroll_x, self.y - common.scroll_y)
        elif self.frame == 5:
            self.image5.clip_draw(0, 0, 73, 74, self.x - common.scroll_x, self.y - common.scroll_y)

        if common.box_on:
            if self.dir == 1:
                draw_rectangle(self.x + 22 - common.scroll_x, self.y - 20 - common.scroll_y, self.x + 62 - common.scroll_x, self.y + 10 - common.scroll_y)
            elif self.dir == -1:
                draw_rectangle(self.x - 43 - common.scroll_x, self.y - 20 - common.scroll_y, self.x - 3 - common.scroll_x, self.y + 10 - common.scroll_y)

    def update(self):
        self.count += 1

        current_time = get_time()
        time_difference = current_time - self.last_time
        self.last_time = current_time
        self.elapsed_time += time_difference

        if self.elapsed_time >= self.idle_time:
            self.elapsed_time = 0
            self.frame = (self.frame + 1) % 4

        self.frame = (self.frame + 1) % 6
        pass

    def get_bb(self):
        if self.count == 35:
            print('asd')
            if self.dir == 1:
                return self.x + 22, self.y - 20, self.x + 62, self.y + 10
            elif self.dir == -1:
                return self.x - 43, self.y - 20, self.x - 3, self.y + 10

    def handle_collision(self, group, other):
        pass