i = 0

numbers = []
x = 6
"""
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i += 1
	print "Numbers now:", numbers
	print "At the bottom i is %d" % i

print "The numbers: "
"""

def whilefunc(i,x,numbers):
	for i in range(0, x):
		print "At the top i is %d" % i
		numbers.append(i)

		#i += x
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


whilefunc(i, x, numbers)
for num in numbers:
	print num
