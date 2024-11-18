from pico2d import load_image, draw_rectangle


class Back:
    line_on = False

    def __init__(self):
        self.image = load_image('전사의 성전.png')

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 800 / 2, 600 / 2)

    def update(self):
        pass


coordinates = [
    (20, 102, 780, 102),
    (610, 177, 685, 177),
    (590, 155, 670, 155),
    (570, 134, 670, 134),
    (145, 150, 210, 150),
    (120, 175, 190, 175),
    (90, 205, 175, 205),
    (70, 283, 155, 283)
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
        pass

    def handle_collision(self, group, other):
        pass