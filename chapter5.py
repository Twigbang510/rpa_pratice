# Chapter 5: Dictionaries

# 1. Introduction to Dictionaries
def create_person_dict():
    person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
    return person
def create_contact_dict():
    contacts = {'Alice': {'phone': '555-1234', 'email': 'alice@example.com'},
                'Bob': {'phone': '555-5678', 'email': 'bob@example.com'}}
    return contacts

# 2. Accessing Values in a Dictionary
def access_values(person):
    name = person['name']
    age = person.get('age')
    country = person.get('country', 'Not specified')
    print(name)  # Output: Alice
    print(age)  # Output: 25
    print(country)  # Output: Not specified
    return name, age, country

# 3. Adding or Modifying Dictionary Values
def add_modify_values(person):
    person['age'] = 30  # Modify an existing key
    person['country'] = 'USA'  # Add a new key-value pair
    print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
    return person

# 4. Deleting Key-Value Pairs
def delete_key_value(person):
    del person['city']  # Remove the 'city' key
    age = person.pop('age')  # Remove 'age' and return its value
    print(person)  # Output: {'name': 'Alice', 'country': 'USA'}
    print(age)  # Output: 30
    return person, age

# 5. Checking for the Existence of Keys
def check_key_existence(person):
    has_name = 'name' in person
    no_city = 'city' not in person
    print(has_name)  # Output: True
    print(no_city)  # Output: True
    return has_name, no_city

# 6. Looping through Dictionaries
def loop_through_dict(person):
    keys = [key for key in person.keys()]  # Collect keys
    values = [value for value in person.values()]  # Collect values
    items = [f'{key}: {value}' for key, value in person.items()]  # Collect key-value pairs as strings
    print(keys)  # Output: ['name', 'country']
    print(values)  # Output: ['Alice', 'USA']
    print(items)  # Output: ['name: Alice', 'country: USA']
    return keys, values, items

# 7. Dictionary Methods
def dictionary_methods(person):
    keys = list(person.keys())
    values = list(person.values())
    items = list(person.items())
    print(keys)  # Output: ['name', 'country']
    print(values)  # Output: ['Alice', 'USA']
    print(items)  # Output: [('name', 'Alice'), ('country', 'USA')]
    return keys, values, items

# 8. Nested Dictionaries
def access_nested_dict(contacts):
    alice_phone = contacts['Alice']['phone']
    print(alice_phone)  # Output: '555-1234'
    return alice_phone

# 9. The setdefault() Method
def setdefault_method(person):
    person.setdefault('hobby', 'unknown')  # Adds 'hobby' if not present
    person.setdefault('name', 'Bob')  # Does nothing as 'name' exists
    print(person)  # Output: {'name': 'Alice', 'country': 'USA', 'hobby': 'unknown'}
    return person

# 10. Pretty Printing a Dictionary with pprint
def pretty_print_dict(contacts):
    import pprint
    pprint.pprint(contacts)
    # Output:
    # {'Alice': {'email': 'alice@example.com', 'phone': '555-1234'},
    #  'Bob': {'email': 'bob@example.com', 'phone': '555-5678'},
    #  'Charlie': {'email': 'charlie@example.com', 'phone': '555-9876'}}

# 11. Practice Project: Character Count
def character_count(text):
    import pprint
    char_count = {}
    for char in text:
        char_count.setdefault(char, 0)
        char_count[char] += 1
    pprint.pprint(char_count)  # Output: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',', 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
    return char_count
