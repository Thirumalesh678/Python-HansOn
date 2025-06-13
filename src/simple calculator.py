number=float(input("enter you first var :"))
number2=float(input("enter you first var :"))

#print("A Simple calculator!!!")
 #add,mul,sub,divide,modulos7

operation = input("Enter your choice in the prompt (add,sub,div,mod,mul) :")

if(operation=="add"):
    print("addition")
    print("add results :",(number + number2))

elif(operation=="sub"):
    print("sub")
    print("add results :",(number - number2))

elif(operation=="div"):
    print("div")
    if(number2!=0):
        print("add results :",(number / number2))
    else:
        print("Error ZeroDivisionError:float division by zero!")
        print("run positive value")


elif(operation=="mod"):
    print("modulos")
    print("add results :",(number % number2))

elif(operation=="mul"):
    print("mul")
    print("add results :",(number * number2))
else:
    print("invalid operation")