# Store the current largest number here.
largest_number = -9999999999

# input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# if the number is not equal to -1, continue.
while number != -1:
	# is number larger than largerst_number?
	if number > largest_number:
		# Yes, update largest_number.
		largest_number = number
	# input the next number.
	number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)
