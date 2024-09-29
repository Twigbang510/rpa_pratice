# Chapter 1: Python Basics

## 1. Expressions and Values

# Example:
2 + 2  # This is an expression. Result is 4
'Hello'  # This is a string value

## 2. Arithmetic Operators
# Basic operators:
# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division (always returns a float)
# % : Modulus (remainder)
# // : Integer division
# ** : Exponentiation

# Examples:
10 + 5  # Result: 15
10 - 3  # Result: 7
10 * 3  # Result: 30
10 / 2  # Result: 5.0
10 % 3  # Result: 1
10 // 3 # Result: 3
10 ** 2 # Result: 100

## 3. Variables
# Variables are used to store values. Use the = operator to assign a value to a variable.

# Rules for naming variables:
# - Can contain letters, numbers, and underscores (_)
# - Cannot start with a number
# - Case-sensitive ('age' and 'Age' are different variables)

# Example:
spam = 42  # Assigns the value 42 to the variable spam
spam + 1   # Result: 43

## 4. Data Types
# Python has different data types including:
# - Integer: Whole numbers like 1, 2, 100
# - Float: Decimal numbers like 1.0, 2.5
# - String: Text enclosed in quotes like 'hello', "Python"

# Example:
type(42)       # Result: <class 'int'>
type(3.14)     # Result: <class 'float'>
type('hello')  # Result: <class 'str'>

## 5. String Concatenation and Replication
# Concatenation: Use the + operator to combine strings.
# Replication: Use the * operator to repeat a string multiple times.

# Examples:
'Hello' + ' World'  # Result: 'Hello World'
'Python' * 3        # Result: 'PythonPythonPython'

## 6. input() and Data Type Conversion
# input() is used to take input from the user. It always returns a string.
# Use int() or float() to convert a string to an integer or float.

# Example:
name = input('What is your name? ')  # Takes user input and stores in the variable name
age = int(input('What is your age? '))  # Takes input, converts to integer, and stores in age

## 7. print() and str()
# print() is used to display values on the screen.
# Use str() to convert other data types (numbers, variables, etc.) to a string.

# Examples:
print('Hello, ' + name)  # Prints 'Hello, ' concatenated with the value of name
print('You will be ' + str(age + 1) + ' in a year.')  # Converts the number to a string before concatenation

## 8. Comments
# Use the # character to add comments to your code. Everything after # will not be executed.




