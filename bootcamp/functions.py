def name_function():
	print('Hello')

name_function()

def say_hello(name="Name"):
	print('Hello '+name)

say_hello("Sally")

result = say_hello('David')

def say_hello(name="Name"):
	return ('Hello '+name)

def add(n1, n2):
	return n1+n2

def dog_check(mystring):
	if 'dog' in mystring:
		return True
	else:
		return False

def dog_check_better(mystring):
	return 'dog' in mystring.lower()