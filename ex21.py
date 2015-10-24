def add(a, b):
	print "Adding %d + %d" %(a, b)
	return a + b

def subtract(a, b):
	print "subtracting %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "dividing %d / %d" %(a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age,height,weight,iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height,multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# Answer above was -4391

new_what = subtract(age, add(height, multiply(weight, divide(iq, 2))))

print "This is the new what ", new_what, "Iz how?"

# Answer above was -4539

new_what2 = add(age, divide(height, subtract(weight, multiply(iq, 2))))

print "This is the 3rd new what,Okay second: %d" % new_what2

# Answer above was 35