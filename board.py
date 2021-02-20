from config import *
class Board:

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.grid = []
        self.__flag = 0

    def create_board(self):
        self.grid = [[" " for j in range(self.__cols)] for i in range(self.__rows)]
        for i in range(self.__rows):
            self.grid[i][0]="|"
            self.grid[i][self.__cols-1]="|"
        # self.grid = ["|" for j in range(self.__rows)]

        
    def print_board(self):
            for i in range(self.__rows):
                for j in range (self.__cols):
                    # print(Back.LIGHTBLACK_EX +self.grid[i][j] + Back.RESET, end='')
                    print(self.grid[i][j],end='')
                print()