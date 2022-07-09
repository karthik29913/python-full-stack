class Dog:
	attr1 = "student"
	# Instance attribute
	def __init__(self, name):
		self.name = name

# Driver code
# Object instantiation
Rodger = Dog("good boy")
Tommy = Dog("karthik")

# Accessing class attributes
print("karthik is a {}".format(Rodger.__class__.attr1))
print("karthik is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("I am {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
