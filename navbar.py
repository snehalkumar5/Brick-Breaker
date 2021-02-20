from colorama import Fore,Back,Style
from config import FRAME_WIDTH
class Navbar():
    """
    Dashboard display
    """
    def __init__(self,scr):
        self._screen = scr

    def print_header(self,newtime, paddle, bricksarr):
        dash = str("LIVES LEFT: "+str(paddle.lives_left()) + "  SCORE:" + str(paddle.show_score())+"  TIME: " + str(newtime))
        print(Fore.BLACK + Back.YELLOW + "               ".center(FRAME_WIDTH)+Style.RESET_ALL)
        print(Fore.BLACK + Back.YELLOW + "BRICK BREAKER".center(FRAME_WIDTH)+Style.RESET_ALL)
        print(Fore.BLACK + Back.YELLOW + "               ".center(FRAME_WIDTH)+Style.RESET_ALL)
        print(Fore.WHITE + Back.CYAN + dash.center(FRAME_WIDTH)+Style.RESET_ALL)

