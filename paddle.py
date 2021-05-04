"""
Module for paddle
"""
from colorama import Fore, Back, Style
from config import *
import numpy as np
from utils import BALL
from player import Player
import time

class Paddle(Player):
    """
    Main player
    """
    def __init__(self, x, y):
        self.__fig = np.array([[body0 if i == 0 or i== 11 else body1 for i in range(12)],\
            [body2 if i == 0 or i== 11 else body1 for i in range(12)]])
        # self.__fig1 = np.array([[body2 if i == 0 or i== 11 else body1 for i in range(12)],\
        #     [body2 if i == 0 or i== 11 else body1 for i in range(12)]])
        # self.__fig1 = np.array([[body0 if i == 0 or i== 17 else body1 for i in range(18)],\
        #     [body2 if i == 0 or i== 17 else body1 for i in range(18)]]) #extended
        # self.__fig2 = np.array([[body0 if i == 0 or i== 5 else body1 for i in range(6)],\
        #     [body2 if i == 0 or i== 5 else body1 for i in range(6)]]) # shrink
        self.__lives = 10
        self.__score = 0
        self.__grab = 1
        self.__starttime = 0
        self.__endtime = 10
        self.__extend = 0
        self.__shrink = 0
        self.__shoot = 0

        Player.__init__(self, x, y)  

    def lives_left(self):
        return self.__lives
    def set_lives(self,x):
        self.__lives = x
    def dec_lives(self):
        os.system('aplay -q ./sounds/lose_life.wav&')
        self.__lives -= 1
        self.force_dead_shoot()

    def show_score(self):
        return self.__score
    def inc_score(self,x=10):
        self.__score += x

    def check_grab(self):
        return self.__grab
    def set_grab(self):
        self.__grab = 0 if self.__grab == 1 else 1
    def grab_set(self):
        self.__grab = 1

    def get_length(self):
        return len(self.__fig[0])
    def set_length(self,x):
        ee = self.get_length()
        return x+ee
    def force_dead_shoot(self):
        self.__shoot=0

    def set_shooter(self,x):
        # if x == 1:
        #     if self.__shoot == 0:
        #         self.__shoot = x
        #         self.__starttime=time.time()
        #     else:
        #         return
        # elif self.get_shoot_time()<=0:
        self.__shoot = x

    def get_shoot(self):
        return self.__shoot
    def get_shoot_time(self):
        if self.__shoot == 1:
            return 10-int(time.time()-self.__starttime)
        return 0
            
    def del_paddle(self, grid):
        x,y = self.get_coord()
        fig = self.getfig()
        for i in range(len(fig)):
            for j in range(len(fig[i])):
                grid[y+i][x+j]=' '

    def getfig(self):
        fig = self.__fig
        if self.get_shoot()==1:
            fig[0][0] = body2
            fig[0][self.get_length()-1]=body2
        else:
            fig[0][0] = body0
            fig[0][self.get_length()-1]=body0
        return fig

    def change_size(self,x):
        length = self.get_length()+x
        self.__fig = np.array([[body0 if i==0 or i == length-1 else body1 for i in range(length)],[body2 if i==0 or i == length-1 else body1 for i in range(length)]])
       
    def set_extend(self,grid,change):
        self.del_paddle(grid)
        self.change_size(change)
        x,y=self.get_coord()
        self.show_paddle(grid,x,y)

    def show_paddle(self, grid, x, y):
        self.del_paddle(grid)
        self.set_coord(x,y)
        fig = self.getfig()
        self.show(grid,fig,x,y)

    def check_collision(self,grid,a,b):
        x, y = self.get_coord()
        y-=1
        length = self.get_length()
        # for i in range(length):
        #     if y==b:
        #         if x+i == a:
        #             return 1
        # return 0

        chunk = length//2
        ran = (length-4)//2
        for p in range(2):
            # if grid[y+p][x+chunk-1]==obstacle or grid[y+p][x+chunk]==obstacle:
            if((y+p==b and x+chunk-1==a) or (y+p==b and x+chunk==a)):
                return 1
            if ran >= 4:
                # if grid[y+p][x+chunk-2]==obstacle or grid[y+p][x+chunk+1]==obstacle:
                if((y+p==b and x+chunk-2==a) or (y+p==b and x+chunk+1==a)):
                    return 1
            # if grid[y+p][x]==obstacle or grid[y+p][x+1]==obstacle or grid[y+p][x-1] == obstacle:
            if((y+p==b and x+1==a) or (y+p==b and x-1==a)):
                return 3
            # if grid[y+p][x+length-1]==obstacle or grid[y+p][x+length-2]==obstacle or grid[y+p][x+length]==obstacle:
            if((y+p==b and x+length-1==a) or (y+p==b and x+length-2==a)):
                return 3
            for i in range(length):
                # if grid[y+p][x+i]==obstacle:
                if(y+p==b and x+i==a):
                    if i < chunk:
                        return 2
                    else:
                        return 2
        return 0