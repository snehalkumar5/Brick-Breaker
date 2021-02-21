"""
Module for configs
"""
import numpy as np
from colorama import Back,Style,Fore
import os

GAMETIME=120
INPUT_CHAR=''

FRAME_WIDTH = 150
FRAME_HEIGHT = 40  

POWERTIME = 10
SCORE = 0

DEBUG = False
BACK_COLOR = Back.BLACK

PAUSED = False

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

EXTEND = Fore.LIGHTBLUE_EX+'+'+Style.RESET_ALL
GRAB = Fore.LIGHTBLUE_EX+'()'+Style.RESET_ALL
SHRINK = Fore.LIGHTBLUE_EX+'-'+Style.RESET_ALL
MULTIPLIER = Fore.LIGHTBLUE_EX+'x'+Style.RESET_ALL
THRU = Fore.LIGHTBLUE_EX+'!'+Style.RESET_ALL
FAST = Fore.LIGHTBLUE_EX+'v'+Style.RESET_ALL

