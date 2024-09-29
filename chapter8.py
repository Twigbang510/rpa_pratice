# Chapter 8: Input Validation with pyinputplus
import pyinputplus as pyip

# 1. Using `inputStr()` to Get Basic Text Input
def get_non_empty_string():
    return pyip.inputStr("Enter a non-empty string: ")

# 2. Using `inputNum()` to Get Numeric Input
def get_number():
    return pyip.inputNum("Enter a number: ")

# Request an integer only
def get_integer():
    return pyip.inputInt("Enter an integer: ")

# Request a float only
def get_float():
    return pyip.inputFloat("Enter a floating-point number: ")

# 3. Using `inputChoice()` for a List of Options
def choose_fruit():
    return pyip.inputChoice(['apple', 'banana', 'cherry'], prompt="Choose a fruit: ")

# 4. Using `inputMenu()` to Display a Menu of Choices
def choose_drink():
    return pyip.inputMenu(['tea', 'coffee', 'water'], numbered=True, prompt="Choose a drink:\n")

# 5. Using `inputYesNo()` for Yes/No Responses
def get_yes_no():
    return pyip.inputYesNo("Do you want to continue? (yes/no): ")

# 6. Using `inputBool()` for Boolean Responses
def get_boolean():
    return pyip.inputBool("Enter True or False: ")

# 7. Setting Validation Criteria with `inputNum()`
def get_number_in_range():
    return pyip.inputNum("Enter a number between 1 and 10: ", min=1, max=10)

def get_number_greater_than_10():
    return pyip.inputNum("Enter a number greater than 10: ", greaterThan=10)

# 8. Using Regular Expressions with `inputRegex()`
def get_phone_number():
    return pyip.inputRegex(r'^\d{3}-\d{3}-\d{4}$', prompt="Enter a phone number (xxx-xxx-xxxx): ")

# 9. Using Timeouts, Retry Limits, and Default Values
def get_number_with_limit():
    try:
        return pyip.inputNum("Enter a number (3 attempts, 10s timeout): ", limit=3, timeout=10, default='N/A')
    except pyip.TimeoutException:
        print("You took too long!")
        return None
    except pyip.RetryLimitException:
        print("Too many invalid attempts!")
        return None

# 10. Allowing Blank Input
def get_string_allow_blank():
    return pyip.inputStr("Enter a string (can be blank): ", blank=True)

# 11. Custom Validation Functions
def is_even(num):
    num = int(num)
    if num % 2 != 0:
        raise Exception("The number is not even.")
    return num

def get_even_number():
    return pyip.inputCustom(is_even, prompt="Enter an even number: ")
