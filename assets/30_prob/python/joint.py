import numpy as np 

P = np.array([
    [5, 20, 12, 22, 20, 18, 13, 7, 6, 1], 
    [23, 22, 25, 24, 18, 15, 13, 5, 1, 0],
    [15, 20, 30, 24, 26, 17, 16, 7, 2, 1],
    [12, 20, 25, 29, 28, 20, 18, 21, 10, 3],
    [15, 20, 22, 32, 40, 30, 29, 27, 20, 5],
    [19, 22, 25, 27, 35, 39, 42, 29, 25, 7],
    [12, 20, 21, 32, 37, 40, 45, 39, 10, 7],
    [4, 12, 17, 32, 20, 25, 35, 32, 28, 8],
    [3, 7, 3, 12, 15, 15, 20, 31, 30, 10],
    [3, 1, 4, 5, 10, 5, 10, 9, 10, 8]] )

px = np.sum(P, axis = 1)
py = np.sum(P, axis = 0)
print np.sum(P)/20
for i in range(10):
    print str(i+1)+ '/'+ str( px[i])+ ',',