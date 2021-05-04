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
from bullet import Bullet

myboard = Board(FRAME_HEIGHT,FRAME_WIDTH)
myboard.create_board()
def next_level(level):
    level+=1
    return False

mypaddle = Paddle(70,36)
xx,yy = mypaddle.get_coord()
x = random.randint(xx,xx+mypaddle.get_length())
# myball = Ball(x,yy-1)
balls=[]
bricks_arr = []
def add_ball(addball,balls):
    for i in addball:
        balls.append(i)

def remove_ball(removeballs,balls,grid):
    for i in removeballs:
        i.clear_ball(grid)
        balls.remove(i)
        # print('ee')
        del i
    removeballs.clear()


def balls_show(grid,arr,brick_arr,paddle):
    for i in arr:
        i.move_ball(grid,brick_arr,paddle)

BRICKSNUM=0
BRICKSLEFT=0
def spawn_bricks(x,y,step,level,bricks_arr):
    # print('step:, y:',step,y)
    if level>3:
        return
    if y >= FRAME_HEIGHT-10:
        return
    if level == 1:

        if x >= FRAME_WIDTH-20:
            y = y+3
            x = 5
            # step += 75
            if y%2 == 0:
                x = 15
                # x = 1
        if y >= 15:
            return 
        pp = 1
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
            elif x < FRAME_WIDTH - 110:
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
    
        bricks_arr.append(mybricks)
        next_x = x + 20   
        next_y = y
        if y==8:
            next_x = x + 10   

        spawn_bricks(next_x,next_y,step,level,bricks_arr)
        return
    
    if level == 2:

        if x >= FRAME_WIDTH-20:
            y += 3
            x = 5
            # step += 75
            # if y%2 == 0:
                # x = 15
                # x = 1
        if y >= 15:
            return 
        pp = 1
        if y == 5:
            mybricks = BasicBrick(x,y,pp)
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

        bricks_arr.append(mybricks)
        next_x = x + 10  
        next_y = y
        # if y==8:
        #     next_x = x + 10   

        spawn_bricks(next_x,next_y,step,level,bricks_arr)
        return
    
    elif level == 3:
        if x >= FRAME_WIDTH-10:
            y += 3
            x = 5
            # step += 75
            # if y%2 == 0:
            #     x = 15
                # x = 1
        if y >= 21:
            return 
        pp=1
        if y == 5:
            mybricks = BasicBrick(x,y,pp)
            # mybricks.show_brick(myboard.grid,x,y,0)
        elif y == 11:
            if x < FRAME_WIDTH/8:
                mybricks = SolidBrick(x,y,pp)
            elif x <FRAME_WIDTH/4:
                mybricks = UltraBrick(x,y,pp)
            elif x < FRAME_WIDTH - 120:
                mybricks = UltraBrick(x,y,pp)
            elif x < FRAME_WIDTH -110:
                mybricks = UltraBrick(x,y,pp)
            elif x < FRAME_WIDTH - 70:
                mybricks = BasicBrick(x,y,pp)
            elif x < FRAME_WIDTH - 60:
                mybricks = BasicBrick(x,y,pp)
            elif x < FRAME_WIDTH - 50:
                mybricks = BasicBrick(x,y,pp)
            elif x < FRAME_WIDTH - 40:
                mybricks = UltraBrick(x,y,pp)
            elif x < FRAME_WIDTH - 30:
                mybricks = BasicBrick(x,y,pp)
            else: 
                mybricks = SolidBrick(x,y,pp)

        elif y == 14:
            mybricks = PrideBrick(x,y,pp)
        elif y==17:
            mybricks = PremiumBrick(x,y,pp)
        elif y==20:
            mybricks = BasicBrick(x,y,pp)
        if mybricks:
            bricks_arr.append(mybricks)
        next_x = x + 20   
        next_y = y
        if y==17 or y==20:
            next_x = x + 10   

        spawn_bricks(next_x,next_y,step,level,bricks_arr)
        return

def bricksshow(grid,arr,paddle,step):
    flag = 1
    drop = 0
    toremove = []
    for _,val in enumerate(arr):
        if val.type!=4:
            flag=0
        if val.type == 6:
            x,y=val.get_coord()
            val.show_brick(grid,x,y+step,0)
            continue
        if val.health_left() <= 0:
            val.del_brick(grid)
            toremove.append(val)
            paddle.inc_score()
            continue
        x,y=val.get_coord()
        drop = val.show_brick(grid,x,y+step,0)
        if drop == 1:
            return -1
    for _,val in enumerate(toremove):
        arr.remove(val)
    # print(flag)
    return flag
    
powerups = [] # spawned
activepowers = [] # activated
inactivepowers = [] # not activated yet

def dropthabomb(x,y,powerups):
    if random.random()<=0.3:
        return
    rand = random.randint(0,8)
    if rand >= 7:
        # power = Power_Multiplier(x,y,time.time())
        power = Power_Shoot(x,y,time.time())
    elif rand >= 6:
        power = Power_Extend(x,y,time.time())
    elif rand >= 5:
        power = Power_Shrink(x,y,time.time())
    elif rand >= 4:
        power = Power_Fast(x,y,time.time())
    elif rand >= 3:
        power = Power_Grab(x,y,time.time())
    elif rand >= 2:
        power = Power_Thru(x,y,time.time())
    elif rand >= 1:
        power = Power_Multiplier(x,y,time.time())
    else: 
        power = Power_Fire(x,y,time.time())
    powerups.append(power)
    

def active_powers(cur_time,paddle,ball,grid,activearray):
    rem = []
    for x,i in enumerate(activearray):
        if int(cur_time-i.start_time) > POWERTIME:
            if i.deactivate(paddle,ball,grid) == 1:
                activearray.pop(x)    
                return
                # rem.append(i)
    for i in rem:
        activearray.remove(i)

def inactive_powers(paddle,ball,grid,inactivearray):
    rem = []
    for x,i in enumerate(inactivearray):
        if i.activate(paddle,ball,grid) == 1:
            os.system('aplay -q ./sounds/power_up.wav&')
            activepowers.append(i)
            rem.append(i)
            # inactivepowers.pop(x)
    for i in rem:
        inactivearray.remove(i)

def droppings(paddle,grid,ball,powerarray,bullets,boss,bricks):
    rem = []
    remo = []
    for x,i in enumerate(powerarray):
        i.display(grid,ball)
        if i.dead == 1:
            rem.append(i)
        if i.check_collision(grid,paddle) == 1:
            inactivepowers.append(i)
            rem.append(i)
            # powerups.pop(x)
    for i in rem:
        powerarray.remove(i)
    for i in bullets:
        if i.active == 0:
            i.clear_bullet(grid)
            remo.append(i)
            continue
        if i.move_bullet(grid,paddle,boss,bricks) != 0:
            i.active=0
            i.clear_bullet(grid)
            remo.append(i)
    for i in remo:
        bullets.remove(i)            

def movement(grid,ball,paddle,boss,level,bullets,brickarr):
    INPUT_CHAR = input_to()
    char = INPUT_CHAR
    ck = check_keys(char)
    if ck==-1:
        clear_screen()
        coloramaReset()
        os.system('aplay -q ./sounds/game_over.wav&')
        print(Fore.GREEN+"Thanks for playing!".center(FRAME_WIDTH)+Style.RESET_ALL)
        quit()
    #left
    elif ck == 'a':
        x,y = paddle.get_coord()
        if x <= 2:
            return True
        paddle.show_paddle(grid,x-3,y)
        if boss!=0:
            boss.show(grid,x-3,1, brickarr)
        if ball.spawn == 1:
            a,b = ball.get_coord()
            ball.show(grid,a-3,b)
        return True
    #right
    elif ck == 'd':
        x,y = paddle.get_coord()
        padlen = paddle.get_length()
        if x+padlen >= FRAME_WIDTH-3:
            return True
        paddle.show_paddle(grid,x+3,y)
        if boss!=0:
            boss.show(grid,x+3,1, brickarr)
        if ball.spawn == 1:
            a,b = ball.get_coord()
            ball.show(myboard.grid,a+3,b)
        return True
    #start
    elif ck == 'e':
        if ball.spawn == 1 and paddle.check_grab() == 1:
            paddle.set_grab()
            ball.setspawn()
        return True
    # grab
    elif ck == ' ':
        if ball.get_catch() == 1 and ball.spawn ==0:
            paddle.set_grab()
        # elif ball.get_catch() == 0 and ball.spawn ==0:
        #     paddle.set_grab()
        return True
    elif ck == 't':
        next_level(level)
        return False
    # elif ck == 'k':
    #     if paddle.get_shoot()==1:
    #         x,y = paddle.get_coord()
    #         len = paddle.get_length()
    #         bullets.append(Bullet(x,y-1,0))
    #         bullets.append(Bullet(x+len-1,y-1,0))
    return True
        