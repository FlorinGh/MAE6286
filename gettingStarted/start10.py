# Naming and adressing
import numpy as np

a  = np.array([1, 2, 3])
b = a

b[1] = 7 # changes the second element of into 7 ???

print a
print b
# wtf ???



c = np.array([4, 5, 6])
d = c.copy()

d[1] = 7

print c
print d