# There are several types of operators in Python:
# 1. Arithmetic Operators: +, -, *, /, %, **, //
# 2. Comparison Operators: ==, !=, >, <, >=, <=
# 3. Logical Operators: and, or, not
# 4. Assignment Operators: =, +=, -=, *=, /=, %=,
# 5. Bitwise Operators: &, |, ^, ~, <<, >>
# 6. Identity Operators: is, is not
# 7. Membership Operators: in, not in
# Example of Arithmetic Operators
a = 10
b = 5
c = a + b
print("Addition:", c)  # Output: 15
c = a - b
print("Subtraction:", c)  # Output: 5
c = a * b
print("Multiplication:", c)  # Output: 50
c = a / b
print("Division:", c)  # Output: 2.0
c = a % b
print("Modulus:", c)  # Output: 0
c = a ** b
print("Exponentiation:", c)  # Output: 100000
c = a // b # Floor Division: // operator returns the quotient of the division, but it rounds down to the nearest whole number.
print("Floor Division:", c)  # Output: 2
# Example of Comparison Operators
x = 10
y = 20
print("Equal to:", x == y)  # Output: False
print("Not equal to:", x != y)  # Output: True
print("Greater than:", x > y)  # Output: False
print("Less than:", x < y)  # Output: True
print("Greater than or equal to:", x >= y)  # Output: False
print("Less than or equal to:", x <= y)  # Output: True
# Example of Logical Operators
p = True
q = False
print("Logical AND:", p and q)  # Output: False
print("Logical OR:", p or q)  # Output: True
print("Logical NOT:", not p)  # Output: False
# Example of Assignment Operators
x = 5
x += 3
print("After += 3:", x)  # Output: 8
x -= 2
print("After -= 2:", x)  # Output: 6
x *= 4
print("After *= 4:", x)  # Output: 24
x /= 6
print("After /= 6:", x)  # Output: 4.0
x %= 3
print("After %= 3:", x)  # Output: 1.0
# Example of Bitwise Operators
a = 5  # In binary: 0101
b = 3  # In binary: 0011
print("Bitwise AND:", a & b)  # Output: 1 (In binary: 0001)
print("Bitwise OR:", a | b)  # Output: 7 (In binary: 0111)
print("Bitwise XOR:", a ^ b)  # Output: 6 (In binary: 0110)
print("Bitwise NOT:", ~a)  # Output: -6 (In binary: 1010)
print("Left Shift:", a << 1)  # Output: 10 (In binary: 1010)
print("Right Shift:", a >> 1)  # Output: 2 (In binary: 0010)
# Example of Identity Operators
x = 5
y = 5
z = 10
print("x is y:", x is y)  # Output: True
print("x is z:", x is z)  # Output: False
print("x is not z:", x is not z)  # Output: True
# Example of Membership Operators
my_list = [1, 2, 3, 4, 5]
print("1 in my_list:", 1 in my_list)  # Output: True
print("6 in my_list:", 6 in my_list)  # Output: False
print("1 not in my_list:", 1 not in my_list)  # Output: False
print("6 not in my_list:", 6 not in my_list)  # Output: True
