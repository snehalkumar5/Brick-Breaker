"""
Defining input class
"""
import sys
import termios
import tty
import signal

class _getChUnix:
    """
    Class to get input
    """

    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    """
    Used to handle timeouts
    """
    raise AlarmException


def input_to(getch,timeout=0.1):
    """Taking input from user."""
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = _getChUnix()()
        signal.alarm(0)
        return text
    except AlarmException:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None