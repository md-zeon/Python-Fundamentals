'''
Tupples in Python
A tuple is an ordered collection of items that is immutable, meaning that once a tuple is created, its contents cannot be changed. Tuples are defined using parentheses () and can contain elements of different types, including numbers, strings, and even other tuples. They are often used to group related data together and can be accessed using indexing and slicing, similar to lists.

Creating a Tuple:
You can create a tuple by enclosing a comma-separated sequence of items in parentheses.
Syntax: tuple_name = (item1, item2, item3, ...)

Accessing Tuple Elements:
You can access individual elements of a tuple using their index. The index starts at 0 for the first element.
Syntax: tuple_name[index]

Tuples have various methods for accessing and manipulating their contents. Here are some common tuple operations:
- Getting the length: You can get the number of elements in a tuple using the len() function.
- Checking for membership: You can check if an element is in a tuple using the in keyword.
- Concatenation: You can concatenate two tuples using the + operator.
- Repetition: You can repeat a tuple using the * operator.
- Unpacking: You can unpack the elements of a tuple into individual variables.
- Slicing: You can slice a tuple to get a subset of its elements using the slicing syntax.
- Counting occurrences: You can count the number of occurrences of a specific element in a tuple using the count() method.
- Finding the index: You can find the index of the first occurrence of a specific element in a tuple using the index() method.
- Sorting: You can sort the elements of a tuple using the sorted() function, which returns a new sorted list.
- Converting to a list: You can convert a tuple to a list using the list() function, which allows you to modify the contents since lists are mutable.
- Converting to a tuple: You can convert a list to a tuple using the tuple() function, which creates an immutable version of the list.

Types of Tuples:
- Single-element tuple: To create a single-element tuple, you need to include a comma after the element. For example: single_tuple = (5,). type(single_tuple) will return <class 'tuple'>.
- Nested tuples: Tuples can contain other tuples as elements, allowing for nested structures. For example: nested_tuple = (1, 2, (3, 4), 5). 
- Empty tuple: An empty tuple is defined using empty parentheses. For example: empty_tuple = ().
- Tuple with different data types: A tuple can contain elements of different data types. For example: mixed_tuple = (1, "Hello", 3.14, [1, 2, 3], (4, 5)).
- Tuple with duplicate elements: A tuple can contain duplicate elements. For example: duplicate_tuple = (1, 2, 2, 3, 4, 4, 5).
'''

# Creating a tuple
my_tuple = (1, "Hello", 3.14, [1, 2, 3], (4, 5))
# Accessing tuple elements
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: Hello
print(my_tuple[2])  # Output: 3.14
# Getting the length of a tuple
print(len(my_tuple))  # Output: 5
# Checking for membership
print(3.14 in my_tuple)  # Output: True
# Concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
# Repetition of tuples
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
# Unpacking a tuple
a, b, c = tuple1
print(a, b, c)  # Output: 1 2 3
# Slicing a tuple
sliced_tuple = concatenated_tuple[2:5]
print(sliced_tuple)  # Output: (3, 4, 5)
# Counting occurrences of an element
duplicate_tuple = (1, 2, 2, 3, 4, 4, 5)
print(duplicate_tuple.count(2))  # Output: 2
# Finding the index of an element
print(duplicate_tuple.index(4))  # Output: 4
# Sorting a tuple
unsorted_tuple = (3, 1, 4, 2)
sorted_tuple = sorted(unsorted_tuple)
print(sorted_tuple)  # Output: [1, 2, 3, 4]
# Converting a tuple to a list
tuple_to_list = list(my_tuple)
print(tuple_to_list)  # Output: [1, 'Hello', 3.14, [1, 2, 3], (4, 5)]
# Converting a list to a tuple
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)  # Output: (1, 'Hello', 3.14, [1, 2, 3], (4, 5))
# Single-element tuple
single_tuple = (5,)
print(type(single_tuple))  # Output: <class 'tuple'>
# Nested tuples
nested_tuple = (1, 2, (3, 4), 5)

not_single_tuple = (5)
print(type(not_single_tuple))  # Output: <class 'int'>, not a tuple because the comma is missing. Single-element tuples require a comma to differentiate them from regular parentheses used for grouping.
# Empty tuple
empty_tuple = ()
print(type(empty_tuple))  # Output: <class 'tuple'>

'''
Looping through a tuple
You can loop through the elements of a tuple using a for loop. This allows you to perform operations on each element in the tuple. Here's an example of how to loop through a tuple:
Syntax:
for element in tuple_name:
    # Perform operations with element

We can also use the enumerate() function to get both the index and the value of each element in the tuple while looping. Here's an example:
for index, element in enumerate(tuple_name):
    # Perform operations with index and element
    print(f"Index: {index}, Element: {element}")

'''

# Looping through a tuple
my_tuple = (1, "Hello", 3.14, [1, 2, 3], (4, 5))
for element in my_tuple:
    print(element)
# Using enumerate to loop through a tuple with index
for index, element in enumerate(my_tuple):
    print(f"Index: {index}, Element: {element}")

# Using a while loop to loop through a tuple
index = 0
while index < len(my_tuple):
    print(my_tuple[index])
    index += 1

# Using list comprehension to create a new list from a tuple
squared_tuple = (1, 2, 3, 4, 5)
squared_list = [x**2 for x in squared_tuple]
print(squared_list)  # Output: [1, 4, 9, 16, 25]