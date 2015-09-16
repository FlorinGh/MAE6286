#This script plots the flight path of the phugoid using the Lanchester model

import numpy as np
import pylab as pl


def radius_of_curvature(z, zt, C):
    """ Returns the radius of curvature of the flight path at a given point
    
    Inputs
    z (float): current depth below the reference horizontal line
    zt (float): initial depth below the reference horizontal line
    C (float): constant of integration
    
    Outputs
    radius (float): radius of curvature
    """
    
    return zt / (1/3.0 - 0.5*C*(zt/z)**1.5)


def rotate(x, z, xCenter, zCenter, angle):
    """ Returns the new position of the phugoid
    
    Inputs
    x (float): previous x coordinate
    z (float): previous z coordinate
    xCenter (float): x coordinate of the center of rotation
    zCenter (float): z coordinate of the center of rotation
    angle (float): angle of rotation
    
    Outputs
    xCenter_new (float): the new x coordinate of the center of rotation
    zCenter_new (float): the new z coordinate of the center of rotation    
    """
    
    dx = x - xCenter
    dz = z - zCenter
    xNew = dx*np.cos(angle) + dz*np.sin(angle)
    zNew = -dx*np.sin(angle) + dz*np.cos(angle)
    
    return xCenter + xNew, zCenter + zNew
    
    
def plot_flight_path(zt, z0, theta0):
    """Plots the flight path
    
    Inputs
    zt (float): trim height of the glider
    z0 (float): initial height of the glider
    theta0 (float): initial orientation of the glider
    
    Output
    None: None (the plot)    
    """
    N = 1000 # resolution
    z = np.zeros(N) # array for height
    x = np.zeros(N) # array for x coordinate
    
    # Initial conditions
    z[0] = z0
    x[0] = 0.
    theta = theta0
    
    # Compute the intergration constant C
    C = (np.cos(theta)-(1/3.)*z0/zt) / (zt/z0)**0.5
    
    # Local incremental distance - flight path resolution
    ds = 1.
    
    # Compute the trajectory coordinates and store them in z and x arrays
    for i in range(1,N):
        normal = np.array([np.cos(theta+np.pi/2), -np.sin(theta+np.pi/2)])
        R = radius_of_curvature(z[i-1],zt,C)
        center = np.array([x[i-1]+normal[0]*R, z[i-1]+normal[1]*R])
        dtheta = ds/R
        x[i], z[i] = rotate(x[i-1], z[i-1], center[0], center[1], dtheta)
        theta = theta + dtheta
    
    # Make a plot for the two vectors
    pl.figure(figsize=(10,6))
    pl.plot(x,-z, color='k', ls='-', lw=2.0)
    pl.axis('equal')
    pl.title("Flight path for")
    pl.xlabel("$x$", fontsize=18)
    pl.ylabel("$z$", fontsize=18)
    pl.legend()
    pl.show()
    