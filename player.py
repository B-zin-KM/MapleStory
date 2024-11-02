from pico2d import load_image, SDL_KEYDOWN, SDLK_SPACE, get_time, SDLK_RIGHT, SDLK_LEFT, SDL_KEYUP, SDLK_a
import math


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


class Idle:

    @staticmethod
    def enter(player, e):
        if player.action == 1:      # 오른쪽 걷기
            player.action = 3       # 오른쪽 아이들
        elif player.action == 2:    # 왼쪽 걷기
            player.action = 4       # 왼쪽 아이들
        player.dir = 0
        player.frame = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 3

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 59, player.action * 106, 59, 106, player.x, player.y)


class Walk:

    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e):
            player.dir, player.action = 1, 1
        elif left_down(e) or right_up(e):
            player.dir, player.action = -1, 2

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4
        player.x += player.dir * 5

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 59, player.action * 106, 59, 106, player.x, player.y)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transition = {
            Idle: {right_down: Walk, left_down: Walk, left_up: Walk, right_up: Walk},
            Walk: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player)

    def draw(self):
        self.cur_state.draw(self.player)

    def handle_event(self, e):  # e : state_events
        for check_event, next_state in self.transition[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True
        return False


class Player:
    def __init__(self):
        self.x, self.y = 400, 82
        self.frame = 0
        self.action = 4
        self.image = load_image('warrior_1.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()