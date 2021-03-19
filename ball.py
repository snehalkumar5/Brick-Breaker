import numpy as np
from config import FRAME_HEIGHT,FRAME_WIDTH
from player import Player
from utils import BALL
import os

class Ball(Player):
    """
    Class for Ball
    """
    def __init__(self,x,y,z,velx=1,vely=1):
        self.fig = np.array([BALL])
        self.__catch = 0
        self.angle = 0
        self.__x_vel = velx
        self.__y_vel = vely
        self.__speedup = 0
        self.__thru = 0
        self.__fire = 0
        self.__multiplier = 0
        self.numspawns = 0
        self.spawn = z
        Player.__init__(self,x,y)   

    def set_catch(self):
        self.__catch = 0 if self.__catch == 1 else 1
    def get_catch(self):
        return self.__catch
    def set_speed(self,x,y):
        if x >=2:
            x=2
        if y>=2:
            y=2
        if x <=-2:
            x=-2
        if y<=-2:
            y=-2
        self.__x_vel = x
        self.__y_vel = y
    def get_speedup(self):
        return self.__speedup
    def set_speedup(self):
        self.__speedup = 0 if self.__speedup == 1 else 1
    def get_thru(self):
        return self.__thru
    def set_thru(self):
        self.__thru = 0 if self.__thru == 1 else 1
    def get_fire(self):
        return self.__fire
    def set_fire(self):
        self.__fire = 0 if self.__fire == 1 else 1
    def get_multiplier(self):
        return self.__multiplier
    def set_multiplier(self,x):
        self.__multiplier = x
    def get_xvel(self):
        return self.__x_vel
    def get_yvel(self):
        return self.__y_vel
    def setspawn(self):
        self.spawn = 1 if self.spawn == 0 else 0
    def clear_ball(self,grid):
        x,y = self.get_coord()
        grid[y][x]= ' '
        
    def show(self,grid,x,y):
        self.clear_ball(grid)
        self.set_coord(x,y)
        grid[y][x]=self.fig[0]
        # print('x y:',x,y)


    def move_ball(self,grid,bricksarr,paddle,boss):
        x,y = self.get_coord()
        if self.spawn == 1:
            return 0,[]
        # print('new:',x,y,self.get_catch())
        collide,rem = self.check_collision(grid,bricksarr,paddle,boss,x,y)
        if collide == 6:
            return collide,rem
        if collide == 5:
            self.clear_ball(grid)
            self.show(grid,x,y)
            return collide,rem
        x+=self.get_xvel()
        y+=self.get_yvel()
        if self.get_speedup() == 1:
            x+=self.get_xvel()
            y+=self.get_yvel()
        self.show(grid,x,y)
        return collide,rem

    def check_collision(self,grid,brickarr,paddle,boss,x,y):
        x,y = self.get_coord()
        beast = self.get_thru()
        fire = self.get_fire()
        x_vel = self.get_xvel()
        y_vel = self.get_yvel()
        rem=[]
        if y >= 38:
            return 6,rem
        if y <= 1:
            self.clear_ball(grid)
            self.set_coord(x,1)
            os.system('aplay -q ./sounds/collide.wav&')
            self.set_speed(x_vel,-y_vel)
            return 1,rem
        if x >= FRAME_WIDTH-10:
            os.system('aplay -q ./sounds/collide.wav&')
            self.set_speed(-x_vel,y_vel)
            return 1,rem
        if x <= 1:
            os.system('aplay -q ./sounds/collide.wav&')
            self.clear_ball(grid)
            self.set_speed(-x_vel,y_vel)
            return 1,rem
        for i in range(len(brickarr)):
            collide_brick = brickarr[i].check_collision(grid,x_vel,y_vel,beast,brickarr,fire,x,y)
            if collide_brick==0:
                continue
            elif collide_brick==1 or collide_brick == 3: 
                self.set_speed(x_vel,-y_vel)
                if brickarr[i].health_left()<=0:
                    brickarr[i].del_brick(grid)
                    rem.append(i)
                    return 9,rem
                return 2,rem
            elif collide_brick==2:
                self.set_speed(-x_vel,y_vel)
                if brickarr[i].health_left()<=0:
                    brickarr[i].del_brick(grid)
                    rem.append(i)
                    return 9,rem
                return 2,rem
        
        #CHECK BOSS COLLISION
        if boss!=0:
            collide_boss = boss.check_collision(grid,x,y)
            if collide_boss == 2:
                self.set_speed(-x_vel,y_vel)
                return 7,rem
            elif collide_boss == 3:
                self.set_speed(x_vel,-y_vel)
                return 7,rem
            
       
        #CHECK PADDLE COLLISION
        collide_pad = paddle.check_collision(grid,x,y)
        # if paddle.check_grab()==1 and collide_pad!=0:
        #     return 5,rem

        # print('eadaeda',collide_pad)
        if collide_pad == 0:
            return 0,rem
        # if collide_pad == 1:
        #     self.set_speed(0,-y_vel)
        # elif collide_pad == 2:
        #     self.set_speed(1,-y_vel)
        # elif collide_pad == -2:
        #     self.set_speed(-1,-y_vel)
        # elif collide_pad == 3:
        #     self.set_speed(2,-y_vel)
        # elif collide_pad == -3:
        #     self.set_speed(-2,-y_vel)
        if collide_pad == 1:
            self.set_speed(x_vel,-y_vel)
        elif collide_pad == 2:
            if x_vel >= 0:
                self.set_speed(x_vel+1,-y_vel)
            else:
                self.set_speed(x_vel-1,-y_vel)
        elif collide_pad == 3: 
            if x_vel >= 0:
                self.set_speed(x_vel+2,-y_vel)
            else:
                self.set_speed(x_vel-2,-y_vel)
        os.system('aplay -q ./sounds/collide.wav&')
        if paddle.check_grab() == 1:
            return 5,rem
        else:
            return 3 ,rem

        return 0,rem

# 0 - NOP        
# 1 - WALL
# 2 - BRICK
# 3 - PADDLE
# 5 - GRAB
# 6 - DEAD
# 7 - BOSS
# 9 - BRICK DEAD