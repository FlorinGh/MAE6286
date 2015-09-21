# Phugoid Oscillation Lecture
import numpy as np
import pylab as pl
pl.ion()

# Initialization of time grid
T = 100.0
dt = 0.025
N = int(T/dt)+1
t = np.linspace(0.0, T, N) # Challenge: makes this with range()
#print t

# Initial conditions
z0 = 100.0 # the initial altitude (the mean value of oscilation)
b0 = 10.0 # upward velocity resulting from gust (this is a convention value)
zt = 100.0 # the same as the initial altitude
g = 9.81 # the gravity acceleration

u = np.array([z0,b0]) # this matrix has only two values
# u[0] -> z
# u[1] -> b
# these values will change with the time loop iterations

# Initialization of an array that will store the values of altitude
z = np.zeros(N) # this creates a N dimension vector with values of zero 
z[0] = z0 # the first value is the initial altitude

# Time-loop with Euler's method: u(t+dt) = u(t) + dt * u'(t)
for n in range(1,N):
    u = u + dt*np.array([u[1],g*(1-u[0]/zt)])
    z[n] = u[0] # store the value of altitude

# Visualising the results with plots (by pylab)
pl.figure(figsize=(10, 5)) # setting the plot size
pl.ylim(40,160) # limits of altitude
pl.xlabel('Time', fontsize=14)
pl.ylabel('Altitude', fontsize=14)
pl.grid(True)
pl.plot(t,z,'k-') # the actual command for plotting

'''
Observations:
- with smaller values of b, the amplitudes of oscillations are smaller
- with higer values of b, the amplitudes are higher
- either way, the frecquency is the same
- using negative values of b makes the phugoid to first decrease in altitude
'''

# Actually there is an exact solution and we want to test the numerical one
w = np.sqrt(g/zt)
A = b0*np.sqrt(zt/g)
B = z0-zt
z_exact = A*np.sin(w*t) + B*np.cos(w*t) + zt

# Plot the exact solution over the numerical one
pl.plot(t,z_exact, 'r--')
pl.legend(['Numerical Solution','Analytical Solution'])

# In the next steps we will calculate the error with the time step
# Time increment array
dt_values = np.array([0.1, 0.05, 0.01, 0.005, 0.001, 0.0001])

# Array that will contain the solution for each grid (time step)
z_values = np.empty_like(dt_values, dtype=np.ndarray)

# Repeat the script above for different values of timesteps and store each
# Vector of elevation in a new line in z_values
for i, dt in enumerate(dt_values):
    N = int(T/dt) + 1 # number of time steps
    t = np.linspace(0.0, T, N)
    
    # creating the initial conditions
    u = np.array([z0,b0])
    z = np.zeros(N)
    z[0] = z0
    
    # creating the time loop with Euler method
    for n in range(1,N):
        u = u + dt*np.array([u[1], g*(1-u[0]/zt)])
        z[n] = u[0]
    
    z_values[i] = z.copy() # storing the results in the line i
    
# To calculate the error we will use a function
def get_error(z,dt):
    """Returns the error relative to analytical solution using L-1 norm.
    
    Parameters
    ----------
    z : array of float
        numerical solution.
    dt : float
        time increment.
        
    Returns
    -------
    err : float
        L_{1} norm of the error with respect to the exact solution.
    """
    N = len(z)
    t = np.linspace(0.0, T, N)
    z_exact = b0*(zt/g)**0.5*np.sin((g/zt)**0.5*t)+\
    (z0-zt)*np.cos((g/zt)**0.5*t) + zt
    
    return dt * np.sum(np.abs(z-z_exact))

# Creating a vector and store in it the errors for each time step
error_values = np.empty_like(dt_values)
for i, dt in enumerate(dt_values):
    error_values[i] = get_error(z_values[i], dt)

# Plotting the error
# The error must decrease with time if the method is convergent
pl.figure(figsize=(10,6))
pl.grid(True)
pl.xlabel('$\Delta t$', fontsize=16)
pl.ylabel('Error', fontsize=16)
pl.loglog(dt_values,error_values, 'ko-') # a log-log plot
pl.axis('equal')

