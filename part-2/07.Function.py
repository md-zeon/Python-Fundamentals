'''
Functions in Python
Functions are reusable blocks of code that perform a specific task. They allow you to break down your code into smaller, more manageable pieces, and can be called multiple times throughout your program.
Defining a Function
Functions has 2 parts:
1. Function Definition: This is where you define the function and its parameters.
2. Function Call: This is where you call the function to execute its code.

Syntax of Function Definition:
def function_name(parameters):
    # Function body
    # Code to be executed
    # Optional return statement

Syntax of a Function  Call:
function_name(arguments)

- return statement: A function can return a value using the return statement. This allows you to get a result back from the function after it has completed its task.

parameters vs Arguments:
- Parameters are the variables that are defined in the function definition. They act as placeholders for the values that will be passed to the function when it is called.
- Arguments are the actual values that you pass to the function when you call it. They are assigned to the corresponding parameters in the function definition.
parameters and arguments can be of any data type, including numbers, strings, lists, and even other functions. This flexibility allows you to create functions that can work with a wide variety of inputs and perform different tasks based on those inputs.

- Functions can also have default parameter values, which are used if no argument is provided for that parameter when the function is called. This allows you to create functions that can be called with fewer arguments than the number of parameters defined, while still providing a default behavior.
Syntax of a Function with Default Parameter Values:
def function_name(parameter1=default_value1, parameter2=default_value2):
    # Function body
    # Code to be executed
    # Optional return statement


'''

# Example of a Function Definition and Call
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# You can call the function with different arguments to get different outputs
greet("Bob")    # Output: Hello, Bob!

# Example of a Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("The sum of 5 and 3 is:", result)  # Output: The sum of 5 and 3 is: 8


# Define a function that takes 3 parameters and returns their average

def average (x = 0, y = 0, z = 0):
    x = float(x)
    y = float(y)
    z = float(z)
    if (x < 0 or y < 0 or z < 0):
        return "Error: All numbers must be non-negative."
    return (x + y + z) / 3;

    

# Example of calling the average function
print(average(10, 20, 30))  # Output: 20.0
print(average(-5, 10, 15))  # Output: Error: All numbers must be non-negative.
print(average(10, "20", 30))  # Output: 20.0 (the string "20" is converted to a float)