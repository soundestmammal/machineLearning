# -*- coding: utf-8 -*-

# I am starting Section 3 of the couse I am taking. This will solidfy Py understanding

#Video 11 Introduction to Python Data Types

"""
Data types
Integers int whole numbers
Floating point float number with a decimal
Strings str ordered sequence of characters "hello"

Data Structures
lists list Ordered sequence of objects 
dictionaries dict unordered key:value pairs: {}
tuples tup ordered immutable sequence of objects: {10 'hello'}
sets set unordered colletion of unique objects
Booleans bool logical value indicating True or False

"""

# Video 12 Numbers

"""

There are two main number types we will work with:
    Indegers which are
    Floating points
    
"""

2+1#Add
2-1#Sub
2*2#Mult
3/2#Divide
7%4#modulo

# If mod 2 is not 0 then the number is odd If 0 then it is even

2**3 # = 8

# Can do order of operations. pemdas

0.1+0.2-0.3

# Lecture 14

#Python uses dynamic typing
#This means that you can reassign variables to different data types.

my_dogs = 2
my_dogs = ['sam', 'robert']

#Faster development time.

#Negatives:
#May result in buds for unexpected data types!
#You nee dto be aware of type()

a = 5
a + a
a = a + a

type(a)
type(30.1)

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)

# Introduction to Strings

# Strings are dwquences of characters, using the syntax of either single quotes or double quoes


'hello'
"hello"
'This is also a string'
"i'm going on a run"

print('Hello")
print('Hello world')

print('Hello \n world')

len(words)
len('words')

#Lecture 16

mystring= "hello world"
print('hello world')

First
mystring[0]

mystring[-2]

#slicing
mystring
mystring[2:]

mystring[:-2]

mystring[3:7]