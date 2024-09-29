# Chapter 2: Flow Control

## 1. Boolean Values
# Python has two Boolean values: True and False.
# They are case-sensitive, so always use capitalized 'True' and 'False'.

# Example:
is_true = True
is_false = False

## 2. Comparison Operators
# Comparison operators compare two values and evaluate to a Boolean value.
# List of comparison operators:
# - == : Equal to
# - != : Not equal to
# - <  : Less than
# - >  : Greater than
# - <= : Less than or equal to
# - >= : Greater than or equal to

# Example:
print(42 == 42)   # True
print(42 != 99)   # True
print(42 < 100)   # True
print(42 > 100)   # False
print(42 <= 42)   # True
print(42 >= 100)  # False

## 3. Boolean Operators
# Boolean operators: 'and', 'or', and 'not'
# - 'and' : Returns True if both operands are True
# - 'or'  : Returns True if at least one of the operands is True
# - 'not' : Reverses the Boolean value

# Example:
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

## 4. Flow Control Statements
# Python has flow control statements like 'if', 'else', and 'elif'.

### 4.1. if Statement
# An 'if' statement checks a condition and executes a block of code if the condition is True.

# Example:
if 10 > 5:
    print("10 is greater than 5")

### 4.2. else Statement
# The 'else' statement executes a block of code if the previous 'if' condition is False.

# Example:
if 10 < 5:
    print("10 is less than 5")
else:
    print("10 is not less than 5")

### 4.3. elif Statement
# The 'elif' statement checks another condition if the previous 'if' condition is False.

# Example:
if 10 < 5:
    print("10 is less than 5")
elif 10 == 5:
    print("10 is equal to 5")
else:
    print("10 is greater than 5")

## 5. while Loop
# A 'while' loop repeatedly executes a block of code as long as the condition is True.

# Example:
count = 0
while count < 5:
    print(count)
    count += 1  # Increments count by 1

## 6. for Loop and range()
# A 'for' loop iterates over a sequence (like a list, tuple, or string).
# The 'range()' function generates a sequence of numbers.

# Example:
for i in range(5):  # Generates numbers from 0 to 4
    print(i)

## 7. break and continue Statements
# - 'break' : Exits the loop immediately.
# - 'continue' : Skips the current iteration and moves to the next.

# Example using 'break':
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2

# Example using 'continue':
for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0, 1, 2, 4

## 8. Importing Modules
# Use 'import' to include additional functionality from Python's standard library.

# Example:
import random
print(random.randint(1, 10))  # Generates a random integer between 1 and 10

from test_module import module1 as test1, module2 as test2
print(test1.plus(2,2))

## Summary
# - Boolean values, comparison operators, and Boolean operators help control the flow of the program.
# - 'if', 'elif', and 'else' statements allow decision-making.
# - Loops ('while' and 'for') let you execute blocks of code multiple times.
# - 'break' and 'continue' provide more control over loop execution.
# - Modules extend the functionality of your programs.
