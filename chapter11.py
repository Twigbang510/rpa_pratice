# Chapter 11: Debugging

# 1. Raising Exceptions with `raise`
# You can use `raise` to throw an exception if a condition occurs.

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for _ in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)

# Testing the function
try:
    box_print('*', 5, 4)
except Exception as err:
    print(f'An error occurred: {err}')


# 2. Using Assertions for Debugging
# Assertions are sanity checks to verify that a condition is true. If the condition is false, the program crashes.

def validate_age(age):
    assert age > 0, 'Age must be positive!'
    print(f'Age is: {age}')

# Testing assertions
try:
    validate_age(-1)  # This will raise an assertion error
except AssertionError as err:
    print(f'Assertion error: {err}')


# 3. Using Logging to Create a Log File
import logging

# Configure logging to write messages to a file
logging.basicConfig(filename='my_program_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example function using logging
def factorial(n):
    logging.debug(f'Start of factorial({n})')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i={i}, total={total}')
    logging.debug(f'End of factorial({n})')
    return total

# Testing the function
print(factorial(5))  # Output: 120

# Check 'my_program_log.txt' to see the debug logs.


# 4. Logging Levels
# The logging module has different levels of logging: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
logging.critical('This is a critical message.')


# 5. Disabling Logging
# You can disable logging after a certain level using `logging.disable()`.
logging.disable(logging.CRITICAL)

# After this, no logging messages at CRITICAL level or below will be shown.
logging.critical('This message will not appear in the log.')


# 6. Using `pprint` for Pretty Printing
import pprint

# Pretty print complex data structures
data = [{'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'gardening']},
        {'name': 'Bob', 'age': 25, 'hobbies': ['hiking', 'gaming', 'cooking']}]

pprint.pprint(data)


