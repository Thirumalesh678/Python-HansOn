import numpy as np

import matplotlib.pyplot as plt

#Data

array1 = [1,2,3,4,5,6,7,8]
x = np.array(array1)
y = np.array(array1) * 5 #np.square(x)
print("X value: ",x)
print("Y value: ",y)

#Line Plot

plt.plot(x,y,label='y = x^2', color="black")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Squared Array")
plt.legend()
plt.grid(True)
plt.show()

#scatter plot
'''
plt.scatter(x,y,color="purple", label="Data Points")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("SquScatter Plot")
plt.legend()
plt.show()'''




