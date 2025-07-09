import numpy as np
import matplotlib.pyplot as plt

colorCollection = ["red", "green", "yellow", "magenta", "brown", "purple"]
qty = np.array([25,90,145,35,170,110])

plt.pie(qty,labels=colorCollection, autopct='%1.2f%%')
plt.show()