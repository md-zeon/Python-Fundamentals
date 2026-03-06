'''
String Formating in Python allows you to create formatted strings by embedding expressions inside string literals. There are several ways to format strings in Python, including using the % operator, the str.format() method, and f-strings (formatted string literals). Each method provides a different way to insert values into a string.
1. format() method:
The str.format() method allows you to format strings by using placeholders defined by curly braces {}. You can specify the position of the arguments or use named placeholders.
With the format() method, you can also specify formatting options such as width, precision, and alignment.

2. f-strings:
F-strings, introduced in Python 3.6, provide a more concise and readable way to format strings. They are defined by prefixing the string with the letter 'f' and using curly braces {} to embed expressions directly within the string.

3. % operator:
The % operator is an older method of string formatting that uses format specifiers to indicate the type of value being inserted into the string. It is less flexible than the format() method and f-strings but is still supported in Python for backward compatibility.
'''
# Example of using the format() method
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Example of using the format() method with named placeholders
print("My name is {name} and I am {age} years old.".format(name=name, age=age))

# Example of using the format() method with indexed placeholders
print("My name is {0} and I am {1} years old. {0} is a common name.".format(name, age))

# Example of using f-strings
name = "Bob"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Example of using the % operator (old-style string formatting)
name = "Charlie"
age = 35
print("My name is %s and I am %d years old." % (name, age))