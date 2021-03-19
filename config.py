"""
Module for configs
"""
import numpy as np
from colorama import Back,Style,Fore
import os

GAMETIME=350
INPUT_CHAR=''

FRAME_WIDTH = 150
FRAME_HEIGHT = 40  

POWERTIME = 10
SCORE = 0

DEBUG = False
BACK_COLOR = Back.BLACK

PAUSED = False
GRAVITY=5
FALLING_TIME=100
BULLET_SHOOT=0.9
BOMB_SHOOT=2.9
TIME_BUF=0.2

body0 = Fore.LIGHTCYAN_EX+' '+Style.RESET_ALL
body1 = Fore.LIGHTCYAN_EX+'_'+Style.RESET_ALL
body2 = Fore.LIGHTCYAN_EX+'|'+Style.RESET_ALL

basic0 = Back.BLUE+'-'+Style.RESET_ALL
basic1 = Back.BLUE+'|'+Style.RESET_ALL
basic2 = Back.BLUE+' '+Style.RESET_ALL

prem00 = Back.LIGHTGREEN_EX+'-'+Style.RESET_ALL
prem01 = Back.LIGHTGREEN_EX+'|'+Style.RESET_ALL
prem02 = Back.LIGHTGREEN_EX+' '+Style.RESET_ALL  
prem10 = Back.GREEN+'-'+Style.RESET_ALL
prem11 = Back.GREEN+'|'+Style.RESET_ALL
prem12 = Back.GREEN+' '+Style.RESET_ALL 

ultra00 = Back.LIGHTRED_EX+'-'+Style.RESET_ALL
ultra01 = Back.LIGHTRED_EX+'|'+Style.RESET_ALL
ultra02 = Back.LIGHTRED_EX+' '+Style.RESET_ALL  
ultra10 = Back.RED+'-'+Style.RESET_ALL
ultra11 = Back.RED+'|'+Style.RESET_ALL
ultra12 = Back.RED+' '+Style.RESET_ALL  
ultra20 = Back.MAGENTA+'-'+Style.RESET_ALL
ultra21 = Back.MAGENTA+'|'+Style.RESET_ALL
ultra22 = Back.MAGENTA+' '+Style.RESET_ALL  

ex0 = Back.LIGHTCYAN_EX+'-'+Style.RESET_ALL
ex1 = Back.LIGHTRED_EX+'|'+Style.RESET_ALL
ex2 = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL 

solid0 = Back.WHITE+'-'+Style.RESET_ALL
solid1 = Back.WHITE+'|'+Style.RESET_ALL
solid2 = Back.WHITE+' '+Style.RESET_ALL


EXTEND = Fore.LIGHTBLUE_EX+'+'+Style.RESET_ALL
GRAB = Fore.LIGHTBLUE_EX+'()'+Style.RESET_ALL
SHRINK = Fore.LIGHTBLUE_EX+'-'+Style.RESET_ALL
MULTIPLIER = Fore.LIGHTBLUE_EX+'x'+Style.RESET_ALL
THRU = Fore.LIGHTBLUE_EX+'!'+Style.RESET_ALL
FAST = Fore.LIGHTBLUE_EX+'v'+Style.RESET_ALL
SHOOT = Fore.LIGHTBLUE_EX+'^'+Style.RESET_ALL
SHOOT1 = Fore.LIGHTBLUE_EX+'v'+Style.RESET_ALL
BOMB = Fore.LIGHTRED_EX+'@'+Style.RESET_ALL
FIRE = Fore.LIGHTBLUE_EX+'F'+Style.RESET_ALL


BASIC0=[[basic0 for i in range(10)],[basic1 if i == 0 or i == 9 else basic2 for i in range(10)],[basic0 for i in range(10)]]
PREM0=[[prem00 for i in range(10)],[prem01 if i == 0 or i == 9 else prem02 for i in range(10)],[prem00 for i in range(10)]]
PREM1=[[prem10 for i in range(10)],[prem11 if i == 0 or i == 9 else prem12 for i in range(10)],[prem10 for i in range(10)]]
ULTRA0=[[ultra00 for i in range(10)],[ultra01 if i == 0 or i == 9 else ultra02 for i in range(10)],[ultra00 for i in range(10)]]    
ULTRA1=[[ultra10 for i in range(10)],[ultra11 if i == 0 or i == 9 else ultra12 for i in range(10)],[ultra10 for i in range(10)]]
ULTRA2=[[ultra20 for i in range(10)],[ultra21 if i == 0 or i == 9 else ultra22 for i in range(10)],[ultra20 for i in range(10)]]
EXPLODE0=[[ex0 for i in range(10)],[ex1 if i == 0 or i == 9 else ex2 for i in range(10)],[ex0 for i in range(10)]]
SOLID0=[[solid0 for i in range(10)],[solid1 if i == 0 or i == 9 else solid2 for i in range(10)],[solid0 for i in range(10)]]
# [[Back.WHITE+'-','-','-','-','-','-','-','-','-','-'+Style.RESET_ALL],\
#             [Back.WHITE+'|',' ',' ',' ',' ',' ',' ',' ',' ','|'+Style.RESET_ALL],\
#                 [Back.WHITE+'-','-','-','-','-','-','-','-','-','-'+Style.RESET_ALL]]
    #     .---.
    #   _/__~0_\_
    #  (_________)