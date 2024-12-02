from pico2d import load_image, draw_rectangle


class Back:
    line_on = False

    def __init__(self):
        self.image = load_image('전사의 성전.png')

    def draw(self):
        self.image.clip_draw(0, 0, 1280, 800, 1280 / 2, 800 / 2) #+240 +100

    def update(self):
        pass


coordinates = [
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