import os
from game import *
from navbar import Navbar
import numpy as np
game_start = time.time()
disp_time=time.time()
move=1
mynav = Navbar(FRAME_WIDTH)
clear_screen()


if __name__ == "__main__":
    spawn_bricks(5,5,20)
    xx,yy = mypaddle.get_coord()
    x = random.randint(xx+5,xx+mypaddle.get_length()-2)
    balls.append(Ball(x,yy-2))
    balls[0].show(myboard.grid,x,yy-2)

    flag=0
    while True:
        timeleft = GAMETIME - (round(time.time()) - round(game_start))
        if(timeleft <= 0 or mypaddle.lives_left()<=0):
            clear_screen()
            print('GAME OVER!'.center(FRAME_WIDTH)) 
            mynav.print_header(timeleft,mypaddle,bricks_arr)
            quit()
        if(time.time()-disp_time>=0.01):
            cursor_set()
            mynav.print_header(timeleft,mypaddle,bricks_arr)
            droppings(mypaddle,myboard.grid)
            movement(balls[0],mypaddle)

            pad_x,pad_y = mypaddle.get_coord()
            mypaddle.show_paddle(myboard.grid,pad_x,pad_y)
            flag = bricksshow(myboard.grid,bricks_arr,mypaddle)
            
            if(len(bricks_arr)==0 or flag==1):
                clear_screen()
                print('You Win!'.center(FRAME_WIDTH)) 
                mynav.print_header(timeleft,mypaddle,bricks_arr)
                quit()
                
            loseball=[]
            addball=[]

            # Movement of balls
            for idx,val in enumerate(balls):
                # print(val.spawn)
                if val.spawn == 1 and mypaddle.check_grab() == 1:
                    continue
                ball_stat = val.move_ball(myboard.grid,bricks_arr,mypaddle)
                # print(ball_stat)
                x,y=val.get_coord()

                # Ball to remove
                if ball_stat == 6:
                    loseball.append(val)
                    active_powers(time.time()+1000,mypaddle,val,myboard.grid)

                # Multiply ball if powerup active
                if val.get_multiplier() == 1:
                    # val.set_mutiplier()
                    addball.append(Ball(x,y))

                # Ball grabbed by paddle
                elif ball_stat == 5:
                    a,b = mypaddle.get_coord()
                    # val.setspawn()
                    # diff = x-a
                    # val.set_coord(a+diff,y)
                
                # Brick 
                elif ball_stat == 9:
                    dropthabomb(x,y-1)
                    mypaddle.inc_score()
                 
            if loseball:
                remove_ball(loseball,balls,myboard.grid)
            if len(balls) == 0:
                mypaddle.dec_lives()
                a,b = mypaddle.get_coord()
                x = random.randint(a+5,a+mypaddle.get_length())
                addball.append(Ball(x,b-2))
                mypaddle.grab_set()
            if addball:
                add_ball(addball,balls)

            inactive_powers(mypaddle,balls[0],myboard.grid)
            active_powers(time.time(),mypaddle,balls[0],myboard.grid)
            disp_time=time.time()
            myboard.print_board()