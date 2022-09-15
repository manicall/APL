import numpy as np

M3 = np.array([[2., 3., 5.], 
               [3., 7., 4.], 
               [1., 2., 2.]])

v3 = np.array([10., 3., 3.])

x = np.linalg.solve(M3, v3)
print(x)
print(np.dot(M3, x))

