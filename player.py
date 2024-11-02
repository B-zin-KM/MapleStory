from pico2d import load_image, SDL_KEYDOWN, SDLK_SPACE, get_time, SDLK_RIGHT, SDLK_LEFT, SDL_KEYUP, SDLK_a
import math


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


class Idle:

    @staticmethod
    def enter(player, e):
        if player.action == 0:
            player.action = 2
        elif player.action == 1:
            player.action = 3
        player.dir = 0
        player.frame = 0
        player.wait_time = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8
        if get_time() - player.wait_time > 5:
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 100, player.action * 100, 100, 100, player.x, player.y)


class Sleep:

    @staticmethod
    def enter(player, e):
        player.frame = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8

    @staticmethod
    def draw(player):
        if player.action == 2:
            player.image.clip_composite_draw(player.frame * 100, 200, 100, 100, math.pi / 2, '', player.x + 25, player.y - 25, 100,
                                          100)
        else:
            player.image.clip_composite_draw(player.frame * 100, 300, 100, 100, math.pi / 2, '', player.x - 25, player.y - 25, 100,
                                          100)

class Run:

    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e):
            player.dir, player.action = 1, 1
        elif left_down(e) or right_up(e):
            player.dir, player.action = -1, 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8
        player.x += player.dir * 5

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 100, player.action * 100, 100, 100, player.x, player.y)


class AutoRun:
    @staticmethod
    def enter(player, e):
        if player.action == 0 or player.action == 2:
            player.action = 0
            player.dir = -1
        elif player.action == 1 or player.action == 3:
            player.action = 1
            player.dir = 1
        player.wait_time = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8
        player.x += player.dir * 10
        if player.x >= 800:
            player.dir, player.action = -1, 0
        elif player.x <= 0:
            player.dir, player.action = 1, 1
        if get_time() - player.wait_time > 5:
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 100, player.action * 100, 100, 100, player.x, player.y + 145, 500, 500)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Sleep
        self.transition = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, a_down: AutoRun, a_up: AutoRun,
                   time_out: Sleep},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, a_down: AutoRun, a_up: AutoRun},
            Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, space_down: Idle, a_down: AutoRun,
                    a_up: AutoRun},
            AutoRun: {time_out: Idle, right_down: Run, right_up: Run, left_down: Run, left_up: Run}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player)

    def draw(self):
        self.cur_state.draw(self.player)

    def handle_event(self, e):  # e : state_events
        for check_evnet, next_state in self.transition[self.cur_state].items():
            if check_evnet(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True
        return False


class Player:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.action = 3
        self.wait_time = 0
        self.image = load_image('warrior_sprite.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()