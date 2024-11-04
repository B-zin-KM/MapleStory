from pico2d import *
from background import Back
from player import Player


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            player.handle_event(event)
            pass


def reset_world():
    global running
    global background
    global world
    global player

    running = True
    world = []

    background = Back()
    world.append(background)

    player = Player()
    world.append(player)


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        print(player.state_machine.cur_state)
        print(player.air)
        print(player.x, player.y)
        o.draw()
    update_canvas()


open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()

    delay(0.01)

close_canvas()