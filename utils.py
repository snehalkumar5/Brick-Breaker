"""
Utility functions:
    - clear screen
    - take non-blocking keyinput
    - timer settimeout
"""
import numpy as np
import subprocess as sp
from colorama import Style,Fore

BALL = Fore.LIGHTYELLOW_EX+'O'+Style.RESET_ALL
def clear_screen():
    sp.call('clear', shell=True)

def check_keys(key):
    """
    Validating input keys
    """
    key = key.lower()
    if key == 'q':
        return -1
    if not key in (' ', 'a', 'd', 't', 'w', 'e'):
        return 0
    return key

def cursor_set():
    """
    Reposition cursor to top left of screen
    """
    print("\033[0;0H")

def find_bricks(x,y,check,grid,array):
    bricks=[]
    # print('called')
    for brick in array:
        if brick.health_left() <= 0:
            continue
        a,b = brick.get_coord()
        if a==x and b==y:
            continue
        if y == b and x-10 == a:
            # brick.destroy_health()
            bricks.append(brick)
            if brick.type == 5:
                brick.explode(grid,array)
            continue
        if y == b and x+10 == a:
            # brick.destroy_health()
            bricks.append(brick)
            if brick.type == 5:
                brick.explode(grid,array)
            continue
        if y-3 == b and x-10 == a:
            bricks.append(brick)
            if brick.type == 5:
                brick.explode(grid,array)
            continue
        if y-3 == b and x+10 == a:
            bricks.append(brick)
            if brick.type == 5:
                brick.explode(grid,array)
            continue
        if y+3 == b and x-10 == a:
            bricks.append(brick)
            if brick.type == 5:
                brick.explode(grid,array)
            continue
        if y+3 == b and x+10 == a:
            bricks.append(brick)
            if brick.type == 5:
                brick.explode(grid,array)
            continue   
        if y-3 == b and x == a:
            bricks.append(brick)
            if brick.type == 5:
                brick.explode(grid,array)
            continue
        if y+3 == b and x == a:
            bricks.append(brick)
            if brick.type == 5:
                brick.explode(grid,array)
            continue 
    return bricks