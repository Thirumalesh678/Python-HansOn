colorCollection = ["red", "green", "yellow", "magenta", "brown", "purple"]

print("Enter color names (type done to finish):")

while True:
	name = input("Enter the color name:")
	if(name.lower() == 'done'):
		break
	colorCollection.append(name)

print("List of names:")

for color in colorCollection:
	print (color)