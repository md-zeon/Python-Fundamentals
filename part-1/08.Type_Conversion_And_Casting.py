# Type Conversion in Python

#* Implicit Type Conversion (Type Coercion)
# Python automatically converts one data type to another when necessary.
a = 5       # Integer
b = 3.2     # Float
result = a + b  # a is implicitly converted to float
print("Result of implicit type conversion:", result)  # Output: 8.2

#* Explicit Type Conversion (Type Casting)
# You can manually convert one data type to another using built-in functions.
# The most common functions for type conversion are int(), float(), str(), and bool() etc.
# Converting integer to float
num1 = 10
num1_float = float(num1)
print("Explicitly converted integer to float:", num1_float)  # Output: 10.0
# Converting float to integer
num2 = 5.7
num2_int = int(num2)
print("Explicitly converted float to integer:", num2_int)  # Output: 5

# Converting string to integer
str_num = "42"
int_num = int(str_num)
print("Explicitly converted string to integer:", int_num)  # Output: 42 
# Converting string to float
str_float = "3.14"
float_num = float(str_float)
print("Explicitly converted string to float:", float_num)  # Output: 3.14
# Converting integer to string
num3 = 100
str_num3 = str(num3)
print("Explicitly converted integer to string:", str_num3)  # Output: "100
# Converting float to string
num4 = 2.718
str_num4 = str(num4)
print("Explicitly converted float to string:", str_num4)  # Output: "2.718"
# Note: When converting from float to integer, the decimal part is truncated (not rounded).

# Type conversion can lead to data loss if not done carefully, especially when converting from a higher precision type (like float) to a lower precision type (like int). Always ensure that the conversion is appropriate for the data you are working with.

print("Type of num1_float:", type(num1_float))  # Output: <class 'float'>
print("Type of num2_int:", type(num2_int))      # Output: <class 'int'>
print("Type of int_num:", type(int_num))        # Output: <class 'int'>
print("Type of float_num:", type(float_num))    # Output: <class 'float'>
print("Type of str_num3:", type(str_num3))    # Output: <class 'str'>
print("Type of str_num4:", type(str_num4))    # Output: <class 'str'>

# int to bool
num5 = 0
bool_num5 = bool(num5)
print("Explicitly converted integer to boolean:", bool_num5)  # Output: False   
num6 = 1
bool_num6 = bool(num6)
print("Explicitly converted integer to boolean:", bool_num6)  # Output: True
# float to bool
num7 = 0.0
bool_num7 = bool(num7)
print("Explicitly converted float to boolean:", bool_num7)  # Output: False
num8 = 0.1
bool_num8 = bool(num8)
print("Explicitly converted float to boolean:", bool_num8)  # Output: True

# string to bool
str1 = ""
bool_str1 = bool(str1)
print("Explicitly converted empty string to boolean:", bool_str1)  # Output: False
str2 = "Hello"
bool_str2 = bool(str2)
print("Explicitly converted non-empty string to boolean:", bool_str2)  # Output: True 

# Note: In Python, the following values are considered False when converted to boolean:
# - None
# - False
# - 0 (zero of any numeric type)
# - 0.0 (zero float)
# - 0j (zero complex)
# - Empty sequences and collections (e.g., '', [], {}, set())
# All other values are considered True.