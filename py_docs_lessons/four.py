# -*- coding: utf-8 -*-

# Besides the while startment just introduced, Python knows the usual control flow statements known from other languages with some twists.
x = str(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    
# Let's try and do this

x = str(input("Where do you attend college: "))
if x == "Hofstra":
    print("Go Pride")
elif x == "Alabama":
    print("Roll Tide")
elif x == "Farmingdale State College":
    print('Go Rams!')
else:
    print("I don't know that school")
    

    
    
# Section 4.2 for Statements

# Measure some strings

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Exponential

power = [2, 3, 4, 5, 6]\

for p in power:
    step = p * p
    print(step)
    
# 4.3 The range function

for i in range(5, 100):
    print(i)

def reverse(str):
    background = str[::-1]
    print(background)
    
reverse("hello")

def fact(num):
    return num

fact(5)









    
    