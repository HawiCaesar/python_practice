class Animal(object):
	pass


## Dog is a type of Animal
class Dog(Animal):
	def __init__(self, name):
		##
		self.name = name

	def make_sound(self):
		print("Woof")


## Cat is a type of Animal
class Cat(Animal):

	def __init__(self, name):
		##
		self.name = name

	def make_sound(self):
		print("Meow")

## this is a base class, inherits from object
class Person(object):

	def __init__(self, name):
		self.name = name

		self.pet = None

## Employee is a type of Person
class Employee(Person):
	def __init__(self, name, salary):

		super(Employee, self).__init__(name)

		self.salary = salary

## base class, inherits from object
class Fish(object):
	pass


## Salmon is a type of Fish
class Salmon(Fish):
	pass


##Halibut is a type of Fish
class Halibut(Fish):
	pass



## rover is a dog
rover = Dog("Rover")
rover.make_sound()


## satan is a cat
satan = Cat("Satan")
satan.make_sound()


## mary is a person
mary = Person("Mary")


## mary has a pet called satan
mary.pet = satan

##frank is an employee with salary 120000
frank = Employee("Frank", 120000)

frank.pet = rover

## flipper is a type of fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is Halibut
harry = Halibut()




