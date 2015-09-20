# Phugoid Oscillation Lecture
import numpy as np
from matplotlib import pyplot as pp

# Initialization of time grid
T = 100.0
dt = 0.02
N = int(T/dt)+1
t = np.linspace(0.0, T, N) # Challenge: makes this with range()
#print t

# Initial conditions
z0 = 100.0 # the initial altitude (the mean value of oscilation)
b0 = 10.0 # upward velocity resulting from gust (this is a convention value)
zt = 100.0 # the same velocity
g = 9.81 # the gravity acceleration

u = np.array([z0,b0])

# Initialization of an array that will store the values of altitude
z = np.zeros(N)
z[0] = z0 # the first value is the initial altitude








