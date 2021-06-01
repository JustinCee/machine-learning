import numpy as np
from numpy import *
j = np.arange(20)

print("Original Array")
print(j)

j_mean = np.mean(j)
print("\nMean: ", j_mean)

j_std = np.std(j)
print("\nStandard deviation: ", j_std)

j_var = np.var(j)
print("\nVariance: ", j_var)

