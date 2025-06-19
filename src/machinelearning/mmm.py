#mean, median and mode 
#average, mid point, Common value

import numpy as np
from scipy import stats

y= np.array([25,90,145,35,170,110])
print("mean of Sales: ",np.mean(y))
print("median of Sales: ",np.median(y))
print("mode of Sales: ",stats.mode(y).mode)

#Standard deviation 
sd = np.std(y)
print("Standard deviation for sales: ",sd) 

#variance

print("variance  for sales: ",sd * sd) 

print("variance  for sales: ",np.var(y)) 

