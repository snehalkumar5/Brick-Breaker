import random
import time
import numpy as np
from colorama import init as coloramaInit, Fore, Style, deinit as coloramaReset
from config import *
from board import Board
from paddle import Paddle
from bricks import *
from ball import *
from input import Get,input_to
from utils import *
from powerup import *

myboard = Board(FRAME_HEIGHT,FRAME_WIDTH)
myboard.create_board()

mypaddle = Paddle(70,36)
xx,yy = mypaddle.get_coord()
x = random.randint(xx,xx+mypaddle.get_length())
# myball = Ball(x,yy-1)
balls=[]

def add_ball(addball,balls):
    for i in addball:
        balls.append(i)

def remove_ball(removeballs,balls,grid):
    for i in removeballs:
        i.clear_ball(grid)
        balls.remove(i)


def balls_show(grid,arr,brick_arr,paddle):
    for i in arr:
        i.move_ball(grid,brick_arr,paddle)

bricks_arr = []
BRICKSNUM=0
BRICKSLEFT=0
def spawn_bricks(x,y,step):
    # print('y:',y)
    if x >= FRAME_WIDTH-20:
        y += 3
        x = 5
        # step += 75
        if y%2 == 0:
            x = 15
            # x = 1
    if y >= 15:
        return 
    pp = 1 if random.random()>0.7 else 0
    if y == 5:
        mybricks = UltraBrick(x,y,pp)
        # mybricks.show_brick(myboard.grid,x,y,0)
    elif y == 8:
        if x < FRAME_WIDTH/8:
            mybricks = PremiumBrick(x,y,pp)
        elif x <FRAME_WIDTH/4:
            mybricks = ExplodeBrick(x,y,pp)
        elif x < FRAME_WIDTH - 120:
            mybricks = ExplodeBrick(x,y,pp)
        elif x < FRAME_WIDTH -110:
            mybricks = SolidBrick(x,y,pp)
        elif x < FRAME_WIDTH - 70:
            mybricks = ExplodeBrick(x,y,pp)
        elif x < FRAME_WIDTH - 60:
            mybricks = SolidBrick(x,y,pp)
        elif x < FRAME_WIDTH - 50:
            mybricks = PremiumBrick(x,y,pp)
        elif x < FRAME_WIDTH - 40:
            mybricks = UltraBrick(x,y,pp)
        elif x < FRAME_WIDTH - 30:
            mybricks = PremiumBrick(x,y,pp)
        else: 
            mybricks = SolidBrick(x,y,pp)

    elif y == 11:
        mybricks = PremiumBrick(x,y,pp)
    else:
        mybricks = BasicBrick(x,y,pp)
    # if y == 8:
    #     if x < FRAME_WIDTH/2:
    #         mybricks = ExplodeBrick(x,y,pp)
    #     else:
    #         mybricks = PremiumBrick(x,y,pp)
        # mybricks.show_brick(myboard.grid,x,y,0)

    bricks_arr.append(mybricks)
    next_x = x + 20   
    next_y = y
    if y==8:
        next_x = x + 10   

    spawn_bricks(next_x,next_y,step)
    return

def bricksshow(grid,arr,paddle):
    flag = 1
    for i in arr:
        x,y=i.get_coord()
        if i.type!=4:
            flag=0
        if i.health_left() <= 0:
            i.del_brick(grid)
            arr.remove(i)
            paddle.inc_score()
            continue
        i.show_brick(grid,x,y,0)
    return flag
    
powerups = [] # spawned
activepowers = [] # activated
inactivepowers = [] # not activated yet

def dropthabomb(x,y):
    if random.random()<=0.3:
        return
    rand = random.randint(0,6)
    if rand >= 5:
        # power = Power_Grab(x,y,time.time())
        power = Power_Extend(x,y,time.time())
    elif rand >= 4:
        power = Power_Shrink(x,y,time.time())
    elif rand >= 3:
        power = Power_Fast(x,y,time.time())
    elif rand >= 2:
        power = Power_Grab(x,y,time.time())
    elif rand >= 1:
        power = Power_Thru(x,y,time.time())
    else: 
        power = Power_Multiplier(x,y,time.time())
    powerups.append(power)
    

def active_powers(cur_time,paddle,ball,grid):
    for x,i in enumerate(activepowers):
        if cur_time-i.start_time > POWERTIME:
            if i.deactivate(paddle,ball,grid) == 1:
                activepowers.pop(x)
                # del i
                return

def inactive_powers(paddle,ball,grid):
    for x,i in enumerate(inactivepowers):
        if i.activate(paddle,ball,grid) == 1:
            activepowers.append(i)
            inactivepowers.pop(x)

def droppings(paddle,grid):
    for x,i in enumerate(powerups):
        i.display(grid)
        if i.check_collision(grid,paddle) == 1:
            inactivepowers.append(i)
            powerups.pop(x)
            

def movement(ball,paddle):
    INPUT_CHAR = input_to()
    char = INPUT_CHAR
    ck = check_keys(char)
    if ck==-1:
        clear_screen()
        coloramaReset()
        print(Fore.GREEN+"Thanks for playing!".center(FRAME_WIDTH)+Style.RESET_ALL)
        quit()
    #left
    elif ck == 'a':
        x,y = paddle.get_coord()
        if x <= 2:
            return
        paddle.show_paddle(myboard.grid,x-3,y)
        if ball.spawn == 1:
            a,b = ball.get_coord()
            ball.show(myboard.grid,a-3,b)
    #right
    elif ck == 'd':
        x,y = paddle.get_coord()
        padlen = paddle.get_length()
        if x+padlen >= FRAME_WIDTH-3:
            return
        paddle.show_paddle(myboard.grid,x+3,y)
        if ball.spawn == 1:
            a,b = ball.get_coord()
            ball.show(myboard.grid,a+3,b)
    #start
    elif ck == 'e':
        if ball.spawn == 1 and paddle.check_grab() == 1:
            paddle.set_grab()
            ball.setspawn()
    # grab
    elif ck == ' ':
        if ball.get_catch() == 1 and ball.spawn ==0:
            paddle.set_grab()
        # elif ball.get_catch() == 0 and ball.spawn ==0:
        #     paddle.set_grab()
        