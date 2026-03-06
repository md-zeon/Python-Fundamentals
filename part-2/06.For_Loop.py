'''
for Loop
- for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
- The syntax of a for loop is:
for variable in iterable:
    # code to execute for each item in the iterable
- The variable takes the value of each item in the iterable one by one, and the code block inside the loop is executed for each item.
- The for loop can also be used with the range() function to iterate over a sequence of numbers.
- The range() function generates a sequence of numbers, which can be used in a for loop to specify the number of iterations.
Syntax of using range() in a for loop:
for variable in range(start, stop, step):
    # code to execute for each number in the range
    print(variable)

- The start parameter is the starting number of the sequence (inclusive), the stop parameter is the ending number of the sequence (exclusive), and the step parameter is the increment between each number in the sequence. If start is not specified, it defaults to 0. If step is not specified, it defaults to 1.
- The for loop can be nested, meaning you can have a for loop inside another for loop, which is useful for iterating over multi-dimensional data structures like lists of lists.
'''

# Example 1: Iterating over a String
string = "hello"
print("Iterating over a string:")
for var in string:
    print(var, end=' ')

# Example 2: Iterating over a List
my_list = [1, 2, 3, 4, 5]
print("\nIterating over a list:")
for num in my_list:
    print(num, end=' ')

# Example 3: Using range() in a for loop
print("\nUsing range() in a for loop:")
for i in range(5):
    print(i, end=' ')

# Example 4: Using range() with start and stop parameters
print("\nUsing range() with start and stop parameters:")
for i in range(2, 10):
    print(i, end=' ')

# Example 5: Using range() with start, stop, and step parameters
print("\nUsing range() with start, stop, and step parameters:")
for i in range(0, 20, 5):
    print(i, end=' ')

# Example 6: Nested for loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nNested for loop:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # Print a newline after each row

# in operator in if statement
my_string = "hello world"
if "world" in my_string:
    print("The word 'world' is in the string.")
# the in operator can also be used to check for the presence of an element in a list
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("The number 3 is in the list.")

# internaly `in` operator uses a for loop to iterate over the elements of the string or list to check for the presence of the specified element. If the element is found, it returns True; otherwise, it returns False after checking all elements.


# practice problems

# count the number of i in the word "artificial intelligence"
word = "artificial intelligence"
count = 0
for char in word:
    if char == 'i':
        count += 1
print(f"The letter 'i' appears {count} times in the word '{word}'.")

# count the number of vowels in the word "artificial intelligence"
vowels = "aeiou"
count = 0
for char in word:
    # if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    #     count += 1
    # the above code can be simplified using the `in` operator to check if the character is a vowel
    if char in vowels:
        count += 1
print(f"The vowels appear {count} times in the word '{word}'.")