import numpy as np 
from colorama import Fore, Style
def dot_plot(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    grid = np.array((n1+1, n2+1), dtype = str)
    grid[:] = " "
    grid[0:1, 1:] = np.array(list(s2))
    grid[1:, 0:1] = np.array(list(s1)).reshape(n1, 1)
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if grid[i][0] == grid[0][j]: grid[i][j] = Fore.GREEN+"x"+Style.RESET_ALL
    return grid

def print_grid(grid):
    st = ""
    for i in range(grid.shape[1]):
        st += "| " + grid[0][i] + " "
    st += "|\n"
    for i in range(grid.shape[1]):
        st += "|---"
    st += "|\n"
    for i in range(1, grid.shape[0]):
        for j in range(grid.shape[1]):
            st += "| " + grid[i][j] + " "
        st += "|\n"
    print(st)
def mark(grid):
  for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
      if i == grid.shape[0]-1 or j == grid.shape[1]-1:
        break  
      if grid[i][j] == grid[i+1][j+1]:
        x=i
        y=j
        cnt=0
        while True:
          if x==grid.shape[0] or y == grid.shape[1]:
            break
          if grid[x][y] != grid[x+1][y+1]:
            break
          else:
            grid[x][y] = Fore.GREEN+"asdas"+Style.RESET_ALL
            cnt+=1


  return grid
if __name__ == "__main__":
    s1 = "TGGCACACTCACACCACACAGACAGTTA"
    s2 = s1
    grid = dot_plot(s1,s2)
    print_grid(mark(grid))
