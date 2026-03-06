'''
String slicing is a powerful technique in Python that allows you to extract a portion of a string by specifying a range of indices. The syntax for string slicing is as follows:
string[start:stop:step]
- start: The index where the slice starts (inclusive). If omitted, it defaults to 0.
- stop: The index where the slice ends (exclusive). If omitted, it defaults to the length of the string.
- step: The step size or the interval between characters to be included in the slice. If omitted, it defaults to 1.
'''
# Example of string slicing
string1 = 'Hello, World!'
# Extracting a substring from index 0 to 5 (exclusive)
substring1 = string1[0:5]  # This will give you 'Hello'
print(string1, "sliced from index 0 to 5:", substring1)
# Extracting a substring from index 7 to the end of the string
substring2 = string1[7:]  # This will give you 'World!'
print(string1, "sliced from index 7 to the end:", substring2)
# Extracting a substring from the beginning of the string to index 5 (exclusive)
substring3 = string1[:5]  # This will give you 'Hello'
print(string1, "sliced from the beginning to index 5:", substring3)
# Extracting a substring with a step of 2
substring4 = string1[::2]  # This will give you 'Hlo ol!'
print(string1, "sliced with a step of 2:", substring4)
# Extracting a substring in reverse order
substring5 = string1[::-1]  # This will give you '!dlroW ,olleH'
print(string1, "sliced in reverse order:", substring5)
# Extracting a substring from index 2 to index 10 with a step of 3
substring6 = string1[2:10:3]  # This will give you 'loW'
print(string1, "sliced from index 2 to 10 with a step of 3:", substring6)
# Extracting a substring from index 5 to index 0 in reverse order
substring7 = string1[5:0:-1]  # This will give you ', ol'
print(string1, "sliced from index 5 to 0 in reverse order:", substring7)
# Extracting a substring from index 10 to index 2 in reverse order
substring8 = string1[10:2:-1]  # This will give you 'roW ,o'
print(string1, "sliced from index 10 to 2 in reverse order:", substring8)

