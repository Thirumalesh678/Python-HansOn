import numpy as np
import matplotlib.pyplot as plt


x = np.random.normal(0.0,5.0,100000)
#p(x) = 1/b-a;
plt.hist(x,100)
plt.show()
