from player import Player
from config import *
import time

class PowerUp(Player):
    def __init__(self,x,y,time):
        self.active = 0
        self.start_time = time-time
        self.prevx = x
        self.prevy = y
        self.xvel=0
        self.yvel=0
        self.air_time = 0
        self.gravity = 1
        self.dead=0
        Player.__init__(self,x,y)
    
    def set_active(self):
        self.active = 1
        self.start_time=time.time()
    def set_deactive(self):
        self.active = 0
    def check_active(self):
        return self.active
    def setgravity(self):
        self.gravity=1
    def check_gravity(self):
        return 0
    def delete_powerup(self,grid,fig):
        x,y = self.get_coord()
        y-=1
        x-=2
        for i in range(len(fig)+2):
            for j in range(len(fig[0])+4):
                grid[y+i][x+j]=' '

    def drop(self,grid,fig,ball):
        if self.air_time == 0:
            self.xvel = ball.get_xvel()
            self.yvel = -ball.get_yvel()
        self.air_time+=1
        self.setgravity()
        next_pos = round(GRAVITY*self.air_time*self.check_gravity()*0.2)
        if self.air_time >= 8:
            self.yvel=max(0,self.yvel)
        if self.air_time >= 10:
            self.yvel=1
            # self.xvel=0
        x,y = self.get_coord()
        if y+self.yvel+next_pos <= 0:
            self.yvel=1
        if (x+self.xvel <= 0 or x+self.xvel >= FRAME_WIDTH-4):
            self.xvel=-(self.xvel)
        if y+self.yvel+next_pos >= 37:
            self.delete_powerup(grid,fig)
            self.dead=1
            return
        self.prevx=x
        self.prevy=y
        self.delete_powerup(grid,fig)
        self.set_coord(x+self.xvel,y+self.yvel+next_pos)
        self.show(grid,fig,x,y)
       
class Power_Extend(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[EXTEND,EXTEND],[EXTEND,EXTEND]]
        PowerUp.__init__(self,x,y,time)

    def display(self,grid,ball):
        self.drop(grid,self.fig,ball)

    def check_collision(self,grid,paddle):
        x,y=self.get_coord()
        coll = paddle.check_collision(grid,x,y)
        coll1 = paddle.check_collision(grid,x+1,y)
        if coll != 0 or coll1 != 0:
            self.delete_powerup(grid,self.fig)
            return 1
        return 0

    def activate(self,paddle,ball,grid):
        x=2
        if paddle.get_length() >= 16:
            x=0
        paddle.set_extend(grid,x)
        self.set_active()
        return 1
        # paddle.set_extend(grid)
        # if paddle.get_extend() == 1:
        #     self.set_active()
        #     return 1
        # return 0
    def deactivate(self,paddle,ball,grid):
        x=-2
        if paddle.get_length() > 16:
            x=0
        paddle.set_extend(grid,x)
        self.set_deactive()
        # print('deactivated')
        return 1
        # paddle.reset_extend(grid)
        # if paddle.get_extend() == 0:
        #     self.set_deactive()
        #     return 1
        # return 0

class Power_Grab(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[GRAB,GRAB],[GRAB,GRAB]]
        PowerUp.__init__(self,x,y,time)

    def display(self,grid,ball):
        self.drop(grid,self.fig,ball)
    def check_collision(self,grid,paddle):
        # coll = paddle.check_collision(grid,self.fig[1][0])
        # coll1 = paddle.check_collision(grid,self.fig[1][1])
        x,y=self.get_coord()
        coll = paddle.check_collision(grid,x,y)
        coll1 = paddle.check_collision(grid,x+1,y)
        if coll != 0 or coll1 != 0:
            self.delete_powerup(grid,self.fig)
            return 1
        return 0

    def activate(self,paddle,ball,grid):
        ball.set_catch()
        if ball.get_catch() == 1:
            self.set_active()
            return 1
        return 0
    def deactivate(self,paddle,ball,grid):
        ball.set_catch()
        if ball.get_catch() == 0:
            self.set_deactive()
            return 1
        return 0


class Power_Shrink(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[SHRINK,SHRINK],[SHRINK,SHRINK]]
        PowerUp.__init__(self,x,y,time)

    def display(self,grid,ball):
        self.drop(grid,self.fig,ball)
    def check_collision(self,grid,paddle):
        # coll = paddle.check_collision(grid,self.fig[1][0])
        # coll1 = paddle.check_collision(grid,self.fig[1][1])
        x,y=self.get_coord()
        coll = paddle.check_collision(grid,x,y)
        coll1 = paddle.check_collision(grid,x+1,y)
        if coll != 0 or coll1 != 0:
            self.delete_powerup(grid,self.fig)
            return 1
        return 0
    def activate(self,paddle,ball,grid):
        x=-2
        if paddle.get_length() <= 6:
            x=0
        paddle.set_extend(grid,x)
        self.set_active()
        # print('activated')
        return 1
        # paddle.set_extend(grid)
        # if paddle.get_extend() == 1:
        #     self.set_active()
        #     return 1
        # return 0
    def deactivate(self,paddle,ball,grid):
        x=2
        if paddle.get_length() < 6:
            x=0
        paddle.set_extend(grid,x)
        self.set_deactive()
        # print('deactivated')
        return 1
       
class Power_Multiplier(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[MULTIPLIER,MULTIPLIER],[MULTIPLIER,MULTIPLIER]]
        PowerUp.__init__(self,x,y,time)

    def display(self,grid,ball):
        self.drop(grid,self.fig,ball)
    def check_collision(self,grid,paddle):
        # coll = paddle.check_collision(grid,self.fig[1][0])
        # coll1 = paddle.check_collision(grid,self.fig[1][1])
        x,y=self.get_coord()
        coll = paddle.check_collision(grid,x,y)
        coll1 = paddle.check_collision(grid,x+1,y)
        if coll != 0 or coll1 != 0:
            self.delete_powerup(grid,self.fig)
            return 1
        return 0

    def activate(self,paddle,ball,grid):
        ball.set_multiplier()
        if ball.get_multiplier() == 1:
            self.set_active()
            return 1
        return 0

    def deactivate(self,paddle,ball,grid):
        ball.set_multiplier()
        if ball.get_multiplier() == 0:
            self.set_deactive()
            return 1
        return 0

class Power_Thru(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[THRU,THRU],[THRU,THRU]]
        PowerUp.__init__(self,x,y,time)
    def display(self,grid,ball):
        self.drop(grid,self.fig,ball)
    def check_collision(self,grid,paddle):
        # coll = paddle.check_collision(grid,self.fig[1][0])
        # coll1 = paddle.check_collision(grid,self.fig[1][1])
        x,y=self.get_coord()
        coll = paddle.check_collision(grid,x,y)
        coll1 = paddle.check_collision(grid,x+1,y)
        if coll != 0 or coll1 != 0:
            self.delete_powerup(grid,self.fig)
            return 1
        return 0

    def activate(self,paddle,ball,grid):
        ball.set_thru()
        if ball.get_thru() == 1:
            self.set_active()
            return 1
        return 0

    def deactivate(self,paddle,ball,grid):
        ball.set_thru()
        if ball.get_thru() == 0:
            self.set_deactive()
            return 1
        return 0

class Power_Fast(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[FAST,FAST],[FAST,FAST]]
        PowerUp.__init__(self,x,y,time)
    def display(self,grid,ball):
        self.drop(grid,self.fig,ball)  

    def check_collision(self,grid,paddle):
        # coll = paddle.check_collision(grid,self.fig[1][0])
        # coll1 = paddle.check_collision(grid,self.fig[1][1])
        x,y=self.get_coord()
        coll = paddle.check_collision(grid,x,y)
        coll1 = paddle.check_collision(grid,x+1,y)
        if coll != 0 or coll1 != 0:
            self.delete_powerup(grid,self.fig)
            return 1
        return 0

    def activate(self,paddle,ball,grid):
        ball.set_speedup()
        if ball.get_speedup() == 1:
            self.set_active()
            return 1
        return 0
    def deactivate(self,paddle,ball,grid):
        ball.set_speedup()
        if ball.get_speedup() == 0:
            self.set_deactive()
            return 1
        return 0

class Power_Shoot(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[SHOOT,SHOOT],[SHOOT,SHOOT]]
        PowerUp.__init__(self,x,y,time)

    def display(self,grid,ball):
        self.drop(grid,self.fig,ball)

    def check_collision(self,grid,paddle):
        x,y=self.get_coord()
        coll = paddle.check_collision(grid,x,y)
        coll1 = paddle.check_collision(grid,x+1,y)
        if coll != 0 or coll1 != 0:
            self.delete_powerup(grid,self.fig)
            return 1
        return 0

    def activate(self,paddle,ball,grid):
        paddle.set_shooter(1)
        self.set_active()
        return 1
        
    def deactivate(self,paddle,ball,grid):
        paddle.set_shooter(0)
        self.set_deactive()
        return 1


class Power_Fire(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[FIRE,FIRE],[FIRE,FIRE]]
        PowerUp.__init__(self,x,y,time)
    def display(self,grid,ball):
        self.drop(grid,self.fig,ball)
    def check_collision(self,grid,paddle):
        x,y=self.get_coord()
        coll = paddle.check_collision(grid,x,y)
        coll1 = paddle.check_collision(grid,x+1,y)
        if coll != 0 or coll1 != 0:
            self.delete_powerup(grid,self.fig)
            return 1
        return 0

    def activate(self,paddle,ball,grid):
        ball.set_fire()
        if ball.get_fire() == 1:
            self.set_active()
            return 1
        return 0

    def deactivate(self,paddle,ball,grid):
        ball.set_fire()
        if ball.get_fire() == 0:
            self.set_deactive()
            return 1
        return 0