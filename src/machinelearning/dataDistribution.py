import numpy as np
import sys
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0,100000)
plt.hist(x, 100)

plt.savefig('Uniform Distribution.pdf', dpi=200,format='pdf', bbox_inches='tight')
plt.show()