# Chapter 3: Functions

# 1. Introduction to Functions
def greet():
    print("Hello, world!")

# Call the function to test
greet()  # Output: Hello, world!


# 2. Arguments and Parameters
def greet(name):
    print(f"Hello, {name}!")

# Test with an argument
greet("Alice")  # Output: Hello, Alice!


# 3. Return Values and `return` Statement
def add(a, b):
    return a + b

# Call the function and store the result
result = add(3, 5)
print(result)  # Output: 8


# 4. None Value
def greet(name):
    print(f"Hello, {name}!")

# Function without a return statement
result = greet("Bob")
print(result)  # Output: Hello, Bob! None


# 5. Keyword Arguments and `print()` Function
print("Hello", "world", sep=", ", end="!\n")  # Output: Hello, world!


# 6. Local and Global Scope
def my_function():
    local_var = 10  # Local variable
    print(local_var)

global_var = 20  # Global variable

my_function()  # Output: 10
print(global_var)  # Output: 20


# 7. The `global` Statement
counter = 0

def increment():
    global counter
    counter += 1

# Test the global modification
increment()
print(counter)  # Output: 1


# 8. Exception Handling with `try` and `except`
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

# Test exception handling
result = divide(4, 0)  # Output: Error: Cannot divide by zero.
print(result)  # Output: None

