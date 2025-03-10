age = int(input("Please enter your age:"))
if age >= 0 and age <= 12:
	print("You are a child.")
elif age >= 13 and age <= 19:
	print("You are a teen.")
elif age >= 20 and age <= 64:
	print("You are an adult.")
elif age >= 65:
	print("You are a senior.")
else:
	print("Get out!")