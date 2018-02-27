# This is part one of learning about how objects work in Python.
# Python is a class based language. This is different that other languages such as javascript.

# How to define a class?

class car:
	pass

car = Vehicle()
print(car)

# Here car is an object (or instance) of the class Vehicle

#Vehicle class has 4 attributes:
# Number of wheels
# Type of tank
# Seating capacity
# Maximum Velocity

class Vehicle:
	def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
		self.number_of_wheels = number_of_wheels
		self.type_of_tank = type_of_tank
		self.seating_capacity = seating_capacity
		self.maximum_velocity = maximum_velocity

class Person:
	def __init__(first_name, last_name, address):
		self.number_of_wheels


#Above we used the init method. We call it a constructor method.

#When we create the vehicle object, we can define this attributes.

# Let's create a tesla model s.

tesla_model_s = Vehicle(4, 'electric', 5, 250)

