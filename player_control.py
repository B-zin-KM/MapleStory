from sys import platform

from pico2d import *
from background import Back, Platform
from player import Player
from bounding_box import Box
from npc import NPC
from talk_box import TalkBox
from ui import UI

import game_world


class Mouse:
    def __init__(self):
        self.x, self.y = 0, 0
        self.box_on = False

    def update(self):
        pass

    def handle_event(self, event):
        if event.type in (SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP):
            self.x, self.y = event.x, get_canvas_height() - event.y

    def get_bb(self):
        return self.x - 3, self.y - 3, self.x + 3, self.y + 3

    def draw(self):
        if self.box_on:
            draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        pass


def handle_events():
    global running
    global mouse
    global box
    global npc
    global talkbox
    global ui

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse.handle_event(event)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse.handle_event(event)
            if game_world.collide(mouse, npc):
                talkbox.count = 1
            if game_world.collide(mouse, talkbox):
                if talkbox.count == 1:
                    talkbox.count = 0
                    player.job = 1      # 전사 전직
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            if talkbox.count == 1:
                talkbox.count = 0
            else:
                running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
             mouse.box_on = not mouse.box_on
             box.box_on = not box.box_on
             npc.box_on = not npc.box_on
             talkbox.box_on = not talkbox.box_on
             Back.line_on = not Back.line_on
        else:
            player.handle_event(event)


def reset_world():
    global running
    global mouse
    global background
    global player
    global box
    global platforms
    global npc
    global talkbox
    global ui

    running = True

    background = Back()
    game_world.add_object(background, 0)

    player = Player()
    game_world.add_object(player, 1)

    talkbox = TalkBox()
    game_world.add_object(talkbox, 2)

    box = Box(player)
    game_world.add_object(box, 3)

    platforms = [Platform() for _ in range(8)]
    game_world.add_objects(platforms, 3)

    npc = NPC()
    game_world.add_object(npc, 3)

    ui = UI()
    game_world.add_object(ui, 3)

    mouse = Mouse()
    game_world.add_object(mouse, 3)

    game_world.add_collision_pair('player:platform', box, None)
    for platform in platforms:
        game_world.add_collision_pair('player:platform', None, platform)


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    print_location(player)
    update_canvas()


def print_location(obj):
    player_coordinates = f"player   state: {str(obj.state_machine.cur_state)}, x: {int(obj.x)}, y: {int(obj.y)}"
    sys.stdout.write("\r" + player_coordinates)
    sys.stdout.flush()


open_canvas(1280, 800)
reset_world()


while running:
    handle_events()
    update_world()
    render_world()

    delay(0.01)


close_canvas()