from pico2d import *
from background import Back, Platform0, Platform1
from player import Player
from bounding_box import Box
from npc import NPC
from talk_box import TalkBox
from ui import UI
from inven import Inven
from common import coordinates_list
from stump import Stump

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
    global inven

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
            if game_world.collide(mouse, inven):
                if mouse.x < 632 and 645 < mouse.y:
                    inven.inven_on = 0
                elif mouse.x < 676 and 645 < mouse.y:
                    inven.inven_on = 1
                elif 726 < mouse.x < 770 and 645 < mouse.y:
                    inven.inven_on = 2
                elif 795 < mouse.x and 678 < mouse.y:
                    inven.inven_on = -1
                elif mouse.x < 635 and mouse.y < 630:
                    player.image = load_image('warrior_1.png')
                    player.char = 1
                    player.frame = 0
            if game_world.collide(mouse, ui):
                if mouse.x < 1075:
                    inven.inven_on = 0
            if game_world.collide(mouse, talkbox):
                if talkbox.count == 1:
                    talkbox.count = 0
                    player.job = 1      # 전사 1차 전직
                    inven.sword = 1     # 검 획득
                    if player.Lv >= 30:
                        player.job = 2  # 전사 2차 전직
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
             ui.box_on = not ui.box_on
             inven.box_on = not inven.box_on
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
    global inven
    global stumps

    running = True

    player = Player()
    game_world.add_object(player, 1)

    background = Back(player)
    game_world.add_object(background, 0)
    background.player = player

    talkbox = TalkBox()
    game_world.add_object(talkbox, 2)

    box = Box(player)
    game_world.add_object(box, 3)

    platforms0 = [Platform0(background) for _ in range(len(coordinates_list[0]))]
    game_world.add_objects(platforms0, 3)

    platforms1 = [Platform1(background) for _ in range(len(coordinates_list[1]))]
    game_world.add_objects(platforms1, 3)

    npc = NPC()
    game_world.add_object(npc, 3)

    ui = UI()
    game_world.add_object(ui, 3)
    ui.player = player

    inven = Inven()
    game_world.add_object(inven, 3)

    stumps = [Stump() for _ in range(10)]
    game_world.add_objects(stumps, 1)
    for stump in stumps:
        game_world.add_collision_pair('offense:stump', None, stump)

    mouse = Mouse()
    game_world.add_object(mouse, 3)

    game_world.add_collision_pair('player:platform0', box, None)
    for platform in platforms0:
        game_world.add_collision_pair('player:platform0', None, platform)

    game_world.add_collision_pair('player:platform1', box, None)
    for platform in platforms1:
        game_world.add_collision_pair('player:platform1', None, platform)


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