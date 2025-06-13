num = int(input("Enter the number"))

if num == 0:
	print("Number cannot be zero!")

result =1
for i in range(1, num+1):
	result *= i

print("factorial of a number is : ",result)