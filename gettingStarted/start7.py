# More Numpy: grab, slice and dice
import numpy as np
array = np.array([1, 2, 3, 4, 5])

print array[1]
#print array[6] # Index error

print array[1:4] # doesn't take the forth element
# the lower index is inclusive
# the upper index is exclusive

print array[1:]

print array[2:-1]# omits the last value, when we don't know the length
print array[2:-2]# omits the last two values