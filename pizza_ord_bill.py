print("Welcome to the pizza zone")
print("What would be your preferable size?")
size=input("What size of pizza do you want?S,M OR L:")
if size == 'S':
	bill = 15
elif size == 'M':
	bill = 20 
elif size == 'L':
	bill = 25
else:
     print("Wrong order")	
pepperoni=input("Do you want pepperoni on your pizza?Y or N:")
if pepperoni == 'Y' and size == 'M' or size == 'L':
	bill += 3
elif pepperoni == 'Y' and size == 'S':
	bill += 2 
elif pepperoni == 'N':
	pass
else:
	print("Wrong order")
extra_cheese=input("Do you want extra cheese?Y or N:")
if extra_cheese == 'Y':
	bill += 1
elif extra_cheese == 'N':
	pass
else:
	print("Wrong order")

print(f"Your final bill is ready : ${bill}")	












