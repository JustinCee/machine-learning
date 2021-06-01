# importing the below modules so we can calculate the mean, standard deviation and Variance
import numpy as np
from numpy import *
# Below is the range of numbers needed to do the calculations
j = np.arange(20)
# this is to print the array of numbers
print("Original Array")
print(j)
# Below is the calculation and to print the result
j_mean = np.mean(j)
print("\nMean: ", j_mean)
# Below is the calculation and to print the result
j_std = np.std(j)
print("\nStandard deviation: ", j_std)
# Below is the calculation and to print the result
j_var = np.var(j)
print("\nVariance: ", j_var)
