class Player():
    """
    Player class
    """
    def __init__(self, x, y):
        self._x = x                 
        self._y = y

    def get_coord(self):
        return self._x, self._y
        
    def set_coord(self,x,y):
        self._x = x
        self._y = y
        
    def show(self,grid,figure,x,y):                  
        for i in range(len(figure)):
            for j in range(len(figure[i])):
                # print(grid[y+i][x+j])
                # if grid[y+i][x+j]!=' ':
                #     continue
                grid[y+i][x+j]=figure[i][j]
