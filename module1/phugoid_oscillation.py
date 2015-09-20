# Phugoid Oscillation Lecture
import numpy as np
import pylab as pl
pl.ion()

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

u = np.array([z0,b0]) # this matrix has only two values
# u[0] -> z
# u[1] -> b
# these values will change with the time loop iterations

# Initialization of an array that will store the values of altitude
z = np.zeros(N) # this creates a N dimension vector with values of zero 
z[0] = z0 # the first value is the initial altitude

# Time-loop with Euler's method: u(t+dt) = u(t) + dt * u'(t)
for i in range(1,N):
    u = u + dt*np.array([u[1],g*(1-u[0]/zt)])
    z[i] = u[0] # store the value of altitude

# Visualising the results with plots (by pylab)
pl.figure(figsize=(10,4)) # setting the plot size
pl.ylim(40,160)
#pl.thick_params(axis='both', labelsize=14)
pl.xlabel('t', fontsize=14)
pl.ylabel('z', fontsize=14)
pl.plot(t,z,'k-')

