"""
Module for various types of bricks
"""
from colorama import Fore, Back, Style
from config import *
import numpy as np
from utils import BALL, find_bricks
from GeneralBrick import Brick
# -------
# |     |
# -------

class BasicBrick(Brick):
    """
    Type 1 brick
    """
    def __init__(self, x, y, power):
        self.__fig = np.array([[basic0 for i in range(10)],\
            [basic1 if i == 0 or i == 9 else basic2 for i in range(10)],\
                [basic0 for i in range(10)]])
        self.__health = 1
        self.__mode = 0
        self.type = 1
        Brick.__init__(self, x, y, power)  

    def health_left(self):
        return self.__health

    def dec_health(self):
        self.__health -= 1
    def destroy_health(self):
        self.__health = 0

    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()

        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[i])):
                # print(i)
                grid[y+i][x+j]=' '

    def show_brick(self, grid, x, y, mode):
        self.del_brick(grid)
        self.set_coord(x,y)
        self.show(grid,self.__fig,x,y)
       
    def check_collision(self,grid,xvel,yvel,thru,array):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel)
        self.del_brick(grid)
        self.show_brick(grid,x,y,0)
        # collide = self.collision(grid,self.__fig,BALL)
        if collide != 0:
            self.dec_health()
            # self.show_brick(grid,x,y,0)
            if self.health_left() <= 0:
                self.set_power()
                self.del_brick(grid)
        return collide
 
class PremiumBrick(Brick):
    """
    Type 2 brick
    """
    def __init__(self, x, y, power):
        self.__fig = np.array([[prem00 for i in range(10)],\
            [prem01 if i == 0 or i == 9 else prem02 for i in range(10)],\
                [prem00 for i in range(10)]])
        self.__fig1 = np.array([[prem10 for i in range(10)],\
            [prem11 if i == 0 or i == 9 else prem12 for i in range(10)],\
                [prem10 for i in range(10)]])
      
        self.__health = 2
        self.__score = 0
        self.type = 2
        self.__mode = 0
        Brick.__init__(self, x, y, power) 

    def health_left(self):
        return self.__health

    def dec_health(self):
        self.__health -= 1
    def destroy_health(self):
        self.__health = 0
    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()
        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[i])):
                grid[y+i][x+j] = ' '
    
    def show_brick(self, grid, x, y, mode):
        self.del_brick(grid)
        self.set_coord(x,y)
        color = self.health_left()
        if color == 2:
            self.show(grid,self.__fig,x,y)
        else:
            self.show(grid,self.__fig1,x,y)
            
    def check_collision(self,grid,xvel,yvel,thru,array):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel)
        if collide != 0:
            if thru == 1:
                self.destroy_health()
            self.dec_health()
            # self.show_brick(grid,x,y,0)
            if self.health_left() <= 0:
                self.del_brick(grid)
                # print('dead')
        return collide 


class UltraBrick(Brick):
    """
    Type 3 brick
    """
    def __init__(self, x, y, power):
        self.__fig = np.array([[ultra00 for i in range(10)],\
            [ultra01 if i == 0 or i == 9 else ultra02 for i in range(10)],\
                [ultra00 for i in range(10)]])
        self.__fig1 = np.array([[ultra10 for i in range(10)],\
            [ultra11 if i == 0 or i == 9 else ultra12 for i in range(10)],\
                [ultra10 for i in range(10)]])
        self.__fig2 = np.array([[ultra20 for i in range(10)],\
            [ultra21 if i == 0 or i == 9 else ultra22 for i in range(10)],\
                [ultra20 for i in range(10)]])
       
        self.__health = 3
        self.__mode = 0
        self.type = 3
        Brick.__init__(self, x, y, power)  

    def health_left(self):
        return self.__health

    def dec_health(self):
        self.__health -= 1
    def destroy_health(self):
        self.__health = 0
    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()
        # flag = self.check_collision(grid)
        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[0])):
                grid[y+i][x+j] = ' '

    def show_brick(self, grid, x, y, mode):
        self.del_brick(grid)
        self.set_coord(x,y)
        color = self.health_left()

        if color == 3:
            self.del_brick(grid)
            self.show(grid,self.__fig,x,y)
        elif color == 2:
            self.del_brick(grid)
            self.show(grid,self.__fig1,x,y)
        else:
            self.del_brick(grid)
            self.show(grid,self.__fig2,x,y)


    def check_collision(self,grid,xvel,yvel,thru,array):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel)
        # collide = self.collision(grid,self.__fig,BALL)
        if collide != 0:
            if thru == 1:
                self.destroy_health()
            self.dec_health()
            self.show_brick(grid,x,y,0)
            if self.health_left() <= 0:
                self.del_brick(grid)
        return collide        

class SolidBrick(Brick):
    """
    Unbreakable brick
    """
    def __init__(self, x, y, power):
        self.__fig = np.array([[Back.WHITE+'-','-','-','-','-','-','-','-','-','-'+Style.RESET_ALL],\
            [Back.WHITE+'|',' ',' ',' ',' ',' ',' ',' ',' ','|'+Style.RESET_ALL],\
                [Back.WHITE+'-','-','-','-','-','-','-','-','-','-'+Style.RESET_ALL]]) #10
        self.__health = 100
        self.__score = 0
        self.__mode = 0
        self.type = 4
        Brick.__init__(self, x, y, power)  
        
    def health_left(self):
        return self.__health

    def destroy_health(self):
        self.__health = 0

    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()
        # flag = self.check_collision(grid)
        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[0])):
                grid[y+i][x+j] = ' '

    def show_brick(self, grid, x, y, mode):
        self.del_brick(grid)
        self.set_coord(x,y)
        self.show(grid,self.__fig,x,y)
            
    def check_collision(self, grid,xvel,yvel,thru,array):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel)
        if collide != 0 and thru == 1:
            self.destroy_health()
            self.del_brick(grid)
            return collide
        self.show_brick(grid,x,y,0)
        return collide   
            
class ExplodeBrick(Brick):
    """
    Type 5 brick
    """
    def __init__(self, x, y, power):
        self.__fig = np.array([[ex0 for i in range(10)],\
            [ex1 if i == 0 or i == 9 else ex2 for i in range(10)],\
                [ex0 for i in range(10)]])
        self.__health = 1
        self.__mode = 0
        self.type = 5
        Brick.__init__(self, x, y, power)  

    def health_left(self):
        return self.__health

    def dec_health(self):
        self.__health -= 1
    def destroy_health(self):
        self.__health = 0
        self.__mode = 1

    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()
        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[0])):
                grid[y+i][x+j] = ' '

    def show_brick(self, grid, x, y, mode):
        self.del_brick(grid)
        self.set_coord(x,y)
        self.show(grid,self.__fig,x,y)
    
    def explode(self,grid,array):
        x,y = self.get_coord()
        self.destroy_health()
        self.__mode = 1
        checklist = [ex0,basic0,prem00,prem10,ultra00,ultra10,ultra20]
        bricks_to_explode=find_bricks(x,y,checklist,grid,array)
        for brick in bricks_to_explode:
            if brick.get_mode() == 1:
                continue
            # another exploding brick
            brick.destroy_health()


    def check_collision(self,grid,xvel,yvel,thru,array):
        x,y = self.get_coord()

        collide = self.collision(grid,self.__fig,BALL,xvel,yvel)
        if collide != 0:
            self.destroy_health()
            self.explode(grid,array)
            self.show_brick(grid,x,y,0)
            if self.health_left() <= 0:
                self.del_brick(grid)
        return collide      
