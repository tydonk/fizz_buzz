import sys

cli_input = 0
count_to = 0

if (len(sys.argv) > 1):
	try:
		cli_input = int(sys.argv[1])
	except ValueError:
		print("That is not a number, please run the game again and enter a number.")
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
	try:
		count_to = int(input("Please provide the number we will count to: "))
	except NameError:
		print("That is not a number, please run the game again and enter a number.")
	except ValueError:
		print("That is not a number, please run the game again and enter a number.")
	print("Fizz buzz counting up to " + str(count_to) + "!")
	for x in range(1,(count_to + 1)):
		if (x % 3 == 0) and (x % 5 == 0):
			print("fizz buzz")
		elif (x % 3 == 0) and (x % 5 != 0):
			print("fizz")
		elif (x % 5 == 0) and (x % 3 != 0):
			print("buzz")
		else:
			print(x)