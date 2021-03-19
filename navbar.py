from colorama import Fore,Back,Style
from config import FRAME_WIDTH
class Navbar():
    """
    Dashboard display
    """
    def __init__(self,scr):
        self._screen = scr

    def print_header(self,newtime, paddle, bricksarr,level,boss):
        level = min(3,level)
        dash = str("LIVES LEFT: "+str(paddle.lives_left()) + "  SCORE:" + str(paddle.show_score())+"  TIME: " + str(newtime)+ "  LEVEL:" + str(level))
        if boss!=0:
            print(Fore.BLACK + Back.YELLOW + ("BOSS HEALTH: " + str(boss.get_health())).ljust(FRAME_WIDTH)+Style.RESET_ALL)
        else:
            print(Fore.BLACK + Back.YELLOW + "  ".center(FRAME_WIDTH)+Style.RESET_ALL)
        if paddle.get_shoot()==1:
            print(Fore.BLACK + Back.YELLOW + ("Shoot time left: " + str(paddle.get_shoot_time())).ljust(FRAME_WIDTH)+Style.RESET_ALL)
        else:
            print(Fore.BLACK + Back.YELLOW + "  ".center(FRAME_WIDTH)+Style.RESET_ALL)
        print(Fore.BLACK + Back.YELLOW + "BRICK BREAKER".center(FRAME_WIDTH)+Style.RESET_ALL)
        print(Fore.BLACK + Back.YELLOW + "               ".center(FRAME_WIDTH)+Style.RESET_ALL)
        print(Fore.WHITE + Back.CYAN + dash.center(FRAME_WIDTH)+Style.RESET_ALL)

