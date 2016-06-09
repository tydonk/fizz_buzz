import sys

try:
	if (len(sys.argv) > 1):
		cli_input = int(sys.argv[1])
		print("Fizz buzz counting up to " + str(cli_input) + "!")
		for x in range(1,(cli_input + 1)):
			if (x % 3 == 0) and (x % 5 == 0):
				print("fizz buzz")
			elif (x % 3 == 0) and (x % 5 != 0):
				print("fizz")
			elif (x % 5 == 0) and (x % 3 != 0):
				print("buzz")
			else:
				print(x)
	else:
		count_to = int(input("Please provide the number we will count to: "))
		print("Fizz buzz counting up to {}!".format(count_to))
		for x in range(1,(count_to + 1)):
			if (x % 3 == 0) and (x % 5 == 0):
				print("fizz buzz")
			elif (x % 3 == 0) and (x % 5 != 0):
				print("fizz")
			elif (x % 5 == 0) and (x % 3 != 0):
				print("buzz")
			else:
				print(x)
except ValueError:
	print("Sorry, that is not a valid input.  Please enter a number.")
	count_to = int(input("Please provide the number we will count to: "))
	print("Fizz buzz counting up to {}!".format(count_to))
	for x in range(1,(count_to + 1)):
		if (x % 3 == 0) and (x % 5 == 0):
			print("fizz buzz")
		elif (x % 3 == 0) and (x % 5 != 0):
			print("fizz")
		elif (x % 5 == 0) and (x % 3 != 0):
			print("buzz")
		else:
			print(x)