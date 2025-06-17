import numpy as np

#create an array
collection = [1,2,3,4]

array = np.array(collection)

print("collection ",collection)
print("numpy array ",array)

collection1 = [50,60,70,80]
array1 = np.array(collection1)
print("array1 ",array1)
sum = array+array1
print("array sum: ",sum)

mean = np.mean(array)
print("mean: ",mean)
print("mean a1 ",np.mean(array1))

#2d array
matrix = np.array([collection,collection1])
print("2D array: ",matrix)

squares = np.square(array)
print("squares array: ",squares)

sc = array *2
print("scaled Array: ",sc)

array5 = array1 * 5
print("scaled array: ",array5)

averageVal = np.average(array5)
print("average of array: ",averageVal)
meanVal = np.average(array5)
print("mean of array: ",meanVal)

