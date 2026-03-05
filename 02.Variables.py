# Variable: A variable is a container for storing data values. In Python, you can create a variable and assign it a value using the assignment operator (=). The name of the variable should follow certain rules, such as starting with a letter or an underscore, and it cannot contain spaces or special characters.
age = 30
name = "John"
# You can also assign multiple variables in one line:
x, y, z = 1, 2, 3
# Variables can hold different types of data, such as integers, floats, strings, lists, etc. You can also change the value of a variable after it has been assigned.
age = 31  # Now the variable 'age' holds a new value
name = "Jane"  # Now the variable 'name' holds a new value
# It's important to choose meaningful variable names that describe the data they hold, as this makes your code easier to read and understand.


# In Memory:
# When you create a variable in Python, it is stored in memory. The variable name is a reference to the location in memory where the value is stored. When you assign a new value to a variable, the reference is updated to point to the new location in memory where the new value is stored. This is why variables can hold different types of data and can be changed throughout the program.

# Example:
x = 10  # 'x' points to the memory location where the value 10 is stored
x = "Hello"  # Now 'x' points to a new memory location where the string "Hello" is stored
# In Python, variables are dynamically typed, which means that you don't need to declare the type of a variable when you create it. The type of the variable is determined at runtime based on the value assigned to it. This allows for flexibility in your code, but it also means that you need to be careful when working with variables to avoid type-related errors.

# here x is known as an identifier, which is the name given to a variable, function, class, or other object in Python. An identifier must follow certain rules:
# It must start with a letter (a-z, A-Z) or an underscore (_).
# It can be followed by letters, digits (0-9), or underscores.
# It cannot be a reserved keyword in Python (such as 'if', 'for', 'while', etc.).

# Examples of valid identifiers:
my_variable = 10
_name = "Alice"
age2 = 25

# Examples of invalid identifiers:
# 2age = 30  # Cannot start with a digit
# my-variable = 5  # Cannot contain a hyphen
# In summary, variables are essential for storing and manipulating data in Python. They allow you to create dynamic and flexible programs by enabling you to change the values they hold throughout the execution of your code.