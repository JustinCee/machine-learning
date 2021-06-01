import numpy as np
import matplotlib.pyplot as plt

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

print("\nNumbers: ", nums)
print("\nBins: ", bins)
print("\nResult", np.histogram(nums, bins))

plt.hist(nums, bins=bins, color="yellow")
plt.title("Challenge 2")
plt.show()
