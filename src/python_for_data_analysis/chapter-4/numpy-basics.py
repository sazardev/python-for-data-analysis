"""
This file is a sample file for python and numpy of how to use ndarrays
in all its forms of arrays
"""

import numpy as np

dataOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arrOne = np.array(dataOne)

print(arrOne)

dataTwo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# This creates a 2D array
arrTwo = np.array(dataTwo)

print(arrTwo)
print(arrTwo.ndim)
print(arrTwo.shape)
print(arrTwo.size)
print(arrTwo.dtype)

# This creates an array with 10 zeros
numbersZero = np.zeros(10)
print("Numbers Zero: ", numbersZero)

# This creates an array with 3 rows and 6 columns
numbersZeroTwo = np.zeros((3, 6))
print("Numbers Zero Two: ", numbersZeroTwo)

# This create an empty array
numbersEmpty = np.empty(10)
print("Numbers Empty: ", numbersEmpty)

# This creates an array with 3 rows and 6 columns
numbersEmptyTwo = np.empty((2, 3, 6))
print("Numbers Empty Two: ", numbersEmptyTwo)


# This creates an array with 10 ones
numbersOne = np.ones(10)
print("Numbers One: ", numbersOne)
