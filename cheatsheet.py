#Cheatsheet
1 + 1 #Everything after the hash symbol is ignored by Python
help(max) #Display the documentation for the max function
type('a') #Get the type of an object — this returns str

#Order of Operations - PEMDAS
>>> 2 + 3 * 6
# 20

>>> (2 + 3) * 6
# 30

>>> 2 ** 8
#256

>>> 23 // 7
# 3

>>> 23 % 7
# 2

>>> (5 - 1) * ((7 + 1) / (3 - 1))
# 16.0

#Arithmetic operators
102 + 37 #Add two numbers with +
102 - 37 # Subtract a number with -
4 * 6 # Multiply two numbers with *
22 / 7 # Divide a number by another with /
22 // 7 # Integer divide a number with //
3 ** 4 # Raise to the power with **
22 % 7 # Returns 1 # Get the remainder  after division with %

#Assignment Operators
a = 5 # Assign a value to a
x[0] =1 # Change the value of an item in a list


#Numeric Comparison Operators
3 == 3 # Test for equality with ==
3 != 3 # Test for inequality with !=
3 > 1 # Test greater than with >
3 >= 3 # Test greater than or equal to with >=
3 < 4 # Test less than with <
3 <= 4 # Test less than or equal to with <=

#Logical Operators
~(2 == 2) # Logical NOT with ~
(1 != 1) & (1 < 1) # Logical AND with &
(1 >= 1) | (1 < 1) # Logical OR with |
(1 != 1) ^ (1 < 1) # Logical XOR with ^


#LISTS
# Create lists with [], elements separated by commas
x = [1, 3, 2]

# Return a sorted copy of the list x
sorted(x) # Returns [1, 2, 3]

# Sort the list in-place (replaces x)
x.sort() # Returns None

# Reverse the order of elements in x
reversed(x) # Returns [2, 3, 1]

# Reverse the list in-place
x.reversed() # Returns None

# Count the number of element 2 in the list
x.count(2)

# Define the list 
x = ['a', 'b', 'c', 'd', 'e']

# Select the 0th element in the list
x[0] # 'a'

# Select the last element in the list
x[-1] # 'e'

# Select 1st (inclusive) to 3rd (exclusive)
x[1:3] # ['b', 'c']

# Select the 2nd to the end
x[2:] # ['c', 'd', 'e']

# Select 0th to 3rd (exclusive)
x[:3] # ['a', 'b', 'c']

# Define the list x and y  
x = [1, 3, 6] 
y = [10, 15, 21]

# Concatenate lists with +
x + y # [1, 3, 6, 10, 15, 21]

# Repeat list n times with *
3 * x # [1, 3, 6, 1, 3, 6, 1, 3, 6]

#Characters and Strings
# Create a string variable with single or double quotes
"Hello"

# Embed a quote in string with the escape character \
"He said, \"Hello\""

# Create multi-line strings with triple quotes
"""
There once was a small bird
he ate red berries a lot
cause he is a bird
- a Haiku
"""

# Get the character at a specific position
str[0] 

# Get a substring from starting to ending index (exclusive)
str[0:2]

# Create a string named str
str = "Jack and Jill"

# Convert a string to uppercase
str.upper() # 'JACK AND JILL'

# Convert a string to lowercase
str.lower() # 'jack and jill'

# Convert a string to title case
str.title() # 'Jack And Jill' 

# Replaces matches of a substring with another
str.replace("J", "P") # 'Pack and Pill'