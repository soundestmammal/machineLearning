# -*- coding: utf-8 -*-

if 3>2:
    print('This is true')

hungry = True

if hungry:
    print('feed me')
else:
    print('Not now, im full')

loc = 'Bank'

if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == "Bank":
    print("You are at the bank")
else:
    print('I do not know much.')
    
name = 'Sammy'

if name == 'Frankie':
    print('Hello Frankie')
elif name == 'Sammi':
    print('Hello Sammi')
else:
    print('What is your name?')

#While loops will continue to execute until condition
    
x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("X is not less than 5")

# Break out of th ecurrent closest loop
    
    
mystring = "This one"
    
for letter in mystring:
    if letter == "a":
        continue
    print(letter)
      
# Continue: goings to the top of the closest englosing loop
    
mystring = "This one"
    
for letter in mystring:
    if letter == "a":
        break
    print(letter)

x = 0

while x < 5:    
    if x == 2:
        break
    print(x)
    x += 1
# pass: does nothing at all

# Useful operators
    
for num in range(0,11,2):
    print(num)

list(range(0,10,2))

index_count = 0
word = 'abcde'
for letter in word:
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1    


for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
    
mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)
    
    
'x' in ['x', 'y', 'z']


'a' in 'a world'    

'mykey' in {'mykey' : 355}    
    
    
d = {'mykey': 345}
345 in d.keys()
345 in d.values()








mylist = [10,20,30]
min(mylist)
max(mylist)    

from random import shuffle    

mylist = [1,2,3,4,5,6,7,8,9]

random_list = shuffle(mylist)
mylist

from random import randint
randint(0,10)

result = input('Enter a number here: ')
print(result)

float(result)

