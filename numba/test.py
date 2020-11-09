import numpy as np
from numba import jit
import time 

array1 = np.random.rand(1000,1000,1000)
#array2 = np.random.rand(1000,1000,1000)

@jit(parallel=True, nopython=True)
def multiply(a1, a2):
    return np.multiply(a1, a2)

startTime = time.time()
for _ in range(20):
    multiply(array1, array1)
executionTime = (time.time() - startTime)
print('Execution time in seconds with jit: ' + str(executionTime))

def multiply(a1, a2):
    return np.multiply(a1, a2)

startTime = time.time()
for _ in range(20):
    multiply(array1, array1)
executionTime = (time.time() - startTime)
print('Execution time in seconds without jit: ' + str(executionTime))
