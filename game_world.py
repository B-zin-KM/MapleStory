world = [[], [], []] # world[0]: background 객체들
                     # world[1]: foreground 객체들
                     # world[2]: boundingbox


def add_object(o, depth):
    world[depth].append(o)


def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print(f'CRITICAL: 존재하지않는 객체{o}를 지우려고 합니다.')