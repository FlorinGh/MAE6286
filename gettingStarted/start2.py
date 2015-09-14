# Introducing Matplotlib
from matplotlib import pyplot as pp

# Create an array of numbers from 0 to 5 with Numpy
import numpy as np
xx = np.linspace(0,5,11)
yy = xx**2

# Creating a plot
pp.plot(xx,yy)

# Showing the plot
pp.show()
