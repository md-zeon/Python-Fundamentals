'''
Dictionary in Python
Definition:
A dictionary in Python is a collection of key-value pairs, where each key is unique and maps to a specific value. Dictionaries are mutable, meaning that you can change their contents after they have been created. They are defined using curly braces {} and can contain elements of different types, including numbers, strings, lists, and even other dictionaries.
Syntax: dictionary_name = {
    key1: value1,
    key2: value2,
    key3: value3,
    ...
}

key: The key is a unique identifier for each value in the dictionary. It can be of any immutable data type, such as strings, numbers, or tuples.
value: The value is the data associated with a specific key. It can be of any data type, including lists, dictionaries, or even functions.

As of Python 3.7, dictionaries maintain the order of insertion, meaning that the items will be returned in the order they were added to the dictionary.
'''
# Example of a dictionary
person = {
    "name": "Zeanur Rahaman Zeon",
    "age": 23,
    "city": "Dhaka",
    "hobbies": ["coding", "traveling", "cooking"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "university": "University of Dhaka"
    },
    123: "This is a numeric key",
    (1, 2): "This is a tuple key",
}

'''
Accessing values in a dictionary
You can access values in a dictionary using their corresponding keys. There are several ways to do this:
1. Using square brackets []: This is the most common way to access values in a dictionary. You simply use the key inside square brackets to retrieve the corresponding value.
value = dictionary_name[key]
2. Using the get() method: This method allows you to access values in a dictionary while providing a default value if the key does not exist. It takes two arguments: the key you want to access and an optional default value. If the key is not found in the dictionary, it will return the default value instead of raising a KeyError.
value = dictionary_name.get(key, default_value)
3. Using the items() method: This method returns a view object that displays a list of dictionary's key-value tuple pairs. You can iterate through this view to access both keys and values.
for key, value in dictionary_name.items():
    print(f"Key: {key}, Value: {value}")

'''

# Accessing values using square brackets
print(person["name"])  # Output: Zeanur Rahaman Zeon
print(person["age"])   # Output: 23
print(person[123])  # Output: This is a numeric key
print(person[(1, 2)])  # Output: This is a tuple key
# Accessing values using the get() method
print(person.get("city"))  # Output: Dhaka
print(person.get("country", "Not Found"))  # Output: Not Found
# Accessing values using the items() method
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

'''
Dictionary Methods
Python provides several built-in methods for working with dictionaries. Here are some commonly used dictionary methods:
1. keys(): This method returns a view object that displays a list of all the keys in the dictionary.
keys = dictionary_name.keys()
2. values(): This method returns a view object that displays a list of all the values in the dictionary.
values = dictionary_name.values()
3. items(): This method returns a view object that displays a list of dictionary's key-value tuple pairs.
items = dictionary_name.items()
4. update(): This method updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
dictionary_name.update(other_dictionary)
5. pop(): This method removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError.
value = dictionary_name.pop(key)
6. popitem(): This method removes and returns an arbitrary key-value pair from the dictionary. If the dictionary is empty, it raises a KeyError.
key, value = dictionary_name.popitem()
7. clear(): This method removes all items from the dictionary.
dictionary_name.clear()
8. copy(): This method returns a shallow copy of the dictionary.
new_dictionary = dictionary_name.copy()
9. get(): This method returns the value for the specified key if the key is in the dictionary, otherwise it returns a default value.
value = dictionary_name.get(key, default_value)
10. setdefault(): This method returns the value of the specified key. If the key does not exist, it inserts the key with a specified default value and returns that value.
value = dictionary_name.setdefault(key, default_value)
11. fromkeys(): This method creates a new dictionary with keys from an iterable and values set to a specified value.
new_dictionary = dict.fromkeys(iterable, value)
'''
# Example of using dictionary methods
# Using keys() method
print(person.keys())  # Output: dict_keys(['name', 'age', 'city', 'hobbies', 'education', 123, (1, 2)])
# Using values() method
print(person.values())  # Output: dict_values(['Zeanur Rahaman Zeon', 23, 'Dhaka', ['coding', 'traveling', 'cooking'], {'degree': "Bachelor's", 'major': 'Computer Science', 'university': 'University of Dhaka'}, 'This is a numeric key', 'This is a tuple key'])
# Using items() method
print(person.items())  # Output: dict_items([('name', 'Zeanur Rahaman Zeon'), ('age', 23), ('city', 'Dhaka'), ('hobbies', ['coding', 'traveling', 'cooking']), ('education', {'degree': "Bachelor's", 'major': 'Computer Science', 'university': 'University of Dhaka'}), (123, 'This is a numeric key'), ((1, 2), 'This is a tuple key')])
# Using update() method
new_info = {"country": "Bangladesh", "age": 24}
person.update(new_info)
print(person)  # Output: {'name': 'Zeanur Rahaman Zeon', 'age': 24, 'city': 'Dhaka', 'hobbies': ['coding', 'traveling', 'cooking'], 'education': {'degree': "Bachelor's", 'major': 'Computer Science', 'university': 'University of Dhaka'}, 123: 'This is a numeric key', (1, 2): 'This is a tuple key', 'country': 'Bangladesh'}
# Using pop() method
age = person.pop("age")
print(age)  # Output: 24
print(person)  # Output: {'name': 'Zeanur Rahaman Zeon', 'city': 'Dhaka', 'hobbies': ['coding', 'traveling', 'cooking'], 'education': {'degree': "Bachelor's", 'major': 'Computer Science', 'university': 'University of Dhaka'}, 123: 'This is a numeric key', (1, 2): 'This is a tuple key', 'country': 'Bangladesh'}
# Using popitem() method
key, value = person.popitem()
print(f"Removed key: {key}, value: {value}")  # Output: Removed key: country, value: Bangladesh
print(person)  # Output: {'name': 'Zeanur Rahaman Zeon', 'city': 'Dhaka', 'hobbies': ['coding', 'traveling', 'cooking'], 'education': {'degree': "Bachelor's", 'major': 'Computer Science', 'university': 'University of Dhaka'}, 123: 'This is a numeric key', (1, 2): 'This is a tuple key'}

# Using copy() method
person_copy = person.copy()
print(person_copy)  # Output: {'name': 'Zeanur Rahaman Zeon', 'city': 'Dhaka', 'hobbies': ['coding', 'traveling', 'cooking'], 'education': {'degree': "Bachelor's", 'major': 'Computer Science', 'university': 'University of Dhaka'}, 123: 'This is a numeric key', (1, 2): 'This is a tuple key'}

# Using setdefault() method
default_value = person.setdefault("country", "Not Found")
print(default_value)  # Output: Not Found
print(person)  # Output: {'name': 'Zeanur Rahaman Zeon', 'city': 'Dhaka', 'hobbies': ['coding', 'traveling', 'cooking'], 'education': {'degree': "Bachelor's", 'major': 'Computer Science', 'university': 'University of Dhaka'}, 123: 'This is a numeric key', (1, 2): 'This is a tuple key', 'country': 'Not Found'}

# Using fromkeys() method
keys = ["name", "age", "city"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# Using get() method with a default value
print(person.get("age", "Age not found"))  # Output: Age not found

# Using get() method without a default value
print(person.get("age"))  # Output: None

# Using setdefault() method to add a new key-value pair
person.setdefault("profession", "Software Engineer")
print(person)  # Output: {'name': 'Zeanur Rahaman Zeon', 'city': 'Dhaka', 'hobbies': ['coding', 'traveling', 'cooking'], 'education': {'degree': "Bachelor's", 'major': 'Computer Science', 'university': 'University of Dhaka'}, 123: 'This is a numeric key', (1, 2): 'This is a tuple key', 'country': 'Not Found', 'profession': 'Software Engineer'}

# Using clear() method
person.clear()
print(person)  # Output: {}
