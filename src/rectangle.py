def rectangle(l,b,area,indicator):
	if indicator == 'a':
		return l * b
	elif indicator == 'l':
		return area/b
	elif indicator == 'p':
		return 2*(l + b)
	else:
		print("Wrong indicator")



print("Area of the rectangle is: ",rectangle(67,5,0,'a'))
print("Length of the rectangle is: ",rectangle(0,67,rectangle(67,5,0,'a'),'l'))
print("Perimeter of the rectangle is: ",rectangle(rectangle(0,67,335,'l'),67,335,'p'))