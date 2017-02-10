import sys

try:
	count = int(sys.argv[1])
except IndexError:
	count = 101

for i in range(1,count):
	print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i)
