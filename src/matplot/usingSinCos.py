import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0, 2 * np.pi, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.plot(x, sin_y,label="sin(x)",color="red")
plt.plot(x, cos_y,label="cos(x)",color="black")


plt.xlabel("x-Axis")
plt.ylabel("y-Axis")

plt.title("sine and Cosine plot")
plt.show()


