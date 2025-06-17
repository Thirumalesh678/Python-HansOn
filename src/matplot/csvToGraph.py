import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df   = pd.read_csv('Colors.csv')
categories = df['colors'].values
qty = np.array(df['Quantity'].values)

plt.bar(categories,qty,color='blue', edgecolor="black")

plt.xlabel("color")
plt.ylabel("Quantity")

plt.title("Quantity of Colors")
plt.show()