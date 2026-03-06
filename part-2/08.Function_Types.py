'''
Types of Functions in Python:
1. Built-in Functions: These are functions that are pre-defined in Python and can be used directly without any need for importing. Examples include `print()`, `len()`, `type()`, etc.
2. User-defined Functions: These are functions that are defined by the user to perform a specific task. They can be called multiple times throughout the program.
3. Lambda Functions: These are small, anonymous functions that can have any number of arguments but can only have one expression. They are defined using the `lambda` keyword.
4. Recursive Functions: These are functions that call themselves in order to solve a problem. They typically have a base case to prevent infinite recursion.
5. Generator Functions: These are functions that use the `yield` statement to return an iterator. They allow you to iterate over a sequence of values without storing the entire sequence in memory at once.
'''

'''
Built-in Functions:
1. `print()`: Used to output data to the console.
2. `len()`: Returns the length of an object.
3. `type()`: Returns the type of an object.
4. `input()`: Used to take input from the user.
5. `range()`: Generates a sequence of numbers.
6. `sum()`: Returns the sum of a sequence of numbers.
7. `max()`: Returns the largest item in an iterable.
8. `min()`: Returns the smallest item in an iterable.
9. `sorted()`: Returns a sorted list from the items in an iterable.
10. `abs()`: Returns the absolute value of a number.
'''
'''
User-defined Functions:
To define a user-defined function in Python, you use the `def` keyword followed by the function name and parentheses. You can also include parameters inside the parentheses. The function body is indented below the function definition.
Example:
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!
'''
'''
Lambda Functions:
Lambda functions are anonymous functions that can be defined in a single line. They are often used for short, simple functions that are not reused elsewhere in the code.
Syntax:
lambda arguments: expression
Example:
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
'''
'''
Recursive Functions:
A recursive function is a function that calls itself in order to solve a problem. It typically has a base case to prevent infinite recursion.
Example:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
'''
'''
Generator Functions:
Generator functions use the `yield` statement to return an iterator. They allow you to iterate over a sequence of values without storing the entire sequence in memory at once.
MORE SIZEABLE THAN LISTS, GENERATORS CAN BE USED TO HANDLE LARGE DATA SETS OR INFINITE SEQUENCES.

Simply put, a generator function is a special type of function that generates a sequence of values using the `yield` statement. Each time the generator's `__next__()` method is called, the generator function executes until it reaches a `yield` statement, at which point it returns the value specified by `yield` and pauses its execution. The next time `__next__()` is called, the generator resumes execution right after the last `yield` statement.

Syntax:
def generator_function():
    yield value
Example:
def count_up_to(n):
    count = 1
    while count <= n:
        yield count # Yield each number in the sequence
        count += 1 # Increment the count

for number in count_up_to(5):
    print(number, end=' ')

# Output: 1 2 3 4 5

here, the `count_up_to` function is a generator that yields numbers from 1 to `n`. When we iterate over the generator using a for loop, it produces each number in the sequence one at a time, allowing us to handle large sequences efficiently without storing them all in memory at once.


'''