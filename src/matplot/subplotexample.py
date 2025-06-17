import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5])
y = np.array([25,90,145,35,170,110])

plt.subplot(1,2,1)
plt.plot(x,y, marker ='o')


x = np.array([0,1,2,3,4,5])
y = np.array([35,60,45,25,70,90])

plt.subplot(1,2,2)
plt.plot(x,y,marker ='o')

x = np.array([0,1,2,3,4,5])
y = np.array([35,40,45,25,70,90])

plt.subplot(1,2,2)
plt.plot(x,y,marker ='o')



plt.show()