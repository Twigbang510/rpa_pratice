# Chapter 4: Lists

# 1. Introduction to Lists
def create_fruit_list():
    fruits = ['apple', 'banana', 'cherry', 'date']
    return fruits  # Output: ['apple', 'banana', 'cherry', 'date']

# 2. Accessing Elements in a List
def access_elements(fruits):
    first = fruits[0]
    third = fruits[2]
    last = fruits[-1]
    print(first)  # Output: apple
    print(third)  # Output: cherry
    print(last)   # Output: date
    return first, third, last  # Output: ('apple', 'cherry', 'date')

# 3. Slicing Lists
def slice_list(fruits):
    slices = {
        '1_to_3': fruits[1:3],
        'start_to_2': fruits[:2],
        '2_to_end': fruits[2:],
        'all': fruits[:]
    }
    print(slices)  # Output: {'1_to_3': ['banana', 'cherry'], 'start_to_2': ['apple', 'banana'], '2_to_end': ['cherry', 'date'], 'all': ['apple', 'banana', 'cherry', 'date']}
    return slices

# 4. Changing Values in a List
def change_value(fruits):
    fruits[1] = 'blueberry'
    print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']
    return fruits

# 5. List Concatenation and Replication
def concatenate_and_replicate(fruits):
    more_fruits = ['elderberry', 'fig']
    all_fruits = fruits + more_fruits
    repeated_fruits = fruits * 2
    print(all_fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']
    print(repeated_fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'apple', 'blueberry', 'cherry', 'date']
    return all_fruits, repeated_fruits

# 6. Removing Elements from a List
def remove_elements(fruits):
    del fruits[2]
    fruits.remove('blueberry')
    print(fruits)  # Output: ['apple', 'date']
    return fruits

# 7. Working with Lists using `for` Loops
def loop_through_list(fruits):
    for fruit in fruits:
        print(fruit)  # Output: apple, date
    return fruits  # Output: ['apple', 'date']

# 8. The `in` and `not in` Operators
def check_membership(fruits):
    in_list = 'apple' in fruits
    not_in_list = 'banana' not in fruits
    print(in_list)  # Output: True
    print(not_in_list)  # Output: True
    return in_list, not_in_list  # Output: (True, True)

# 9. The `len()` Function
def get_length(fruits):
    length = len(fruits)
    print(length)  # Output: 2
    return length  # Output: 2

# 10. List Methods
class ListMethods:
    def __init__(self):
        self.fruits = create_fruit_list()  # Initializes with ['apple', 'banana', 'cherry', 'date']
        
    def append_to_list(self):
        self.fruits.append('grape')
        print(self.fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'grape']
        return self.fruits

    def insert_at_position(self):
        self.fruits.insert(1, 'blackberry')
        print(self.fruits)  # Output: ['apple', 'blackberry', 'banana', 'cherry', 'date', 'grape']
        return self.fruits

    def sort_list(self):
        self.fruits.sort()
        print(self.fruits)  # Output: ['apple', 'banana', 'blackberry', 'cherry', 'date', 'grape']
        return self.fruits

    def reverse_list(self):
        self.fruits.reverse()
        print(self.fruits)  # Output: ['grape', 'date', 'cherry', 'blackberry', 'banana', 'apple']
        return self.fruits

    def reverse_case(self):
        self.fruits = [fruit.upper() if fruit.islower() else fruit.lower() for fruit in self.fruits]
        print(self.fruits)  # Output: ['GRAPE', 'DATE', 'CHERRY', 'BLACKBERRY', 'BANANA', 'APPLE']
        return self.fruits

# 11. Nested Lists
def access_nested_list(matrix):
    row = matrix[1]
    element = matrix[1][2]
    print(row)  # Output: [4, 5, 6]
    print(element)  # Output: 6
    return row, element  # Output: ([4, 5, 6], 6)

# 12. List References and Copying
def copy_list(numbers):
    numbers_copy = numbers.copy()
    numbers_copy[0] = 99
    print(numbers)  # Output: [1, 2, 3]
    print(numbers_copy)  # Output: [99, 2, 3]
    return numbers, numbers_copy  # Output: ([1, 2, 3], [99, 2, 3])

# 13. Practice Project: Comma Code
def comma_code(items):
    if len(items) == 0:
        return ''  # Output: ''
    elif len(items) == 1:
        return items[0]  # Output: 'apples'
    else:
        result = ', '.join(items[:-1]) + ', and ' + items[-1]
        print(result)  # Output: apples, bananas, tofu, and cats
        return result
