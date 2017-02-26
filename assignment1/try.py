import numpy as np 

x = np.array([[1,3],[3,4]])
N = x.shape[0]
x = np.max(x, axis=1).reshape(N, 1)
print(x)