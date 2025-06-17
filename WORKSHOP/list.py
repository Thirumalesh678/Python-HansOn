furniture = ["sofa","desk","wardrobe"]

collector=input("enter your furniture to add to this collection: ")
#append to add the collection / list 
furniture.append(collector)
print(furniture)

for i in furniture:
    print(i)

furniture.remove("desk")
print(furniture)



colors =["safron","white","green"]
colors.clear()
color = input("enter your color to add to this collection: ")
colors.append(color)
print(colors) 

#colors.remove(color)
#print(colors)