# importing the function below allows you to do the calculations you need to do
import numpy as np
# importing the below module is for the graph
import matplotlib.pyplot as plt
# below is the number and bins needed for the histogram
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
# Below is to print the numbers, bins and results in the Terminal
print("\nNumbers: ", nums)
print("\nBins: ", bins)
print("\nResult", np.histogram(nums, bins))
# Below is the configuration for the histogram
plt.hist(nums, bins=bins, color="yellow")
plt.title("Challenge 2")
plt.show()
