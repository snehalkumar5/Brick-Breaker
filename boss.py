"""
Module for boss
"""
from colorama import Fore, Back, Style
from config import *
import numpy as np
from utils import BALL
from player import Player
from bricks import *

class Boss(Player):
    """
    Main player
    """
    def __init__(self, x, y):
        self.__fig = np.array([[" "," "," ",".","-","-","-","."," "," "," "],\
            [" ","_","/","_","_","~","0","_","\\","_"," "],\
                ["(","_","_","_","_","_","_","_","_","_",")"]])
        self.__health = 10
        self.spawned = 0
        Player.__init__(self,x, y)  

    def get_length(self):
        return len(self.__fig[0])
    def getfig(self):
        return self.__fig
    def get_health(self):
        return self.__health
    def dec_health(self):
        os.system('aplay -q ./sounds/collide_boss.wav&')
        self.__health -= 1
        self.spawned=0
    def del_boss(self,grid):
        x,y = self.get_coord()
        fig = self.getfig()
        for i in range(len(fig)):
            for j in range(len(fig[i])):
                grid[y+i][x+j]=' '    
    def show(self, grid, x, y, brickarray):
        self.del_boss(grid)
        self.set_coord(x,y)
        fig = self.getfig()
        health = self.get_health()
        if health==2 and self.spawned==0:
            self.spawn_protecc(grid,brickarray)
        if health==6 and self.spawned==0:
            self.spawn_protecc(grid,brickarray)

        Player.show(self,grid,fig,x,y)

    def check_collision(self,grid,a,b):
        x,y = self.get_coord()
        width = self.get_length()
        if((b==y and x==a) or (b==y+1 and x==a)):
            self.dec_health()
            return 2
        if((b==y and x+width==a) or (b==y+1 and x+width==a)):
            self.dec_health()
            return 2
        for i in range(width):
            if(b==y+2 and x+i==a):
                self.dec_health()
                return 3
        return 0  
    def spawn_protecc(self,grid,brickarray):
        if self.spawned == 1:
            return
        y=8
        x=5
        if self.get_health()==2:
            y=5
        while(True):
            if x>FRAME_WIDTH-10:
                self.spawned=1
                break
            brickarray.append(BasicBrick(x,y,0))
            x+=10



