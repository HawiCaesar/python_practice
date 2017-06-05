def isDivisibleBy_7(number):
	if number < 0:
		return isDivisibleBy_7( -number )
 
	##Base case
	if number==0 or number ==7:
		return 1
 
 
	if number <10:
		return 0
 
	return isDivisibleBy_7( int(number/10) - (2*(number%10) ) )
 
 
 
def isDivisibleBy_5(number):
	if number % 5 != 0:
		return 1
	
 
for i in range(2000,3201):
	if isDivisibleBy_7(i) == 1 and isDivisibleBy_5(i) == 1:
		print i,



"""
class StringClass(object):
	def __init__(self):
		self.input_string = ""

	def getString(self):
		self.input_string = raw_input("Please enter a string ")
		return self.input_string

	def printString(self):
		return self.input_string.upper()

	def test_getString(self):
		output_string = self.getString()
		
		try:
			i = int(output_string)
			print("The value %d is NOT a string" %i)
		except ValueError:
			print("The value is a string. Good")
		

	def test_printString(self):
		output = self.printString()
		assert(output.isupper()), "Cant capitalise the string"


a = StringClass()

a.test_getString()
a.test_printString()

a.test_getString()
a.test_printString()
"""




