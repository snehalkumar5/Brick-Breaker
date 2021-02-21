"""
Module for paddle
"""
from colorama import Fore, Back, Style
from config import *
import numpy as np
from utils import BALL
from player import Player

class Paddle(Player):
    """
    Main player
    """
    def __init__(self, x, y):
        self.__fig = np.array([[body0 if i == 0 or i== 11 else body1 for i in range(12)],\
            [body2 if i == 0 or i== 11 else body1 for i in range(12)]])
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

        Player.__init__(self, x, y)  

    def lives_left(self):
        return self.__lives
    def set_lives(self,x):
        self.__lives = x
    def dec_lives(self):
        self.__lives -= 1

    def show_score(self):
        return self.__score
    def inc_score(self):
        self.__score += 10

    def check_grab(self):
        return self.__grab
    def set_grab(self):
        self.__grab = 0 if self.__grab == 1 else 1
    def grab_set(self):
        self.__grab = 1
    def get_length(self):
        # fig = self.getfig()
        return len(self.__fig[0])
    def set_length(self,x):
        # fig = self.getfig()
        ee = self.get_length()
        return x+ee
        
    def del_paddle(self, grid):
        x,y = self.get_coord()
        fig = self.getfig()
        for i in range(len(fig)):
            for j in range(len(fig[i])):
                grid[y+i][x+j]=' '

    def getfig(self):
        return self.__fig

    def change_size(self,x):
        length = self.get_length()+x
        self.__fig = np.array([[body0 if i==0 or i == length-1 else body1 for i in range(length)],[body2 if i==0 or i == length-1 else body1 for i in range(length)]])
       

    # def get_extend(self):
    #     return self.__extend
    def set_extend(self,grid,change):
        self.del_paddle(grid)
        self.change_size(change)
        x,y=self.get_coord()
        self.show_paddle(grid,x,y)
    # def reset_extend(self,grid,change):
    #     self.del_paddle(grid)
    #     self.change_size(change)
    #     x,y=self.get_coord()
    #     self.show_paddle(grid,x,y)

    # def get_shrink(self):
    #     return self.__shrink
    # def set_shrink(self,grid):  
    #     self.del_paddle(grid)
    #     self.__shrink = 1
    #     x,y=self.get_coord()
    #     self.show_paddle(grid,x,y)
    # def reset_shrink(self,grid):
    #     self.del_paddle(grid)
    #     self.__shrink = 0
    #     x,y=self.get_coord()
    #     self.show_paddle(grid,x,y)

    def show_paddle(self, grid, x, y):
        self.del_paddle(grid)
        self.set_coord(x,y)
        fig = self.getfig()
        # print('figure:',fig)
        self.show(grid,fig,x,y)

    def check_collision(self,grid,obstacle):
        x, y = self.get_coord()
        y-=1
        length = self.get_length()
        chunk = length//2
        ran = (length-4)//2
        for p in range(2):
            if grid[y+p][x+chunk-1]==obstacle or grid[y+p][x+chunk]==obstacle:
                return 1
            if ran >= 4:
                if grid[y+p][x+chunk-2]==obstacle or grid[y+p][x+chunk+1]==obstacle:
                    return 1
            if grid[y+p][x]==obstacle or grid[y+p][x+1]==obstacle or grid[y+p][x-1] == obstacle:
                return 3
            if grid[y+p][x+length-1]==obstacle or grid[y+p][x+length-2]==obstacle or grid[y+p][x+length]==obstacle:
                return 3
            for i in range(length):
                if grid[y+p][x+i]==obstacle:
                    if i < chunk:
                        return 2
                    else:
                        return 2
        return 0