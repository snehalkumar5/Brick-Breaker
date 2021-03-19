import os
from game import *
from navbar import Navbar
import numpy as np
from boss import Boss
game_start = time.time()
disp_time=time.time()
move=1
mynav = Navbar(FRAME_WIDTH)
clear_screen()
store_time=time.time()
next_time=time.time()
chck_time=time.time()
bullet_time=time.time()
bullets=[]

step = 0
if __name__ == "__main__":
    os.system('aplay -q ./sounds/game_start.wav&')
    level=1
    while level>=0:
        clear_screen()
        for i in balls:
            i.clear_ball(myboard.grid)
            del i
        balls.clear()
        balls=[]
        for i in bricks_arr:
            i.del_brick(myboard.grid)
            del i
        bricks_arr.clear()
        bricks_arr=[]
        for i in bullets:
            i.clear_bullet(myboard.grid)
            del i
        bullets.clear()
        bullets=[]
        if level!=3:
            spawn_bricks(5,5,0,level,bricks_arr)
        xx,yy = mypaddle.get_coord()
        x = random.randint(xx+5,xx+mypaddle.get_length()-3)
        balls.append(Ball(x,yy-2,1))
        balls[0].show(myboard.grid,x,yy-2)
        myboss=0
        if level==3:
            myboss = Boss(xx,1)
            myboss.show(myboard.grid,xx,1,bricks_arr)
            os.system('aplay -q ./sounds/boss_music.wav&')
            spawn_bricks(5,8,0,level,bricks_arr)
        endgame=0
        run=True
        # print('new level',level)
        while run==True:
            todrop=0
            flag=0
            time_passed = (round(time.time()) - round(game_start))
            # print(time_passed)
            timeleft = GAMETIME - time_passed
            step=0
            
            if(timeleft <= 0 or mypaddle.lives_left()<=0 or level>3 or endgame==1):
                clear_screen()
                if level>3:
                    print('YOU WIN!'.center(FRAME_WIDTH)) 
                    os.system('aplay -q ./sounds/game_win.wav&')
                    mynav.print_header(timeleft,mypaddle,bricks_arr,level,myboss)
                    quit()    
                print('GAME OVER!'.center(FRAME_WIDTH)) 
                os.system('aplay -q ./sounds/game_over.wav&')
                mynav.print_header(timeleft,mypaddle,bricks_arr,level,myboss)
                quit()
            
            # Spawn bombs
            if myboss!=0:
                if myboss.get_health()<=0:
                    mypaddle.inc_score(1000)
                    endgame=1
                if BOMB_SHOOT <= time.time()-chck_time:
                    x,y=myboss.get_coord()
                    bullets.append(Bullet(x+5,y+3,1))
                    chck_time=time.time()

            # Spawn bullets
            if mypaddle.get_shoot() == 1:
                # print('shooting')
                if BULLET_SHOOT <= time.time()-bullet_time:
                    a,b = mypaddle.get_coord()
                    lent = mypaddle.get_length()
                    os.system('aplay -q ./sounds/shoot.wav&')
                    bullets.append(Bullet(a,b-1,0))
                    bullets.append(Bullet(a+lent-1,b-1,0))
                    bullet_time=time.time()
            loseball=[]
            addball=[]
            # Movement of balls
            if 0.1<=time.time()-next_time <= 0.4:
                for idx,val in enumerate(balls):
                    # print(val.spawn)
                    if val.spawn == 1 and mypaddle.check_grab() == 1:
                        continue
                    ball_stat,rem = val.move_ball(myboard.grid,bricks_arr,mypaddle,myboss)
                    # print(ball_stat)
                    x,y=val.get_coord()

                    # Ball to remove
                    if ball_stat == 6:
                        loseball.append(val)
                        active_powers(time.time()+1000,mypaddle,val,myboard.grid,activepowers)

                    # Multiply ball if powerup active
                    if val.get_multiplier() == 1 and ball_stat==3:
                        xvel=val.get_xvel()
                        yvel=val.get_yvel()
                        addball.append(Ball(x,y,0,xvel,yvel))
                        val.set_multiplier(0)

                    # Ball grabbed by paddle
                    elif ball_stat == 5:
                        a,b = mypaddle.get_coord()
                        # val.setspawn()
                        # diff = x-a
                        # val.set_coord(a+diff,y)
                    
                    # Brick 
                    elif ball_stat == 9:
                        if rem:
                            for i in rem:
                                if bricks_arr[i].check_power()==1:
                                    dropthabomb(x,y-1,powerups)
                                bricks_arr.pop(i)
                        mypaddle.inc_score()
                    
                    elif ball_stat == 3 and val.spawn==0:
                        todrop = 1
                next_time=time.time()
                    
            if loseball:
                remove_ball(loseball,balls,myboard.grid)
            if len(balls) == 0:
                mypaddle.dec_lives()
                a,b = mypaddle.get_coord()
                x = random.randint(a+5,a+mypaddle.get_length())
                addball.append(Ball(x,b-2,1))
                mypaddle.grab_set()
            if addball:
                add_ball(addball,balls)

            inactive_powers(mypaddle,balls[0],myboard.grid,inactivepowers)
            active_powers(time.time(),mypaddle,balls[0],myboard.grid,activepowers)
            pad_x,pad_y = mypaddle.get_coord()
            mypaddle.show_paddle(myboard.grid,pad_x,pad_y)
            run=movement(myboard.grid,balls[0],mypaddle,myboss,level,bullets,bricks_arr)

            if(time.time()-disp_time>=0.1):
                cursor_set()
                mynav.print_header(timeleft,mypaddle,bricks_arr,level,myboss)
                droppings(mypaddle,myboard.grid,balls[0],powerups,bullets,myboss,bricks_arr)

                # FALLING BRICKS
                # if (todrop == 1 and FALLING_TIME <= time.time()-store_time):
                if (todrop == 1 and time_passed>=FALLING_TIME):
                    store_time = time.time()
                    step=1
                    todrop=0
                flag = bricksshow(myboard.grid,bricks_arr,mypaddle,step)
                step=0
                if(len(bricks_arr) == 0 or flag==1 or level>3):
                    clear_screen()
                    print('You Win!'.center(FRAME_WIDTH)) 
                    mynav.print_header(timeleft,mypaddle,bricks_arr,level,myboss)
                    step=0
                    run=False
                disp_time=time.time()
                myboard.print_board()
                if flag == -1:
                    mypaddle.set_lives(0)
            if run == False:
                mypaddle.grab_set()
                level+=1
                active_powers(time.time()+1000,mypaddle,balls[0],myboard.grid,activepowers)
                for i in balls:
                    loseball.append(i)
                if loseball:
                    remove_ball(loseball,balls,myboard.grid)
                loseball.clear()
