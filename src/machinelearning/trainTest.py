#Data set

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.random.normal(3, 1,100)
y = np.random.normal(150, 40,100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

polyfit = np.polyfit(train_x,train_y,4)
model = np.poly1d(polyfit)

r2 = r2_score(train_y,model(train_x))
print("R2 :",r2)

line = np.linspace(0,6,100)

print("RRDICTION: ",model(3))

plt.scatter(train_x,train_y,color="red", label='Train Data')
plt.scatter(test_x,test_y,color="blue", label='Test Data')
plt.plot(line, model(line))
plt.show()


