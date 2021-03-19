import numpy as np
from config import FRAME_HEIGHT,FRAME_WIDTH,SHOOT,SHOOT1
from player import Player
from utils import BALL
import os

class Bullet(Player):
    """
    Class for Bullet
    """
    def __init__(self,x,y,z):
        self.boss=z
        self.fig = SHOOT
        self.fig1 = SHOOT1
        self.active = 1
        self.start = 0
        self.crash=0
        Player.__init__(self,x,y)   

    def set_crash(self):
        self.__crash = 0 if self.__crash == 1 else 1
    def get_crash(self):
        return self.__crash
    def get_fig(self):
        if self.boss == 1:
            return self.fig1
        return self.fig
    def clear_bullet(self,grid):
        x,y = self.get_coord()
        if self.active == 0:
            grid[y][x]= ' '
        if self.boss == 1:
            grid[y-1][x]= ' '
        else:
            grid[y+1][x]= ' '
        
    def show(self,grid):
        self.clear_bullet(grid)
        x,y = self.get_coord()
        fig=SHOOT if self.boss == 0 else SHOOT1
        grid[y][x]=fig if grid[y][x]!=BALL else ' '

    def move_bullet(self,grid,paddle,boss,brickarray):
        x,y = self.get_coord()
        if self.active == 0:
            return 0
        collide = self.check_collision(grid,paddle,boss,brickarray)
        # print('bullet',x,y,collide)
        self.show(grid)
        if collide == 0:
            if self.active == 1:
                if self.boss == 1:
                    self.set_coord(x,y+1)
                else:
                    self.set_coord(x,y-1)
            self.show(grid)
            return collide
        else:
            self.clear_bullet(grid)
            if collide == 1:
                self.active=0
                return collide
            if self.boss == 1:
                self.active=0
                paddle.dec_lives()
                return collide
            elif boss!=0:
                self.active=0
                boss.dec_health()
            return collide

    def check_collision(self,grid,paddle,boss,brickarray):
        x,y = self.get_coord()
        if y >= FRAME_HEIGHT-3 or y<=1:
            self.clear_bullet(grid)
            self.active=0
            return 1
        if x >= FRAME_WIDTH-10 or x<=1:
            self.clear_bullet(grid)
            self.active=0
            return 1
        if self.boss == 1:
            if paddle.check_collision(grid,x,y)!=0:
                # print('ee')
                self.active=0
                return 2
        if self.boss == 0:
            if boss!=0 and boss.check_collision(grid,x,y)!=0:
                self.active=0
                return 3
            else:
                for i in brickarray:
                    if i.check_collision(grid,0,-1,0,brickarray,0,x,y)!=0:
                        self.active=0
                        if i.health_left()<=0:
                            i.del_brick(grid)
                            brickarray.remove(i)
                        return 1
        return 0
        
        
        