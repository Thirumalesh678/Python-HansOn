def factorial(num):
	if num == 0 or num ==1:
		return 1
	#recursssion
	return num * factorial(num - 1)

num = int(input("Enter the number"))
if(num <0):
	print("Number cannot be zero!")
else:
	print("factorial of a number is : ",factorial(num))
