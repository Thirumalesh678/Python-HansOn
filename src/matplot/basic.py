import numpy as np
import matplotlib.pyplot  as plt


x = np.array([1,2,3,4,5])
y = x**2

plt.plot(x,y)
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")

plt.title("Line plot")
plt.show()

