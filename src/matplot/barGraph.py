import numpy as np
import matplotlib.pylab as plt

colorCollection = ["red", "green", "yellow", "magenta", "brown", "purple"]
qty = np.array([25,90,145,35,170,110])

plt.bar(colorCollection,qty,color="blue",edgecolor="black")

plt.xlabel("color")
plt.ylabel("Quantity")

plt.title("sales and week")
plt.show()
