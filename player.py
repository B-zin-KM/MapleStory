from pico2d import load_image, SDL_KEYDOWN, SDLK_RIGHT, SDLK_LEFT, SDLK_LALT, SDLK_LCTRL, SDLK_a, SDL_KEYUP, SDLK_DOWN, get_time, draw_rectangle
import math


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
                    player.image.clip_draw(19, 549, 41, 66, player.x + 10, player.y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 653, 41, 66, player.x + 10, player.y)
            else:
                if player.action == 3:
                    player.image.clip_draw(player.frame * 59, 338, 59, 66, player.x, player.y)
                elif player.action == 4:
                    player.image.clip_draw(player.frame * 59, 444, 59, 66, player.x, player.y)
        if player.char == 1:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 771, 50, 66, player.x + 5, player.y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 875, 50, 66, player.x + 14, player.y)
            else:
                if player.action == 3:
                    if player.frame == 0:
                        player.image.clip_draw(203, 560, 46, 66, player.x + 12, player.y)
                    elif player.frame == 1:
                        player.image.clip_draw(141, 560, 46, 66, player.x + 12, player.y)
                    elif player.frame == 2:
                        player.image.clip_draw(18, 560, 46, 66, player.x + 12, player.y)
                    elif player.frame == 3:
                        player.image.clip_draw(79, 560, 46, 66, player.x + 12, player.y)
                elif player.action == 4:
                    if player.frame == 0:
                        player.image.clip_draw(203, 666, 46, 66, player.x + 7, player.y)
                    elif player.frame == 1:
                        player.image.clip_draw(141, 666, 46, 66, player.x + 8, player.y)
                    elif player.frame == 2:
                        player.image.clip_draw(18, 666, 46, 66, player.x + 9, player.y)
                    elif player.frame == 3:
                        player.image.clip_draw(79, 666, 46, 66, player.x + 8, player.y)

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
                    player.image.clip_draw(19, 549, 41, 66, player.x + 10, player.y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 653, 41, 66, player.x + 10, player.y)
            else:
                if player.action == 1:
                    if player.frame % 2 == 0:
                        player.image.clip_draw(player.frame * 59, 126, 59, 66, player.x, player.y)
                    elif player.frame % 2 == 1:
                        player.image.clip_draw(player.frame * 59, 126, 59, 66, player.x, player.y - 1)
                elif player.action == 2:
                    if player.frame % 2 == 0:
                        player.image.clip_draw(player.frame * 59, 232, 59, 66, player.x, player.y)
                    elif player.frame % 2 == 1:
                        player.image.clip_draw(player.frame * 59, 232, 59, 66, player.x, player.y - 1)
        if player.char == 1:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 771, 50, 66, player.x + 5, player.y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 875, 50, 66, player.x + 14, player.y)
            else:
                if player.action == 1:
                    if player.frame == 0:
                        player.image.clip_draw(80, 347, 50, 68, player.x + 14, player.y)
                    elif player.frame == 1:
                        player.image.clip_draw(206, 347, 50, 68, player.x + 15, player.y - 1)
                    elif player.frame == 2:
                        player.image.clip_draw(143, 347, 50, 68, player.x + 14, player.y)
                    elif player.frame == 3:
                        player.image.clip_draw(19, 347, 50, 68, player.x + 13, player.y - 1)
                elif player.action == 2:
                    if player.frame == 0:
                        player.image.clip_draw(80, 453, 50, 68, player.x + 11, player.y)
                    elif player.frame == 1:
                        player.image.clip_draw(206, 453, 50, 68, player.x + 4, player.y - 1)
                    elif player.frame == 2:
                        player.image.clip_draw(143, 453, 50, 68, player.x + 11, player.y)
                    elif player.frame == 3:
                        player.image.clip_draw(19, 453, 50, 68, player.x + 14, player.y - 1)

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
                    player.image.clip_draw(19, 549, 41, 66, player.x + 10, player.y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 653, 41, 66, player.x + 10, player.y)
            else:
                if player.action == 7:
                    player.image.clip_draw(78, 575, 64, 39, player.x + 23, player.y - 15)
                elif player.action == 8:
                    player.image.clip_draw(78, 679, 64, 39, player.x - 5, player.y - 15)
        if player.char == 1:
            if player.air:
                if player.dir == 1:
                    player.image.clip_draw(19, 771, 50, 66, player.x + 5, player.y)
                elif player.dir == -1:
                    player.image.clip_draw(19, 875, 50, 66, player.x + 14, player.y)
            else:
                if player.action == 7:
                        player.image.clip_draw(87, 797, 68, 39, player.x + 25, player.y - 15)
                elif player.action == 8:
                        player.image.clip_draw(87, 901, 68, 39, player.x - 7, player.y - 15)

class Attack:

    idle_time = 0.15
    elapsed_time = 0.0
    last_time = 0.0

    @staticmethod
    def enter(player, e):
        if player.dir == 1:
            player.dir, player.action = 1, 9
        elif player.dir == -1:
            player.dir, player.action = -1, 10
        Attack.elapsed_time = 0.0
        Attack.last_time = get_time()
        player.frame = 0
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

    @staticmethod
    def draw(player):
        if player.action == 9:
            if player.frame == 0:
                player.image.clip_draw(80, 24, 47, 68, player.x + 15, player.y)
            if player.frame == 1:
                player.image.clip_draw(80, 24, 47, 68, player.x + 15, player.y)
            elif player.frame == 2:
                player.image.clip_draw(19, 26, 42, 66, player.x + 20, player.y - 1)
            elif player.frame == 3:
                player.image.clip_draw(145, 19, 71, 73, player.x + 8, player.y - 8)

        elif player.action == 10:
            if player.frame == 0:
                player.image.clip_draw(80, 135, 47, 68, player.x + 4, player.y)
            if player.frame == 1:
                player.image.clip_draw(80, 135, 47, 68, player.x + 4, player.y)
            elif player.frame == 2:
                player.image.clip_draw(19, 137, 42, 66, player.x - 3, player.y - 1)
            elif player.frame == 3:
                player.image.clip_draw(145, 130, 71, 73, player.x + 10, player.y - 8)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transition = {
            Idle: {right_down: Walk, left_down: Walk, right_up: Walk, left_up: Walk, down_down: Prone, down_up: Idle, ctrl_down: Attack},
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
        self.x, self.y = 400, 250
        self.char = 0
        self.frame = 0
        self.action = 4
        self.image = load_image('warrior_0.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.dir = -1
        self.air = False
        self.jumping = False
        self.attack = False
        self.gravity = -0.35            # 중력 가속도, 하강 시 속도가 점차 증가
        self.velocity = 0               # 현재 속도
        self.max_jump_velocity = 7.3    # 점프 시 초기 속도
        self.right_key_pressed = False
        self.left_key_pressed = False
        self.down_key_pressed = False
        self.alt_key_pressed = False
        self.ctrl_key_pressed = False

    def jump(self):
        if not self.jumping and not self.air:
            self.jumping = True
            self.velocity = self.max_jump_velocity

    def update(self):
        if self.state_machine.cur_state != Idle and self.state_machine.cur_state != Attack and not (self.right_key_pressed or self.left_key_pressed or self.down_key_pressed or self.alt_key_pressed or self.ctrl_key_pressed):
            self.state_machine.cur_state = Idle
            self.state_machine.cur_state.enter(self, None)

        if not self.air and self.alt_key_pressed and not self.jumping:
            self.jump()

        if self.jumping:
            self.y += self.velocity
            self.velocity += self.gravity
            if self.y <= 82:
                self.y = 82
                self.velocity = 0
                self.jumping = False
                self.air = False
                if self.down_key_pressed:
                    self.state_machine.cur_state = Prone
                    self.state_machine.cur_state.enter(self, None)

        Gravity(self)
        self.state_machine.update()

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LALT:
                self.alt_key_pressed = True
                self.jump()
            elif event.key == SDLK_DOWN:
                self.down_key_pressed = True
            elif event.key == SDLK_RIGHT:
                self.right_key_pressed = True
            elif event.key == SDLK_LEFT:
                self.left_key_pressed = True
            elif event.key == SDLK_LCTRL:
                self.ctrl_key_pressed = True
            elif event.key == SDLK_a:
                self.image = load_image('warrior_1.png')
                self.char = 1
                self.frame = 0

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LALT:
                self.alt_key_pressed = False
            elif event.key == SDLK_DOWN:
                self.down_key_pressed = False
            elif event.key == SDLK_RIGHT:
                self.right_key_pressed = False
            elif event.key == SDLK_LEFT:
                self.left_key_pressed = False
            elif event.key == SDLK_LCTRL:
                self.ctrl_key_pressed = False

        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()


def Gravity(obj):
    if obj.y > 82:
        obj.air = True
    else:
        obj.air = False
        obj.y = 82
        obj.velocity = 0

    if not obj.jumping:
        if obj.air:
            obj.velocity += obj.gravity
            obj.y += obj.velocity
            if obj.y <= 82:
                obj.y = 82
                obj.velocity = 0
                obj.air = False