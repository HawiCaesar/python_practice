# for loops and range example


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# the for-loop
for number in the_count:
	print "This is count %d " % number

# for-loop again with fruits list
for fruit in fruits: 
	print "A fruit of type %s " % fruit

# mixed list
for i in change:
	print "I got %r " % i

# building lists, with an empty one
elements = []

for i in range(0, 6):
	print "Adding %d to the list" % i
	# how to add items to a list
	elements.append(i)

for i in elements:
	print "Element is %d " % i


