# Homework - module1

import numpy as np

'''
Create a linspace array with 43 elements which spans from 4 to 23
What is the value of the 6th element? (Out to 4 decimal places)'''

array1 = np.linspace(4,23,43)
print round(array1[5],4)

'''
The following code is executed;
How many rows does zeros_array have?'''
ones_array = np.ones( (5,17) ) 
zeros_array = np.zeros( ones_array.shape )
print ones_array
print zeros_array

'''
Given the following code:
Compute sin^3(p/r) in Python.
Enter the second value of your answer array (4 decimal places)'''
p = 7
r = np.array([11.2, 4.7, 6.6])
sin3 = (np.sin(p/r))**3
print round(sin3[1],4)

'''
We used a computational fluid dynamics software package to compute the drag
over a sphere immersed in a flow.
The first thing we do is to perform a grid-refinement study of this problem
and using grid spacings of 0.04, 0.02 and 0.01,
we obtained a drag coefficient of 1.600, 1.500 and 1.475, respectively.

What is the order of convergence of the scheme implemented in the software?'''
f3 = 1.600
f2 = 1.500
f1 = 1.475
r = 2.0
p = np.log((f3-f2)/(f2-f1))/np.log(r)
print 'p = ' + str(round(p,4))
