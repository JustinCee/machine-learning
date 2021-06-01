import matplotlib.pyplot as plt
import numpy as np

marks = np.array([70, 45, 90, 12])
names = np.array(["Memphis", "Godwin", "Thando", "Thabo"])

plt.bar(names, marks, color="Yellow")
plt.xlabel("Marks")
plt.ylabel("Names")
plt.title("The Marks of Students")

plt.show()
