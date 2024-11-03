from pico2d import load_image, SDL_KEYDOWN, SDLK_RIGHT, SDLK_LEFT, SDL_KEYUP, SDLK_DOWN, get_time, draw_rectangle
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


class Idle:

    idle_time = 0.5
    elapsed_time = 0.0
    last_time = 0.0

    @staticmethod
    def enter(player, e):
        if player.action == 1 or player.action == 7:      # 오른쪽 걷기, 오른쪽 엎드리기
            player.action = 3                             # 오른쪽 아이들
        elif player.action == 2 or player.action == 8:    # 왼쪽 걷기, 왼쪽 엎드리기
            player.action = 4                             # 왼쪽 아이들
        player.dir = 0
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
        if player.action == 3:
            player.image.clip_draw(player.frame * 59, 338, 59, 66, player.x, player.y)
        elif player.action == 4:
            player.image.clip_draw(player.frame * 59, 444, 59, 66, player.x, player.y)
        # 캐릭터 주변에 사각형 테두리 그리기
        left = player.x - 59 // 2 + 16
        bottom = player.y - 66 // 2
        right = player.x + 59 // 2 + 2
        top = player.y + 70 // 2
        draw_rectangle(left, bottom, right, top)


class Walk:

    idle_time = 0.2
    elapsed_time = 0.0
    last_time = 0.0

    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e):
            player.dir, player.action = 1, 1
        elif left_down(e) or right_up(e):
            player.dir, player.action = -1, 2
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
        if player.action == 1:
            player.image.clip_draw(player.frame * 59, 126, 59, 66, player.x, player.y)
        elif player.action == 2:
            player.image.clip_draw(player.frame * 59, 232, 59, 66, player.x, player.y)
        # 캐릭터 주변에 사각형 테두리 그리기
        left = player.x - 59 // 2 + 16
        bottom = player.y - 66 // 2
        right = player.x + 59 // 2 + 2
        top = player.y + 70 // 2
        draw_rectangle(left, bottom, right, top)


class Prone:

    @staticmethod
    def enter(player, e):
        if player.action == 1 or player.action == 3:
            player.dir, player.action = 0, 7
        elif player.action == 2 or player.action == 4:
            player.dir, player.action = 0, 8
        player.frame = 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        if player.action == 7:
            player.x = player.x + 23
            player.image.clip_draw(player.frame * 78, 575, 64, 39, player.x, player.y - 15)
            player.x = player.x - 23
            # 캐릭터 주변에 사각형 테두리 그리기
            left = player.x - 78 // 2 + 26
            bottom = player.y - 39 // 2 - 15
            right = player.x + 78 // 2 + 18
            top = player.y + 39 // 2 - 10
            draw_rectangle(left, bottom, right, top)
        elif player.action == 8:
            player.x = player.x - 5
            player.image.clip_draw(player.frame * 78, 679, 64, 39, player.x, player.y - 15)
            player.x = player.x + 5
            # 캐릭터 주변에 사각형 테두리 그리기
            left = player.x - 78 // 2
            bottom = player.y - 39 // 2 - 15
            right = player.x + 78 // 2 - 8
            top = player.y + 39 // 2 - 10
            draw_rectangle(left, bottom, right, top)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.prone = False
        self.transition = {
            Idle: {right_down: Walk, left_down: Walk, right_up: Walk, left_up: Walk, down_down: Prone, down_up: Idle},
            Walk: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
            Prone: {down_down: Prone, down_up: Idle, right_down: Walk, left_down: Walk, right_up: Idle, left_up: Idle}
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