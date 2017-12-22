# shortest path dynamic programming
import numpy as np

def minCost(grid,m,n):

    if m < 0 or n < 0:
        return 1e9
    elif m==0 and n==0:
        return(grid[m,n])
    else:
        t =grid[m,n] + min ( minCost(grid,m-1,n-1), minCost(grid,m-1,n), minCost(grid,m,n-1))
        print("m = ", m, "n = ", n, "cost to go to 0,0 = ", t)
        return t





# min of 3 numbers
def min(x, y, z):
    if (x < y):
        if (x < z):
            return x
        else:
            return z
    else:
        if (y < z):
            return y
        else:
            return z
test = min(2,3,4)
print(test)


grid = np.array([[1,2,1],[3,5,1],[4,4,3]])
# start at index [2,2] and get back to [0,0]
print(grid)
test = minCost(grid,2,2)
print("shortest path = ", test)
