import numpy as np
import matplotlib.pyplot as plt

x = [2, 4, 6, 8,10, 12, 14, 16,18,20, 22,24]
y = [25, 90,145,35,176, 110, 77,98,45,39,125, 26]

polyfit = np.polyfit(x,y,3)
#print(polyfit)
model = np.poly1d(polyfit)
#print(model)
line = np.linspace(1,22,100)
#print(line)
plt.scatter(x,y)
plt.plot(line, model(line))

plt.show()