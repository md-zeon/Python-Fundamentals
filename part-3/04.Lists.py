'''
Lists in Python
Lists are a built-in data structure in Python that allows you to store and manage a collection of items. They are ordered, mutable, and can contain elements of different types. Lists are defined using square brackets [] and can be created by separating items with commas.
Creating a List:
You can create a list by enclosing a comma-separated sequence of items in square brackets.
Syntax: list_name = [item1, item2, item3, ...]
Lists can contain any type of data, including numbers, strings, and even other lists.
Example:
'''
my_list = [1, "Hello", 3.14, [2, 4, 6]]
'''
Accessing List Elements:
You can access individual elements of a list using their index. The index starts at 0 for the first element.
Syntax: list_name[index]
Example:
'''
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: Hello
print(my_list[2])  # Output: 3.14
print(my_list[3])  # Output: [2, 4, 6]

# You can also use negative indexing to access elements from the end of the list
print(my_list[-1])  # Output: [2, 4, 6]
print(my_list[-2])  # Output: 3.14
# Lists are mutable, which means you can change their contents
my_list[0] = 42
print(my_list[0])  # Output: 42

'''
Lists have various methods for adding, removing, and manipulating their contents. Here are some common list operations:
- Adding elements: You can add new elements to a list using the append() method or the insert() method.
- Removing elements: You can remove elements from a list using the remove() method or the pop() method.
- Getting the length: You can get the number of elements in a list using the len() function.
- Sorting and reversing: You can sort a list using the sort() method and reverse the order of elements using the reverse() method.
- Checking for membership: You can check if an element is in a list using the in keyword.
'''
# You can also add new elements to a list using the append() method
my_list.append("New Item")
print(my_list)  # Output: [42, 'Hello', 3.14, [2, 4, 6], 'New Item']
# To remove an element from a list, you can use the remove() method
my_list.remove("Hello")
print(my_list)  # Output: [42, 3.14, [2, 4, 6], 'New Item']
# You can also use the pop() method to remove an element by index
my_list.pop(1)
print(my_list)  # Output: [42, [2, 4, 6], 'New Item']
# To get the length of a list, you can use the len() function
print(len(my_list))  # Output: 3

'''
Slicing and Concatenation:
Lists can be sliced to create a new list containing a subset of the original list. You can specify the start and end indices for slicing, and you can also use negative indices to slice from the end of the list. Additionally, lists can be concatenated using the + operator, and you can repeat a list using the * operator.
Slicing syntax: list_name[start:end]
Concatenation syntax: list1 + list2
Repetition syntax: list_name * n
'''
# Lists can also be sliced to create a new list containing a subset of the original list
sliced_list = my_list[0:2]
print(sliced_list)  # Output: [42, [2, 4, 6]]
# You can also use negative slicing to get elements from the end of the list
sliced_list = my_list[-2:]
print(sliced_list)  # Output: [[2, 4, 6], 'New Item']
# Lists can be concatenated using the + operator
another_list = [7, 8, 9]
combined_list = my_list + another_list
print(combined_list)  # Output: [42, [2, 4, 6], 'New Item', 7, 8, 9]
# You can also repeat a list using the * operator
repeated_list = my_list * 2
print(repeated_list)  # Output: [42, [2, 4, 6], 'New Item', 42, [2, 4, 6], 'New Item']
# Lists can contain duplicate elements
duplicate_list = [1, 2, 2, 3, 4, 4, 4]
print(duplicate_list)  # Output: [1, 2, 2, 3, 4, 4, 4]
# You can check if an element is in a list using the in keyword
print(42 in my_list)  # Output: True
print("Hello" in my_list)  # Output: False
# Lists can also be nested, meaning you can have lists within lists
nested_list = [1, [2, 3], [4, 5, 6]]
print(nested_list)  # Output: [1, [2, 3], [4, 5, 6]]
# You can access elements in a nested list using multiple indices
print(nested_list[1][0])  # Output: 2
print(nested_list[2][1])  # Output: 5

'''
Sorting and Reversing:
Lists have many built-in methods for manipulating their contents, such as sort(), reverse(), and clear(). The sort() method sorts the elements of a list in ascending order, while the reverse() method reverses the order of the elements. The clear() method removes all elements from the list, leaving it empty.

Sorting a list requires that all elements be of the same type, otherwise it will raise an error. For example, if you try to sort a list that contains both numbers and strings, it will not work because Python cannot compare different types of data for sorting. To sort a list successfully, ensure that all elements are of the same type, such as all numbers or all strings.
Reverse and clear operations can be performed on any list regardless of the types of elements it contains, as they do not require comparison between elements.

Sorting syntax: list_name.sort()
Sort is by default in ascending order, but you can also sort in descending order by passing the reverse=True argument to the sort() method. For example:
list_name.sort(reverse=True)
Reversing syntax: list_name.reverse()
Clearing syntax: list_name.clear()
'''

# Lists have many built-in methods for manipulating their contents, such as sort(), reverse(), and clear()
# my_list.sort()  # This will raise an error because the list contains different types of elements
# To sort a list, all elements must be of the same type
numbers_list = [3, 1, 4, 1, 5, 9]
numbers_list.sort() # This will sort the list in ascending order
print(numbers_list)  # Output: [1, 1, 3, 4, 5, 9]

numbers_list.sort(reverse=True) # This will sort the list in descending order
print(numbers_list)  # Output: [9, 5, 4, 3, 1, 1]

my_list.reverse()
print(my_list)  # Output: ['New Item', [2, 4, 6], 42]
my_list.clear()
print(my_list)  # Output: []    

# You can also use the `sorted()` function to create a new sorted list without modifying the original list
original_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(original_list)
print(sorted_list)  # Output: [1, 1, 3, 4, 5, 9]
print(original_list)  # Output: [3, 1, 4, 1, 5, 9]


'''
Looping through a List:
You can loop through the elements of a list using a for loop. This allows you to perform operations on each element of the list. You can also use a while loop to iterate through a list, but for loops are more commonly used for this purpose.
Looping syntax:
for element in list_name:
    # Perform operations on element
Or using a while loop:
index = 0
while index < len(list_name):
    element = list_name[index]
    # Perform operations on element
    index += 1

Or using a for loop with range:
for index in range(len(list_name)):
    element = list_name[index]
    # Perform operations on element
'''

my_list = [1, 2, 3, 4, 5]
# You can loop through the elements of a list using a for loop
print("\nUsing for loop:")
for element in my_list:
    print(element, end=" ")  # Output: 1 2 3 4 5
# You can also use a while loop to iterate through a list
print("\nUsing while loop:")
index = 0
while index < len(my_list):
    element = my_list[index]
    print(element, end=" ")  # Output: 1 2 3 4 5
    index += 1

# Or using a for loop with range
print("\nUsing for loop with range:")
for index in range(len(my_list)):
    element = my_list[index]
    print(element, end=" ")  # Output: 1 2 3 4 5

# You can also use list comprehensions to create a new list by applying an expression to each element of an existing list
squared_list = [x**2 for x in my_list]
print("\nSquared list using list comprehension:")
print(squared_list)  # Output: [1, 4, 9, 16, 25]