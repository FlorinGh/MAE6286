# Introducing data types
import numpy as np

a = 5
b = 5.0
c = 'five'
d = [1,2,3]
e = (4,2)
f = np.linspace(0,10,11)

for i in [a, b, c, d, e, f]:
    print type(i)

# The numpy array is the data type that acts as a matrix an can be used 
# in numerical analysis