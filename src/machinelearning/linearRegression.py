from scipy import stats
import matplotlib.pyplot as plt

x = [4,6,7,5,2,3,8,9,4,5,7,8]
y = [25, 90,145,35,176, 110, 77,98,45,39,125, 26]

slope, intercept, r, p, str_err = stats.linregress(x,y)

def slopeFun(x):
    return slope * x +intercept

model = list(map(slopeFun, x))

plt.scatter(x, y)
plt.plot(x,model)

plt.show()