import numpy as np
from config import FRAME_HEIGHT,FRAME_WIDTH
from player import Player
from utils import BALL

class Ball(Player):
    """
    Class for Ball
    """
    def __init__(self,x,y):
        self.fig = np.array([BALL])
        self.__catch = 0
        self.angle = 0
        self.__x_vel = 1
        self.__y_vel = 1
        self.__speedup = 0
        self.__thru = 0
        self.__multiplier = 0
        self.numspawns = 0
        self.spawn = 1
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
    def get_multiplier(self):
        return self.__multiplier
    def set_multiplier(self):
        self.__multiplier = 0 if self.__multiplier == 1 else 1
        # self.__multiplier = 1
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


    def move_ball(self,grid,bricksarr,paddle):
        x,y = self.get_coord()
        # print('new:',x,y,self.get_catch())
        collide = self.check_collision(grid,bricksarr,paddle)
        # print('collided',collide)
        if collide == 6:
            return collide
       
        if collide == 5:
            self.clear_ball(grid)
            self.show(grid,x,y)
            return collide
        x+=self.get_xvel()
        y+=self.get_yvel()
        if self.get_speedup() == 1:
            x+=self.get_xvel()
            y+=self.get_yvel()
        # self.set_coord(x,y)
        self.show(grid,x,y)
        return collide

    def check_collision(self,grid,brickarr,paddle):
        x,y = self.get_coord()
        beast = self.get_thru()
        x_vel = self.get_xvel()
        y_vel = self.get_yvel()
        if y >= 38:
            return 6
        if y <= 1:
            self.clear_ball(grid)
            self.set_coord(x,1)

            self.set_speed(x_vel,-y_vel)
            return 1
        if x >= FRAME_WIDTH-10:
            self.set_speed(-x_vel,y_vel)
            return 1
        if x <= 1:
            self.clear_ball(grid)
            self.set_speed(-x_vel,y_vel)
            return 1
        for i in range(len(brickarr)):
            collide_brick = brickarr[i].check_collision(grid,x_vel,y_vel,beast,brickarr)
            if collide_brick==0:
                continue
            elif collide_brick==1 or collide_brick == 3: 
                self.set_speed(x_vel,-y_vel)
                if brickarr[i].health_left()==0:
                    brickarr.pop(i)
                    return 9
                return 2
            elif collide_brick==2:
                self.set_speed(-x_vel,y_vel)
                if brickarr[i].health_left()==0:
                    brickarr.pop(i)
                    return 9
                return 2

        collide_pad = paddle.check_collision(grid,BALL)
        # if paddle.check_grab()==1 and collide_pad!=0:
        #     return 5

        # print(collide_pad)
        if collide_pad == 0:
            return 0
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
        if paddle.check_grab() == 1:
            return 5
        else:
            return 3   
        return 0
