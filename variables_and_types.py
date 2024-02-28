#!/usr/bin/env python3
#Python Variables and Types tutorial by Nifemni Olafisan
'''This script introduces more advanced data structures and the concept of type hints. 
Experiment with these examples to get a better understanding of how they work. 
Python's flexibility with data types allows for powerful data manipulation and structuring capabilities.'''

#Part 1

#A variable is essentially a name that refers to a value. 
#The basic types of variables include integers, floats (decimal numbers), strings (text), and booleans (True or False).

# Integer: Whole numbers
age = 26
print("Age:", age)  # Output: Age: 26

# Float: Decimal numbers
height = 6.0
print("Height:", height)  # Output: Height: 6.0

# String: Text
name = "Nifemi"
print("Name:", name)  # Output: Name: Nifemi

# Boolean: True or False
is_student = True
print("Is student:", is_student)  # Output: Is student: False

#type check
print("Age:",type(age))  # Output: <class 'int'>
print("Height:",type(height))  # Output: <class 'float'>
print("Name:",type(name))  # Output: <class 'str'>
print("Is student:",type(is_student))  # Output: <class 'bool'>

#Part 2

#Lists are ordered collections of items that can be of mixed types. They are mutable, meaning you can change their contents.

# Creating a list
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits)

# Accessing list elements
print(fruits[0])  # Output: apple

# Adding an element to the end of the list
fruits.append("orange")
print(fruits)

# Removing an element
fruits.remove("banana")
print(fruits)

# Adding an item to the list
fruits.append("orange")
print(fruits)

# Accessing a list item by index
print(fruits[0])  # Output: apple

# Slicing a list
print(fruits[1:3])  # Output: ['banana', 'cherry']

#Dictionaries store key-value pairs. They are unordered and indexed by keys, which must be unique.

# Creating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print(person)

# Accessing a value by key
print(person["name"])  # Output: John

# Adding a new key-value pair
person["job"] = "Developer"
print(person)

# Removing a key-value pair
del person["age"]
print(person)

#Tuples are like lists but immutable. You cannot change, add, or remove items after the tuple is created.

# Creating a tuple
coordinates = (10.0, 20.0)
print(coordinates)

# Accessing a tuple item by index
print(coordinates[0])  # Output: 10.0

#Sets are unordered collections of unique items. They are useful for removing duplicates and set operations like union and intersection.

# Creating a set
colors = {"red", "green", "blue"}
print(colors)

# Adding an item to the set
colors.add("yellow")
print(colors)

# Removing duplicates
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)

# Creating another set
animals = {"cat", "dog", "fish"}
print(animals)

# Adding an element to a set
animals.add("bird")
print(animals)

# Removing an element from a set
animals.remove("fish")
print(animals)

#Part 3

#List comprehensions provide a concise way to create lists. 
#Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable.

# Creating a list of squares using list comprehension
squares = [x**2 for x in range(10)]
print(squares)

#map - applies a function to all the items in an input list.
#filter - creates a list of elements for which a function returns true.
# Using map to convert strings to uppercase
names = ["Alice", "Bob", "Charlie"]
uppercase_names = list(map(lambda x: x.upper(), names))
print(uppercase_names)

# Using filter to filter out even numbers
numbers = range(10)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#Type hints are a feature introduced in Python 3.5 that allow for explicit indication of the type of a variable, 
#which can help with code readability and error checking.
from typing import List, Dict, Tuple, Set

# Using type hints
def process(items: List[int]) -> int:
	return sum(items)

items: List[int] = [1, 2, 3]
total: int = process(items)
print(total)  # Output: 6
