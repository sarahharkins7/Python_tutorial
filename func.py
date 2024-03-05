'''
This script demonstrates some mutable/immutable differences, and functions
'''

import numpy as np

# This is how you create a function:
def my_function(array1, array2):
    '''
    This is the doc string for the function. Good doc strings say briefly what
    the purpose of the function is, what it takes in, and what it spits out.

    Arguments:
        array1: 2D ndarray
        array2: 2D ndarray

    Returns:
        ndarray
    '''

    # When mutable data types are passed into a function, they are passed by
    #   reference. That means that the actual array is passed in, not a copy - 
    #   if you alter the array in the function, it is altered outside the function!
    #   This is faster than creating a true copy, but can result in hard to debug
    #   errors, especially if you alter the array by accident.

    array1[0,0] = 0
    array2_cpy = np.array(array2) # remember you need a true copy!
    array2_cpy = array2_cpy * 5

    return array2_cpy

# Now we test out the function...
A = np.eye(3) # 3x3 identity matrix
B = np.ones((3,3)) # 3x3 array of ones

print('A before function:')
print(A)
print('B before function:')
print(B)
print('------------------')

C = my_function(A, B)

print('A after function:')
print(A)
print('B after function:')
print(B)
print('Array returned by function:')
print(C)


# There are other, somewhat more complicated "gotchas" in Python, but not very many.
# Google "Python gotchas" and read about them!