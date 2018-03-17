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

def pig_latin(word):
	vowel_list = ['a', 'e', 'i', 'o', 'u']
	for letter in vowel_list:
		if word[0] == letter:
			vowel_word = word.append('ay')
			return vowel_word
		else:
			first_letter = word.pop(0)
			cons_word = word.append(first_letter)
			final_word = cons_word.append('ay')
			return final_word

