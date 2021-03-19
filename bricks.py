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
        self.__fig = np.array(BASIC0)
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
        self.__mode = 1

    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()

        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[i])):
                # print(i)
                grid[y+i][x+j]=' '

    def show_brick(self, grid, x, y, mode):
        if y>=FRAME_HEIGHT-6:
            return 1
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

    def check_collision(self,grid,xvel,yvel,thru,array,fire,a,b):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel,a,b)
        self.del_brick(grid)
        self.show_brick(grid,x,y,0)
        # collide = self.collision(grid,self.__fig,BALL)
        if collide != 0:
            if thru == 1:
                self.destroy_health()
            if fire == 1:
                self.explode(grid,array)
            os.system('aplay -q ./sounds/collide.wav&')

            self.dec_health()
            # self.show_brick(grid,x,y,0)
            if self.health_left() <= 0:
                self.del_brick(grid)
        return collide
 
class PremiumBrick(Brick):
    """
    Type 2 brick
    """
    def __init__(self, x, y, power):
        self.__fig = np.array(PREM0)
        self.__fig1 = np.array(PREM1)
      
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
        self.__mode = 1
    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()
        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[i])):
                grid[y+i][x+j] = ' '
    
    def show_brick(self, grid, x, y, mode):
        if y>=FRAME_HEIGHT-6:
            return 1
        self.del_brick(grid)
        self.set_coord(x,y)
        color = self.health_left()
        if color == 2:
            self.show(grid,self.__fig,x,y)
        else:
            self.show(grid,self.__fig1,x,y)
            
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

    def check_collision(self,grid,xvel,yvel,thru,array,fire,a,b):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel,a,b)
        if collide != 0:
            os.system('aplay -q ./sounds/collide.wav&')

            if thru == 1:
                self.destroy_health()
            if fire == 1:
                self.explode(grid,array)
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
        self.__fig = np.array(ULTRA0)
        self.__fig1 = np.array(ULTRA1)
        self.__fig2 = np.array(ULTRA2)
       
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
        self.__mode = 1
    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()
        # flag = self.check_collision(grid)
        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[0])):
                grid[y+i][x+j] = ' '

    def show_brick(self, grid, x, y, mode):
        if y>=FRAME_HEIGHT-6:
            return 1
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

    def check_collision(self,grid,xvel,yvel,thru,array,fire,a,b):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel,a,b)
        # collide = self.collision(grid,self.__fig,BALL)
        if collide != 0:
            os.system('aplay -q ./sounds/collide.wav&')
            if thru == 1:
                self.destroy_health()
            if fire == 1:
                self.explode(grid,array)
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
        self.__fig = np.array(SOLID0) #10
        self.__health = 100
        self.__score = 0
        self.__mode = 0
        self.type = 4
        Brick.__init__(self, x, y, power)  
        
    def health_left(self):
        return self.__health

    def destroy_health(self):
        self.__health = 0
        self.__mode = 1

    def get_mode(self):
        return self.__mode

    def del_brick(self, grid):
        x,y = self.get_coord()
        # flag = self.check_collision(grid)
        for i in range(len(self.__fig)):
            for j in range(len(self.__fig[0])):
                grid[y+i][x+j] = ' '

    def show_brick(self, grid, x, y, mode):
        if y>=FRAME_HEIGHT-6:
            return 1
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

    def check_collision(self, grid,xvel,yvel,thru,array,fire,a,b):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel,a,b)
        if collide != 0:
            os.system('aplay -q ./sounds/collide.wav&')
            if thru == 1:
                self.destroy_health()
                self.del_brick(grid)
                return collide
            if fire == 1:
                self.explode(grid,array)
        self.show_brick(grid,x,y,0)
        return collide   

class ExplodeBrick(Brick):
    """
    Type 5 brick
    """
    def __init__(self, x, y, power):
        self.__fig = np.array(EXPLODE0)
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
        if y>=FRAME_HEIGHT-6:
            return 1
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


    def check_collision(self,grid,xvel,yvel,thru,array,fire,a,b):
        x,y = self.get_coord()

        collide = self.collision(grid,self.__fig,BALL,xvel,yvel,a,b)
        if collide != 0:
            os.system('aplay -q ./sounds/explode.wav&')
            self.destroy_health()
            self.explode(grid,array)
            self.show_brick(grid,x,y,0)
            if self.health_left() <= 0:
                self.del_brick(grid)
        return collide  


class PrideBrick(Brick):
    """
    Type 6 brick
    """
    def __init__(self, x, y, power):
        self.__fig = np.array(SOLID0)
        self.__health = 10
        self.__mode = 0
        self.type = 6
        self.choose = np.array([BASIC0,PREM0,ULTRA0])
        self.index = 0
        self.brick=-1
        self.color=0
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

    def get_fig(self):
        if self.brick==-1:
            self.index = (self.index+1)%3
            fig = self.choose[self.index]
            return fig
        else:
            return self.__fig

    def del_brick(self, grid):
        x,y = self.get_coord()
        fig = self.get_fig()
        for i in range(len(fig)):
            for j in range(len(fig[0])):
                grid[y+i][x+j] = ' '

    def show_brick(self, grid, x, y, mode):
        if y>=FRAME_HEIGHT-6:
            return 1
        self.del_brick(grid)
        self.set_coord(x,y)
        color = self.health_left()
        fig = self.get_fig()
        if self.brick == -1:
            self.show(grid,fig,x,y)
        else:
            if self.index == 3 or self.index == 0:
                self.show(grid,fig,x,y)
                return
            if self.index == 2:
                if color == 3:
                    self.del_brick(grid)
                    self.show(grid,fig[0],x,y)
                elif color == 2:
                    self.del_brick(grid)
                    self.show(grid,fig[1],x,y)
                else:
                    self.del_brick(grid)
                    self.show(grid,self.__fig[2],x,y)
            elif self.index == 1:
                if color == 2:
                    self.del_brick(grid)
                    self.show(grid,self.__fig[0],x,y)
                else:
                    self.del_brick(grid)
                    self.show(grid,self.__fig[1],x,y)
        return
    
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

    def check_collision(self,grid,xvel,yvel,thru,array,fire,a,b):
        x,y = self.get_coord()
        collide = self.collision(grid,self.__fig,BALL,xvel,yvel,a,b)
        if collide != 0:
            os.system('aplay -q ./sounds/collide.wav&')
            if thru == 1:
                self.destroy_health()
            if fire == 1:
                self.explode(grid,array)
            if self.brick == -1:
                self.brick=1
                if self.index == 0:
                    #basic 
                    self.__health = 1
                    self.__fig = np.array(BASIC0)
                elif self.index == 1:
                    #premium 
                    self.__health = 2
                    self.__fig = np.array([PREM0,PREM1])
                elif self.index == 2:
                    #ultra
                    self.__health = 3
                    self.__fig = np.array([ULTRA0,ULTRA1,ULTRA2])
                # elif self.index == 3:
                #     #solid 
                #     self.__health = 100
                #     self.__fig = np.array(SOLID0)
                return collide
            self.dec_health()                
            self.show_brick(grid,x,y,0)
            if self.health_left() <= 0:
                self.del_brick(grid)
        return collide        