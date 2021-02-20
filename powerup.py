from player import Player
from config import *

class PowerUp(Player):
    def __init__(self,x,y,time):
        self.active = 0
        self.start_time = time
        Player.__init__(self,x,y)
    
    def set_active(self):
        self.active = 1
    def set_deactive(self):
        self.active = 0
    def check_active(self):
        return self.active

    def delete_powerup(self,grid,fig):
        x,y = self.get_coord()
        y-=1
        for i in range(len(fig)+1):
            for j in range(len(fig[0])):
                grid[y+i][x+j]=" "

    def drop(self,grid,fig):
        x,y = self.get_coord()
        if y >= 37:
            self.delete_powerup(grid,fig)
            return
        self.delete_powerup(grid,fig)
        self.set_coord(x,y+1)
        self.show(grid,fig,x,y)
       
class Power_Extend(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[EXTEND,EXTEND],[EXTEND,EXTEND]]
        PowerUp.__init__(self,x,y,time)

    def display(self,grid):
        self.drop(grid,self.fig)

    def check_collision(self,grid,paddle):
        coll = paddle.check_collision(grid,self.fig[1][0])
        coll1 = paddle.check_collision(grid,self.fig[1][1])
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
        print('deactivated')
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

    def display(self,grid):
        self.drop(grid,self.fig)
    def check_collision(self,grid,paddle):
        coll = paddle.check_collision(grid,self.fig[1][0])
        coll1 = paddle.check_collision(grid,self.fig[1][1])
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

    def display(self,grid):
        self.drop(grid,self.fig)
    def check_collision(self,grid,paddle):
        coll = paddle.check_collision(grid,self.fig[1][0])
        coll1 = paddle.check_collision(grid,self.fig[1][1])
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
        print('activated')
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
        print('deactivated')
        return 1
       
class Power_Multiplier(PowerUp):

    def __init__(self,x,y,time):
        self.fig = [[MULTIPLIER,MULTIPLIER],[MULTIPLIER,MULTIPLIER]]
        PowerUp.__init__(self,x,y,time)

    def display(self,grid):
        self.drop(grid,self.fig)
    def check_collision(self,grid,paddle):
        coll = paddle.check_collision(grid,self.fig[1][0])
        coll1 = paddle.check_collision(grid,self.fig[1][1])
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
    def display(self,grid):
        self.drop(grid,self.fig)
    def check_collision(self,grid,paddle):
        coll = paddle.check_collision(grid,self.fig[1][0])
        coll1 = paddle.check_collision(grid,self.fig[1][1])
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
    def display(self,grid):
        self.drop(grid,self.fig)  

    def check_collision(self,grid,paddle):
        coll = paddle.check_collision(grid,self.fig[1][0])
        coll1 = paddle.check_collision(grid,self.fig[1][1])
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