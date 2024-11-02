from pico2d import *
import gfw
import math
from player.Gun import Gun
from player.Bullet import Bullet

class Actor(gfw.Sprite):   
    PLAYER_FRAMES = {
        "IDLE": [
            (0, 20, 18, 20), (0, 20, 18, 20), (0, 20, 18, 20)
        ],
        "WALK": [
            (0, 42, 18, 20), (18, 42, 18, 20), (36, 42, 18, 20), 
            (0, 62, 18, 20), (18, 62, 18, 20), (36, 62, 18, 20),
        ],
        "BACK": [
            (36, 62, 18, 20), (18, 62, 18, 20), (0, 62, 18, 20), 
            (36, 42, 18, 20), (18, 42, 18, 20), (0, 42, 18, 20), 
        ],
        "DEAD": [
            (19, 0, 18, 20), (37, 0, 18, 20),
        ],
    }
   
    def __init__(self, path):
        x = get_canvas_width() // 2
        y = get_canvas_height() // 2
        super().__init__(path, x, y)
        
        # 애니메이션 관련
        self.state = None
        self.frame_index = 0
        self.frame_time = 0
        self.elapsed_time = 0
        self.hp = 3 # 레벨업 요소
        
        self._do_IDLE()
 
        # 이동 관련
        self.dx, self.dy = 0, 0
        self.speed = 100 # 레벨업 요소
        self.degree = 0
        self.flip = 'h'
        
        # 총 관련
        self.gun = Gun()
        
        # 총알 관련
        self.bullet_time = 1  
        self.bullet_Colltime = 1 # 레벨업 요소
        self.bullet_range = 200 # 레벨업 요소
        self.bullet_speed = 1000 # 레벨업 요소
        self.bullet_ColCnt = 1 # 레벨업 요소
        self.bullet_RowCnt = 1 # 레벨업 요소

        self.bg = None
    # 업데이트            
    def update(self):
        self.x += self.dx * self.speed * gfw.frame_time
        self.y += self.dy * self.speed * gfw.frame_time
        
        # 사격 쿨타임 증가
        if self.bullet_time <= self.bullet_Colltime:
            self.bullet_time += gfw.frame_time
        
        # 애니메이션 전환
        self.elapsed_time += gfw.frame_time
        if self.elapsed_time >= self.frame_time:
            self.elapsed_time = 0 
            # 다음 프레임으로 전환
            self.frame_index = (self.frame_index + 1) % self.frame_count
            
        #self.bg.show(self.x, self.y)
            
    # 드로우        
    def draw(self):
        current_frame = Actor.PLAYER_FRAMES[self.state][self.frame_index]
        x1, y1, x2, y2 = current_frame

        #screen_pos = self.bg.to_screen(self.x, self.y)
        self.image.clip_composite_draw(*current_frame,  0, self.flip, self.x, self.y, w=50, h=50)
        self.gun.draw(self.flip, self.x, self.y)
             
    ## ---------------------------------------------------------------------------     
    def adjust_delta(self, x, y):
        self.dx += x
        self.dy += y
           
    def rotate(self, tx, ty):
        if tx - self.x > 0:
            self.flip = ' '
        else:
            self.flip = 'h'

        self.gun.rotate(tx, ty, self.flip)
        
    # 총알 발사
    def fire(self):
        if self.bullet_time < self.bullet_Colltime: return
        #print('fire!')
        world = gfw.top().world
        bulletInfo = self.gun.x, self.gun.y, self.gun.angle, self.bullet_range, self.bullet_speed, self.flip
        world.append(Bullet(*bulletInfo), world.layer.bullet)
        self.bullet_time = 0
        
    # 상태 변경
    def checkState(self):
        if self._isDead():
            self._do_DEAD()
            
        elif self._isMove():
            if self._isBack(): self._do_BackWALK()
            else: self._do_WALK()
        else:
            self._do_IDLE()
        
    def _isDead(self):
        if self.hp <= 0:
            return True
        return False
    
    def _isBack(self):
        if self.flip == ' ':
            if self.dx < 0 or self.dy > 0:
                return True
        else:
            if self.dx > 0 or self.dy < 0:
                return True
        return False
    
    def _isMove(self):
        if (abs(self.dx) + abs(self.dy)) > 0:
            return True
        return False
               
    def _update_frame_count(self):
        self.frame_count = len(Actor.PLAYER_FRAMES[self.state])
        
    def _change_state(self, name):
        if self.state != name or self.state == None:
            self.state = name
            self.frame_index = 0
            self.elapsed_time = 0
            self._update_frame_count()
    
    # 상태별 행동
    def _do_IDLE(self):
        if self.state == 'IDLE':
            return
        self._change_state('IDLE')
        self.frame_time = 1 / 5
            
    def _do_WALK(self):
        if self.state == 'WALK':
            return
        self._change_state("WALK")
        self.frame_time = 1 / 12
        
    def _do_BackWALK(self):
        if self.state == 'BACK':
            return
        self._change_state("BACK")
        self.frame_time = 1 / 12
        
    def _do_DEAD(self):
        if self.state == 'DEAD':
            return
        self._change_state("DEAD")
        self.frame_time = 1 / 3
    

    