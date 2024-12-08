from pico2d import *
import time
import common
from background import Back, Platform0, Platform1
from player import Player
from bounding_box import Box
from npc import NPC
from talk_box import TalkBox
from ui import UI
from inven import Inven
from common import coordinates_list
from stump import Stump
from stumpy import Stumpy
from start import Start
from clear import Clear

import game_world

stump_last_spawn_time = time.time()
stump_spawn_interval = 10

class Mouse:
    def __init__(self):
        self.x, self.y = 0, 0

    def update(self):
        pass

    def handle_event(self, event):
        if event.type in (SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP):
            self.x, self.y = event.x, get_canvas_height() - event.y

    def get_bb(self):
        return self.x - 3, self.y - 3, self.x + 3, self.y + 3

    def draw(self):
        if common.box_on:
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
    global offense
    global stump
    global start
    global start_on

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
                    player.Click_sound.play()
                    inven.inven_on = 0
                elif mouse.x < 676 and 645 < mouse.y:
                    player.Click_sound.play()
                    inven.inven_on = 1
                elif 726 < mouse.x < 770 and 645 < mouse.y:
                    player.Click_sound.play()
                    inven.inven_on = 2
                elif 795 < mouse.x and 678 < mouse.y:
                    player.Click_sound.play()
                    inven.inven_on = -1
                elif mouse.x < 635 and mouse.y < 630:
                    player.DropItem_sound.play()
                    player.image = load_image('warrior_1.png')
                    player.char = 1
                    player.frame = 0
            if game_world.collide(mouse, ui):
                if mouse.x < 1075:
                    player.Click_sound.play()
                    inven.inven_on = 0
            if game_world.collide(mouse, talkbox):
                if talkbox.count == 1:
                    player.Click_sound.play()
                    player.JobChanged_sound.play()
                    talkbox.count = 0
                    player.job = 1      # 전사 1차 전직
                    inven.sword = 1     # 검 획득
            if common.start_on:
                if game_world.collide(mouse, start):
                    player.Click_sound.play()
                    game_world.remove_object(start)
                    common.start_on = False
                    del start
                    background.bgm.repeat_play()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            if talkbox.count == 1:
                talkbox.count = 0
            else:
                running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
             common.box_on = not common.box_on
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
    global stumpy
    global start
    global clear

    running = True

    start = Start()
    game_world.add_object(start, 4)

    player = Player()
    game_world.add_object(player, 1)

    background = Back(player)
    game_world.add_object(background, 0)
    background.player = player
    game_world.add_collision_pair('player:stump', player, None)

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

    stumps = [Stump(player) for _ in range(10)]
    game_world.add_objects(stumps, 0)
    for stump in stumps:
        game_world.add_collision_pair('offense:stump', None, stump)
        game_world.add_collision_pair('player:stump', None, stump)

    stumpy = Stumpy(player)
    game_world.add_object(stumpy, 0)

    clear = Clear()
    game_world.add_object(clear, 4)

    mouse = Mouse()
    game_world.add_object(mouse, 3)

    game_world.add_collision_pair('player:platform0', box, None)
    for platform in platforms0:
        game_world.add_collision_pair('player:platform0', None, platform)

    game_world.add_collision_pair('player:platform1', box, None)
    for platform in platforms1:
        game_world.add_collision_pair('player:platform1', None, platform)

    global stump_last_spawn_time
    stump_last_spawn_time = time.time()


def update_world():
    global stump_last_spawn_time
    game_world.update()

    current_time = time.time()
    if current_time - stump_last_spawn_time >= stump_spawn_interval:
        if game_world.count_object(1) < 10 + 1:
            spawn_stump()
            stump_last_spawn_time = current_time


def render_world():
    clear_canvas()
    game_world.render()
    print_location(player)
    update_canvas()


def print_location(obj):
    player_coordinates = f"player   state: {str(obj.state_machine.cur_state)}, x: {int(obj.x)}, y: {int(obj.y)}"
    sys.stdout.write("\r" + player_coordinates)
    sys.stdout.flush()


def spawn_stump():
    global stump

    stump = Stump(player)
    game_world.add_object(stump, 0)
    game_world.add_collision_pair('offense:stump', None, stump)
    game_world.add_collision_pair('player:stump', None, stump)


open_canvas(1280, 800)
reset_world()


while running:
    handle_events()
    update_world()
    render_world()

    delay(0.01)


close_canvas()