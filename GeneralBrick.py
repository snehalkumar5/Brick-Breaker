class Brick:

    def __init__(self, x, y,pow):
        self._x = x
        self._y = y
        self.__power = pow
    
    def check_power(self):
        return self.__power

    def set_power(self):
        self.__power  ^= self.__power

    def get_coord(self):
        return self._x,self._y
        
    def set_coord(self,x,y):
        self._x = x
        self._y = y
  
    def show(self,grid,figure,x,y):                  
        for i in range(len(figure)):
            for j in range(len(figure[0])):
                grid[y+i][x+j]=figure[i][j]

    def collision(self, grid, figure, obstacle,xvel,yvel):
        hori_ck = 0 if yvel==0 else 2
        vert_ck = 0 if xvel==0 else 2
        k = 0 if vert_ck==0 else 1
        x,y = self.get_coord()
        ret = 0
        if hori_ck>0 and y>0:
            y-=1 
        if vert_ck>0 and x>0:
            x-=1 
        for i in range(len(figure)+hori_ck):
            if i == 0:
                ret = 1
            elif i==1:
                ret = 2
            elif i==2:
                ret = 3
            for j in range(len(figure[0])+vert_ck):
                if grid[y+i][x+j] == obstacle:
                    # print(x,y,i,j)
                    if vert_ck == 0:
                        return ret
                    elif j==0 or j==len(figure[0])+1:
                    #     print('hallelujah')
                        return 2
                    return ret
        return 0
       