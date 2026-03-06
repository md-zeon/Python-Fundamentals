'''
Python Strings
Definition: A string is a sequence of characters enclosed in quotes. It can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are immutable, meaning that once they are created, they cannot be changed.
Strings are one of the most commonly used data types in Python and are used to represent text. They can contain letters, numbers, symbols, and whitespace characters. Strings can be manipulated using various built-in methods and operators, making them a powerful tool for handling text data in Python.


'''
# You can create strings in Python using different types of ways. Here are some examples:
# Using single quotes
string1 = 'Hello, World!'
print(string1)
# Using double quotes
string2 = "Python is great!"
print(string2)
# Using triple quotes
string3 = '''This is a multi-line string.'''
print(string3)
# Using triple double quotes
string4 = """This is also a multi-line string."""
print(string4)
# Using escape characters
string5 = 'It\'s a nice day!'
print(string5)
# Using raw strings
string6 = r'C:\Users\Username\Documents'
print(string6)
# Using string concatenation
string7 = string1 + " " + string2
print(string7)
# Using string formatting
name = "Alice"
age = 30
string8 = f"My name is {name} and I am {age} years old."
print(string8)
# Using the format() method
string9 = "My name is {} and I am {} years old.".format(name, age)
print(string9)
# Using the % operator
string10 = "My name is %s and I am %d years old." % (name, age)
print(string10)
# Using string literals
string11 = "This is a string literal."
print(string11)
# Using string slicing
string12 = string1[0:5]  # This will give you 'Hello'
print("Using string slicing:", string12)
# Using string methods
string13 = string1.upper()  # This will convert the string to uppercase
print("Using upper():", string13)
string14 = string1.lower()  # This will convert the string to lowercase
print("Using lower():", string14)
string15 = string1.replace("World", "Python")  # This will replace 'World' with 'Python'
print("Using replace():", string15)
string16 = string1.split(",")  # This will split the string into a list based on the comma
print("Using split():", string16)
string17 = string1.strip()  # This will remove any leading or trailing whitespace
print("Using strip():", string17)
string18 = string1.find("World")  # This will return the index of the first occurrence of 'World'
print("Using find():", string18)
string19 = string1.count("o")  # This will count the number of occurrences of 'o'
print("Using count():", string19)
string20 = string1.startswith("Hello")  # This will check if the string starts with 'Hello'
print("Using startswith():", string20)
string21 = string1.endswith("!")  # This will check if the string ends with '!'
print("Using endswith():", string21)
string22 = string1.isalpha()  # This will check if the string contains only alphabetic characters
print("Using isalpha():", string22)
string23 = string1.isdigit()  # This will check if the string contains only digits
print("Using isdigit():", string23)
string24 = string1.isalnum()  # This will check if the string contains only alphanumeric characters
print("Using isalnum():", string24)
string25 = string1.isspace()  # This will check if the string contains only whitespace characters
print("Using isspace():", string25)
string26 = string1.title()  # This will convert the string to title case
print("Using title():", string26)
string27 = string1.capitalize()  # This will capitalize the first character of the string
print("Using capitalize():", string27)
string28 = string1.center(20)  # This will center the string within a field of width 20
print("Using center():", string28)
string29 = string1.ljust(20)  # This will left-justify the string within a field of width 20
print("Using ljust():", string29)
string30 = string1.rjust(20)  # This will right-justify the string within a field of width 20
print("Using rjust():", string30)
string31 = string1.zfill(20)  # This will pad the string with zeros on the left to fill a width of 20
print("Using zfill():", string31)
string32 = string1.encode()  # This will encode the string into bytes
print("Using encode():", string32)
# string33 = string1.decode()  # This will decode the bytes back into a string
# print("Using decode():", string33)
string34 = string1.islower()  # This will check if all characters in the string are lowercase
print("Using islower():", string34)
string35 = string1.isupper()  # This will check if all characters in the string are uppercase
print("Using isupper():", string35)
string36 = string1.isnumeric()  # This will check if all characters in the string are numeric
print("Using isnumeric():", string36)
string37 = string1.isdecimal()  # This will check if all characters in the string are decimal characters
print("Using isdecimal():", string37)
string38 = string1.isidentifier()  # This will check if the string is a valid identifier
print("Using isidentifier():", string38)
string39 = string1.isprintable()  # This will check if all characters in the string are printable
print("Using isprintable():", string39)
string40 = string1.isascii()  # This will check if all characters in the string are ASCII characters
print("Using isascii():", string40)