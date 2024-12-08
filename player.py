from pico2d import *
import math

import common
from bounding_box import Box
from common import coordinates_list
from offense import Offense0

import game_world


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN

def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN

def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP

def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP

def alt_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LALT

def alt_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LALT

def ctrl_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LCTRL

def ctrl_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LCTRL

def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE


class Idle:

    idle_time = 0.5
    elapsed_time = 0.0
    last_time = 0.0

    @staticmethod
    def enter(player, e):
        if player.action == 1 or player.action == 5 or player.action == 7 or player.action == 9:
            player.action, player.dir = 3, 1
        elif player.action == 2 or player.action == 6 or player.action == 8 or player.action == 10:
            player.action, player.dir = 4, -1
        player.frame = 0
        Idle.elapsed_time = 0.0
        Idle.last_time = get_time()
        if e is not None and up_down(e):
            if common.map == 1:
                if 865 < player.x < 895 and player.y == 310:
                    player.portal_sound.play()
                    common.map = 0
                    common.scroll_x = 0
                    common.scroll_y = 0
                    player.x = 1855
                    player.y = 343
            elif common.map == 0:
                if 1840 < player.x < 1870 and player.y == 343:
                    player.portal_sound.play()
                    common.map = 1
                    player.x = 880
                    player.y = 310
                elif 122 < player.x < 152 and player.y == 223:
                    player.portal_sound.play()
                    player.x = 183
                    player.y = 827
                elif 1455 < player.x < 1485 and player.y == 950:
                    player.portal_sound.play()
                    player.x = 1490
                    player.y = 1093


    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        current_time = get_time()
        time_difference = current_time - Idle.last_time
        Idle.last_time = current_time
        Idle.elapsed_time += time_difference

        if Idle.elapsed_time >= Idle.idle_time:
            Idle.elapsed_time = 0
            player.frame = (player.frame + 1) % 4

    @staticmethod
    def draw(player):
        if player.char == 0:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 549, 41, 66, player.screen_x + 10, player.screen_y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 653, 41, 66, player.screen_x + 10, player.screen_y)
            else:
                if player.action == 3:
                    player.image.clip_draw(player.frame * 59, 338, 59, 66, player.screen_x, player.screen_y)
                elif player.action == 4:
                    player.image.clip_draw(player.frame * 59, 444, 59, 66, player.screen_x, player.screen_y)
        if player.char == 1:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 771, 50, 66, player.screen_x + 5, player.screen_y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 875, 50, 66, player.screen_x + 14, player.screen_y)
            else:
                if player.action == 3:
                    if player.frame == 0:
                        player.image.clip_draw(203, 560, 46, 66, player.screen_x + 12, player.screen_y)
                    elif player.frame == 1:
                        player.image.clip_draw(141, 560, 46, 66, player.screen_x + 12, player.screen_y)
                    elif player.frame == 2:
                        player.image.clip_draw(18, 560, 46, 66, player.screen_x + 12, player.screen_y)
                    elif player.frame == 3:
                        player.image.clip_draw(79, 560, 46, 66, player.screen_x + 12, player.screen_y)
                elif player.action == 4:
                    if player.frame == 0:
                        player.image.clip_draw(203, 666, 46, 66, player.screen_x + 7, player.screen_y)
                    elif player.frame == 1:
                        player.image.clip_draw(141, 666, 46, 66, player.screen_x + 8, player.screen_y)
                    elif player.frame == 2:
                        player.image.clip_draw(18, 666, 46, 66, player.screen_x + 9, player.screen_y)
                    elif player.frame == 3:
                        player.image.clip_draw(79, 666, 46, 66, player.screen_x + 8, player.screen_y)

class Walk:

    idle_time = 0.2
    elapsed_time = 0.0
    last_time = 0.0

    @staticmethod
    def enter(player, e):
        if e is not None:
            if right_down(e) or left_up(e):
                player.dir, player.action = 1, 1
            elif left_down(e) or right_up(e):
                player.dir, player.action = -1, 2
        else:
            if player.right_key_pressed:
                player.dir = 1
            elif player.left_key_pressed:
                player.dir = -1
        if player.dir == 1:
            player.action = 1
        if player.dir == -1:
            player.action = 2
        Walk.elapsed_time = 0.0
        Walk.last_time = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        current_time = get_time()
        time_difference = current_time - Walk.last_time
        Walk.last_time = current_time
        Walk.elapsed_time += time_difference

        if Walk.elapsed_time >= Walk.idle_time:
            Walk.elapsed_time = 0
            player.frame = (player.frame + 1) % 4

        player.x += player.dir * 1.5

    @staticmethod
    def draw(player):
        if player.char == 0:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 549, 41, 66, player.screen_x + 10, player.screen_y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 653, 41, 66, player.screen_x + 10, player.screen_y)
            else:
                if player.action == 1:
                    if player.frame % 2 == 0:
                        player.image.clip_draw(player.frame * 59, 126, 59, 66, player.screen_x, player.screen_y)
                    elif player.frame % 2 == 1:
                        player.image.clip_draw(player.frame * 59, 126, 59, 66, player.screen_x, player.screen_y - 1)
                elif player.action == 2:
                    if player.frame % 2 == 0:
                        player.image.clip_draw(player.frame * 59, 232, 59, 66, player.screen_x, player.screen_y)
                    elif player.frame % 2 == 1:
                        player.image.clip_draw(player.frame * 59, 232, 59, 66, player.screen_x, player.screen_y - 1)
        if player.char == 1:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 771, 50, 66, player.screen_x + 5, player.screen_y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 875, 50, 66, player.screen_x + 14, player.screen_y)
            else:
                if player.action == 1:
                    if player.frame == 0:
                        player.image.clip_draw(80, 347, 50, 68, player.screen_x + 14, player.screen_y)
                    elif player.frame == 1:
                        player.image.clip_draw(206, 347, 50, 68, player.screen_x + 15, player.screen_y - 1)
                    elif player.frame == 2:
                        player.image.clip_draw(143, 347, 50, 68, player.screen_x + 14, player.screen_y)
                    elif player.frame == 3:
                        player.image.clip_draw(19, 347, 50, 68, player.screen_x + 13, player.screen_y - 1)
                elif player.action == 2:
                    if player.frame == 0:
                        player.image.clip_draw(80, 453, 50, 68, player.screen_x + 11, player.screen_y)
                    elif player.frame == 1:
                        player.image.clip_draw(206, 453, 50, 68, player.screen_x + 4, player.screen_y - 1)
                    elif player.frame == 2:
                        player.image.clip_draw(143, 453, 50, 68, player.screen_x + 11, player.screen_y)
                    elif player.frame == 3:
                        player.image.clip_draw(19, 453, 50, 68, player.screen_x + 14, player.screen_y - 1)

class Prone:

    @staticmethod
    def enter(player, e):
        if player.action == 1 or player.action == 3:
            player.dir, player.action = 1, 7
        elif player.action == 2 or player.action == 4:
            player.dir, player.action = -1, 8
        player.frame = 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        if player.char == 0:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 549, 41, 66, player.screen_x + 10, player.screen_y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 653, 41, 66, player.screen_x + 10, player.screen_y)
            else:
                if player.action == 7:
                    player.image.clip_draw(78, 575, 64, 39, player.screen_x + 23, player.screen_y - 15)
                elif player.action == 8:
                    player.image.clip_draw(78, 679, 64, 39, player.screen_x - 5, player.screen_y - 15)
        if player.char == 1:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 771, 50, 66, player.screen_x + 5, player.screen_y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 875, 50, 66, player.screen_x + 14, player.screen_y)
            else:
                if player.action == 7:
                        player.image.clip_draw(87, 797, 68, 39, player.screen_x + 25, player.screen_y - 15)
                elif player.action == 8:
                        player.image.clip_draw(87, 901, 68, 39, player.screen_x - 7, player.screen_y - 15)

class Attack:

    idle_time = 0.15
    elapsed_time = 0.0
    last_time = 0.0

    ps_idle_time = 0.05
    ps_elapsed_time = 0.0
    ps_last_time = 0.0
    ps_frame = 0

    @staticmethod
    def enter(player, e):
        if player.Lv >= 10:
            player.PS_sound.play()
        if player.dir == 1:
            player.dir, player.action = 1, 9
        elif player.dir == -1:
            player.dir, player.action = -1, 10
        Attack.elapsed_time = 0.0
        Attack.last_time = get_time()

        Attack.ps_elapsed_time = 0.0
        Attack.ps_last_time = get_time()

        player.frame = 0
        Attack.ps_frame = 0
        player.attack = True

    @staticmethod
    def exit(player, e):
        player.attack = False
        pass

    @staticmethod
    def do(player):
        current_time = get_time()
        time_difference = current_time - Attack.last_time
        Attack.last_time = current_time
        Attack.elapsed_time += time_difference

        ps_current_time = get_time()
        ps_time_difference = ps_current_time - Attack.ps_last_time
        Attack.ps_last_time = ps_current_time
        Attack.ps_elapsed_time += ps_time_difference


        if Attack.ps_elapsed_time >= Attack.ps_idle_time:
            Attack.ps_elapsed_time = 0
            Attack.ps_frame = Attack.ps_frame + 1

        if Attack.elapsed_time >= Attack.idle_time:
            Attack.elapsed_time = 0
            player.frame = (player.frame + 1) % 4
            if not player.ctrl_key_pressed:
                if player.frame == 0:
                    if player.left_key_pressed or player.right_key_pressed:
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Walk
                        player.state_machine.cur_state.enter(player, None)
                    else:
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Idle
                        player.state_machine.cur_state.enter(player, None)

            if player.frame == 2:
                player.Attack_sound.play()
            if player.frame == 3:
                player.offense()


    @staticmethod
    def draw(player):
        if player.action == 9:
            if player.frame == 0:
                player.image.clip_draw(80, 24, 47, 68, player.screen_x + 15, player.screen_y)
            if player.frame == 1:
                player.image.clip_draw(80, 24, 47, 68, player.screen_x + 15, player.screen_y)
            elif player.frame == 2:
                player.image.clip_draw(19, 26, 42, 66, player.screen_x + 20, player.screen_y - 1)
            elif player.frame == 3:
                player.image.clip_draw(145, 19, 71, 73, player.screen_x + 8, player.screen_y - 8)

        elif player.action == 10:
            if player.frame == 0:
                player.image.clip_draw(80, 135, 47, 68, player.screen_x + 4, player.screen_y)
            if player.frame == 1:
                player.image.clip_draw(80, 135, 47, 68, player.screen_x + 4, player.screen_y)
            elif player.frame == 2:
                player.image.clip_draw(19, 137, 42, 66, player.screen_x - 3, player.screen_y - 1)
            elif player.frame == 3:
                player.image.clip_draw(145, 130, 71, 73, player.screen_x + 10, player.screen_y - 8)

        if player.Lv >= 10:
            if player.dir == -1:
                if Attack.ps_frame == 0:
                    player.image0.clip_draw(0, 0, 164, 156, player.x - common.scroll_x, player.y - common.scroll_y)
                elif Attack.ps_frame == 1:
                    player.image1.clip_draw(0, 0, 164, 151, player.x - common.scroll_x, player.y - common.scroll_y)
                elif Attack.ps_frame == 2:
                    player.image2.clip_draw(0, 0, 162, 144, player.x - common.scroll_x, player.y - common.scroll_y)
                elif Attack.ps_frame == 3:
                    player.image3.clip_draw(0, 0, 143, 134, player.x - common.scroll_x, player.y - common.scroll_y)
                elif Attack.ps_frame == 4:
                    player.image4.clip_draw(0, 0, 118, 103, player.x - common.scroll_x, player.y - common.scroll_y)
                elif Attack.ps_frame == 5:
                    player.image5.clip_draw(0, 0, 73, 74, player.x - common.scroll_x, player.y - common.scroll_y)
                elif Attack.ps_frame == 6:
                    player.image6.clip_draw(0, 0, 113, 81, player.x - common.scroll_x - 25, player.y - common.scroll_y)
                elif Attack.ps_frame == 7:
                    player.image6.clip_draw(0, 0, 113, 81, player.x - common.scroll_x - 25, player.y - common.scroll_y)
                elif Attack.ps_frame == 8:
                    player.image6.clip_draw(0, 0, 113, 81, player.x - common.scroll_x - 25, player.y - common.scroll_y)
                elif Attack.ps_frame == 9:
                    player.image6.clip_draw(0, 0, 113, 81, player.x - common.scroll_x - 25, player.y - common.scroll_y)

            elif player.dir == 1:
                if Attack.ps_frame == 0:
                    player.image0.composite_draw(0, 'h', player.x - common.scroll_x + 16, player.y - common.scroll_y)
                elif Attack.ps_frame == 1:
                    player.image1.composite_draw(0, 'h', player.x - common.scroll_x + 16, player.y - common.scroll_y)
                elif Attack.ps_frame == 2:
                    player.image2.composite_draw(0, 'h', player.x - common.scroll_x + 16, player.y - common.scroll_y)
                elif Attack.ps_frame == 3:
                    player.image3.composite_draw(0, 'h', player.x - common.scroll_x + 16, player.y - common.scroll_y)
                elif Attack.ps_frame == 4:
                    player.image4.composite_draw(0, 'h', player.x - common.scroll_x + 16, player.y - common.scroll_y)
                elif Attack.ps_frame == 5:
                    player.image5.composite_draw(0, 'h', player.x - common.scroll_x + 16, player.y - common.scroll_y)

                elif Attack.ps_frame == 6:
                    player.image6.composite_draw(0, 'h', player.x - common.scroll_x + 40, player.y - common.scroll_y)
                elif Attack.ps_frame == 7:
                    player.image6.composite_draw(0, 'h', player.x - common.scroll_x + 40, player.y - common.scroll_y)
                elif Attack.ps_frame == 8:
                    player.image6.composite_draw(0, 'h', player.x - common.scroll_x + 40, player.y - common.scroll_y)
                elif Attack.ps_frame == 9:
                    player.image6.composite_draw(0, 'h', player.x - common.scroll_x + 40, player.y - common.scroll_y)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transition = {
            Idle: {right_down: Walk, left_down: Walk, right_up: Walk, left_up: Walk, down_down: Prone, down_up: Idle, up_down: Idle, ctrl_down: Attack},
            Walk: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, ctrl_down: Attack},
            Prone: {down_down: Prone, down_up: Idle, right_down: Walk, left_down: Walk, right_up: Idle, left_up: Idle},
            Attack: {}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player)

    def draw(self):
        self.cur_state.draw(self.player)

    def handle_event(self, e):
        if self.player.char == 0 and (e[1].key == SDLK_LCTRL and e[1].type == SDL_KEYDOWN):
            return
        if self.cur_state == Walk and (e[1].key == SDLK_DOWN and e[1].type == SDL_KEYDOWN):
            return
        if (e[1].key == SDLK_LEFT or e[1].key == SDLK_RIGHT) and e[1].type == SDL_KEYUP:
            if self.player.down_key_pressed:
                self.cur_state = Prone
                self.cur_state.enter(self.player, e)
                return
        if e[1].key == SDLK_DOWN and e[1].type == SDL_KEYUP:
            if self.player.right_key_pressed or self.player.left_key_pressed:
                self.cur_state = Walk
                self.cur_state.enter(self.player, e)
                return
        for check_event, next_state in self.transition[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True
        return False


class Player:
    def __init__(self):
        self.x, self.y = 640, 500
        self.char = 0
        self.frame = 0
        self.action = 4
        self.image = load_image('warrior_0.png')

        self.image0 = load_image('파스0.png')
        self.image1 = load_image('파스1.png')
        self.image2 = load_image('파스2.png')
        self.image3 = load_image('파스3.png')
        self.image4 = load_image('파스4.png')
        self.image5 = load_image('파스5.png')
        self.image6 = load_image('파스스윙.png')

        self.jump_sound = load_wav('Jump.mp3')
        self.jump_sound.set_volume(20)

        self.portal_sound = load_wav('Portal.mp3')
        self.portal_sound.set_volume(40)

        self.die_sound = load_wav('Tombstone.mp3')
        self.die_sound.set_volume(40)

        self.LvUp_sound = load_wav('LevelUp.mp3')
        self.LvUp_sound.set_volume(10)

        self.DropItem_sound = load_wav('DropItem.mp3')
        self.DropItem_sound.set_volume(20)

        self.JobChanged_sound = load_wav('JobChanged.mp3')
        self.JobChanged_sound.set_volume(30)

        self.Click_sound = load_wav('BtMouseClick.mp3')
        self.Click_sound.set_volume(30)

        self.Attack_sound = load_wav('Attack.mp3')
        self.Attack_sound.set_volume(30)

        self.PS_sound = load_wav('PS.mp3')
        self.PS_sound.set_volume(30)

        self.StumpDamage_sound = load_wav('StumpDamage.mp3')
        self.StumpDamage_sound.set_volume(20)

        self.StumpDie_sound = load_wav('StumpDie.mp3')
        self.StumpDie_sound.set_volume(15)

        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.dir = -1
        self.air = True
        self.jumping = False
        self.attack = False
        self.gravity = -0.35            # 중력 가속도, 하강 시 속도가 점차 증가
        self.velocity = 0               # 현재 속도
        self.max_jump_velocity = 7.3    # 점프 시 초기 속도
        self.right_key_pressed = False
        self.left_key_pressed = False
        self.down_key_pressed = False
        self.up_key_pressed = False
        self.alt_key_pressed = False
        self.ctrl_key_pressed = False
        self.space_key_pressed = False
        self.Lv = 1
        self.level_1 = 1
        self.level_10 = 0
        self.job = 0                    # 전사 양수 / 마법사 음수
        self.HP = 0
        self.MP = 0
        self.EXP = 184
        self.offenses = []
        self.invincible = False
        self.invincible_count = 0

    def jump(self):
        if not self.jumping and not self.air:
            self.jump_sound.play()
            self.jumping = True
            self.air = True
            self.velocity = self.max_jump_velocity

    def update(self):
        global box
        global platform
        box = Box(self)
        platform = coordinates_list[common.map][0]

        if self.offenses:
            for offense in self.offenses:
                game_world.remove_object(offense)
            self.offenses.clear()

        if self.state_machine.cur_state != Idle and self.state_machine.cur_state != Attack and not (self.right_key_pressed or self.left_key_pressed or self.down_key_pressed or self.alt_key_pressed or self.ctrl_key_pressed):
            self.state_machine.cur_state = Idle
            self.state_machine.cur_state.enter(self, None)

        if not self.air and self.alt_key_pressed and not self.jumping:
            self.jump()

        if self.jumping:
            self.y += self.velocity
            self.velocity += self.gravity
            if self.velocity <= 0:
                self.jumping = False
                self.air = True
            if self.down_key_pressed:
                self.state_machine.cur_state = Prone
                self.state_machine.cur_state.enter(self, None)

        self.Gravity()
        if self.invincible:
            if self.invincible_count >= 100:
                self.invincible = False
            self.invincible_count += 1
        if self.HP >= 168:
            self.die_sound.play()
            self.HP = 80
            self.EXP = 184
            common.map = 1
            self.x, self.y = 640, 500

        self.state_machine.update()

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LALT:
                self.alt_key_pressed = True
                self.jump()
            elif event.key == SDLK_DOWN:
                self.down_key_pressed = True
            elif event.key == SDLK_UP:
                self.up_key_pressed = True
            elif event.key == SDLK_RIGHT:
                self.right_key_pressed = True
            elif event.key == SDLK_LEFT:
                self.left_key_pressed = True
            elif event.key == SDLK_LCTRL:
                self.ctrl_key_pressed = True
            elif event.key == SDLK_SPACE:
                self.space_key_pressed = True
            elif event.key == SDLK_a:   # 레벨업
                self.LvUp_sound.play()
                self.Lv += 1
                if self.Lv == 10:
                    self.JobChanged_sound.play()
                    common.attack_power += 5
                common.attack_power += 1
                self.level_10 = self.Lv // 10
                self.level_1 = self.Lv % 10
                self.EXP = 184
                self.HP = 0
                self.MP = 0

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LALT:
                self.alt_key_pressed = False
            elif event.key == SDLK_DOWN:
                self.down_key_pressed = False
            elif event.key == SDLK_UP:
                self.up_key_pressed = False
            elif event.key == SDLK_RIGHT:
                self.right_key_pressed = False
            elif event.key == SDLK_LEFT:
                self.left_key_pressed = False
            elif event.key == SDLK_LCTRL:
                self.ctrl_key_pressed = False
            elif event.key == SDLK_SPACE:
                self.space_key_pressed = False

        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        if common.box_on:
            draw_rectangle(self.x - common.scroll_x,
                           self.y - 33 - common.scroll_y,
                           self.x + 20 - common.scroll_x,
                           self.y + 33 - common.scroll_y)

    def get_bb(self):
        return self.x, self.y - 33, self.x + 20, self.y + 33
        pass

    def Gravity(self):
        if not self.jumping:
            self.velocity += self.gravity
            self.y += self.velocity

    def offense(self):
        offense = Offense0(self.x, self.y, self.dir)
        game_world.add_object(offense, 3)
        self.offenses.append(offense)
        game_world.add_collision_pair('offense:stump', offense, None)

    def handle_collision(self, group, other):
        if group == 'player:stump':
            if not self.invincible:
                self.HP += 15
                self.x += -self.dir * 15
                self.invincible = True
                self.invincible_count = 0