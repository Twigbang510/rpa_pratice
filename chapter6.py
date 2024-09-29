# Chapter 6: Manipulating Strings

# 1. Working with Strings
def working_with_strings():
    text = "Hello, world!"
    print(text)  # Output: Hello, world!

    # Using triple quotes for multi-line strings
    multiline_text = """This is a
multi-line string."""
    print(multiline_text)
    # Output:
    # This is a
    # multi-line string.

# 2. Escape Characters
def escape_characters():
    quote = 'He said, "It\'s a lovely day!"'
    print(quote)  # Output: He said, "It's a lovely day!"

    new_line_text = "First line.\nSecond line."
    print(new_line_text)
    # Output:
    # First line.
    # Second line.

# 3. Raw Strings
def raw_strings():
    raw_string = r'This is a raw string. Newlines are not processed: \n'
    print(raw_string)  # Output: This is a raw string. Newlines are not processed: \n

# 4. Indexing and Slicing Strings
def indexing_and_slicing():
    sample_text = "Automate"
    print(sample_text[0])  # Output: A
    print(sample_text[-1])  # Output: e
    print(sample_text[1:4])  # Output: uto
    print(sample_text[:4])  # Output: Auto
    print(sample_text[4:])  # Output: mate

# 5. The `in` and `not in` Operators with Strings
def in_not_in_operators():
    sample_text = "Automate"
    print('Auto' in sample_text)  # Output: True
    print('mate' not in sample_text)  # Output: False

# 6. Useful String Methods
class StringMethods:
    def __init__(self, text):
        self.text = text

    # Method to convert to uppercase and lowercase
    def convert_case(self):
        print(self.text.upper())  # Output: HELLO, WORLD!
        print(self.text.lower())  # Output: hello, world!

    # Method to check if the string is uppercase or lowercase
    def check_case(self):
        print(self.text.isupper())  # Output: False
        print(self.text.islower())  # Output: False

    # Method to check if the string starts or ends with a specific substring
    def start_end_check(self, start_substring, end_substring): #Input: 'hi' and 'world'
        print(self.text.startswith(start_substring))  # Output: False
        print(self.text.endswith(end_substring))  # Output: True

    # Method to join elements of a list into a string
    def join_words(self, words): #Input: world
        joined_string = ' '.join(words)
        print(joined_string)  # Output: w o r l d

    # Method to split the string into a list of substrings
    def split_text(self, delimiter=', '):
        split_text = self.text.split(delimiter)
        print(split_text)  # Output: ['Hello', 'world!']

    # Method to justify or center the text
    def justify_text(self):
        print(self.text.rjust(20))  # Output: '       Hello, world!'
        print(self.text.ljust(20, '-'))  # Output: 'Hello, world!-------'
        print(self.text.center(20, '*'))  # Output: '***Hello, world!****'

    # Method to strip whitespace or specified characters
    def strip_text(self):
        whitespace_text = '   Hello, world!   '
        print(whitespace_text.strip())  # Output: 'Hello, world!'
        print(whitespace_text.rstrip())  # Output: '   Hello, world!'
        print(whitespace_text.lstrip())  # Output: 'Hello, world!   '

# 7. String Formatting
def string_formatting():
    name = "Alice"
    age = 30

    # Using f-strings
    formatted_string = f"My name is {name} and I am {age} years old."
    print(formatted_string)  # Output: My name is Alice and I am 30 years old.

    # Using `format()` method
    formatted_string_old = "My name is {} and I am {} years old.".format(name, age)
    print(formatted_string_old)  # Output: My name is Alice and I am 30 years old.

# 8. Practice Project: Password Strength Checker
def is_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit

def password_strength_checker():
    password = input("Enter a password to check its strength: ")
    if is_strong_password(password):
        print("This is a strong password.") 
    else:
        print("This is a weak password.") 
