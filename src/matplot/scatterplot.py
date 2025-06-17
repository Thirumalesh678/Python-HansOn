import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10)
y = np.random.rand(10)

plt.scatter(x,y, color='orange')
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")

plt.title("Random scatter plot")

plt.show()