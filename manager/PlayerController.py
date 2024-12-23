from pico2d import * 
import gfw
from player import Actor
from player import Aim
 
 # 분리해야될 기능 많음.
class PlayerController:
    def __init__(self): pass
    def update(self): pass
    def draw(self): pass
    def handle_event(self, e): pass
    
class PlayerController_main(PlayerController):
    def __init__(self, bg):
        self.player = Actor('player/mainC.png', bg)
        self.aim = Aim()
        self.world = gfw.top().world
        world = gfw.top().world
        world.append(self.player, world.layer.player)
        world.append(self.aim, world.layer.UI)
        self.hitTime = 0
        self.ending_Sound = gfw.sound.sfx('Lose.wav')
        self.ending_Sound.set_volume(60)
        self.end = False
        self.__font = gfw.font.load('neodgm.TTF', 256)
    def draw(self):
        if not self.end: return
        time_text = "Win!"
        centerX = gfw.get_canvas_width() / 2
        y = gfw.get_canvas_height() / 2
        self.__font.draw(centerX - centerX / 2, y, time_text, (0, 255, 255))
    def update(self):
        if self.end: return
        if self.player.state == 'DEAD':
            self.hitTime += gfw.frame_time
            if self.hitTime >= 1:
                self.hitTime = 0
                self.ending_Sound.play()
                gfw.top().ending()
        else:
            self.player.rotate(self.aim.x, self.aim.y)
            self.player.checkState()
    def handle_event(self, e):
        # 에임 설정
        if self.end: return
        if self.player.state == "DEAD": return

        if e.type == SDL_MOUSEMOTION:
            mouse_x,  mouse_y = e.x, get_canvas_height() - e.y
            self.aim.setLoaction(mouse_x, mouse_y)
        
        if e.type == SDLK_l:
            self.Xp += 1
        
        # 사격 수행
        if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                self.player.fire()
        
        # 이동 설정
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.player.adjust_delta(-1, 0)
            elif e.key == SDLK_d:
                self.player.adjust_delta(1, 0)
            elif e.key == SDLK_w:
                self.player.adjust_delta(0, 1)
            elif e.key == SDLK_s:
                self.player.adjust_delta(0, -1)
            elif e.key == SDLK_l:
                self.player.Xp +=1
                
        if e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.player.adjust_delta(1, 0)
            elif e.key == SDLK_d:
                self.player.adjust_delta(-1, 0)
            elif e.key == SDLK_w:
                self.player.adjust_delta(0, -1)
            elif e.key == SDLK_s:
                self.player.adjust_delta(0, 1)

    def Init(self, key_states):
        if key_states[26]:
            self.player.adjust_delta(0, 1)
        if key_states[4]:
            self.player.adjust_delta(-1, 0)
        if key_states[22]:
            self.player.adjust_delta(0, -1)
        if key_states[7]:
            self.player.adjust_delta(1, 0)
    def KeyCheck(self, key_states):
        if key_states[26]:
            self.player.adjust_delta(0, -1)
        if key_states[4]:
            self.player.adjust_delta(1, 0)
        if key_states[22]:
            self.player.adjust_delta(0, 1)
        if key_states[7]:
            self.player.adjust_delta(-1, 0)