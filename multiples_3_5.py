"""
def check_multiple3(number):
	if number > 0:
		print "%d is not a multiple of 3" % number
"""


v3 = 0
v5 = 0
total = 0


for i in range(0,1000):
	v3 = i%3
	v5 = i%5

	if i%3 == 0:
		print "%d is multiple of 3" % i
		total += i

	elif i%5 == 0:
		print "%d is multiple of 5" % i
		total += i

print "The sum total of multiples 3 and 5 is %d " % total
