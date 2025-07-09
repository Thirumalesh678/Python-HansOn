import requests as rq
from functools import reduce 

def sendRequest(url="https://fake-json-api.mock.beeceptor.com/users"):
    response = rq.get(url)
    return response

def processResponse(response):
    if response.status_code == 200:
        print("Successfull")
        data = response.json()
        print("data in json: ",data)
    return data

#res = sendRequest()
#print(res)

#data = processResponse(res)

# Arguments 
# url, name, age
# 1,2,3

#*(star) Arguments considering as tuple
def sumNumbers(*arg):
    return sum(arg)

print(sumNumbers(4,5,6,9,8))

#*kvarg

# state : Karnataka, city: Bangalore

def printResponse(**kvargs):
    for key, value in kvargs.items():
        print(f"{key}: {value}")

#printResponse(name="Bharath", age=25)

# Lamda
square  = lambda x: x *x
print(square(5))

#map(), filter(), reduce()

numbers = [1,2,3,4,5,6]
#Square of numbers
squares = list(map(lambda x: x**2, numbers))
print(squares)

#Cubes of numbers
cubes = list(map(lambda x: x**3, numbers))
print(cubes)

#filter
# filter the even numbers out of list
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)

#filter out number which are > 2
greaterThan2 = list(filter(lambda x: x>=2, numbers))
print(greaterThan2)

#reduce

product = reduce(lambda x, y: x+y , numbers)
print(product)

product = reduce(lambda x, y: x*y , numbers)
print(product)
