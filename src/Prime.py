print("Welcome to prime number check!")

varNum=int(input("Enter your number "))
for i in range(2,varNum):
    if(varNum % i==0):
        print("It's is a prime")
        break
    else:
        print("it's not a prime")
        break
