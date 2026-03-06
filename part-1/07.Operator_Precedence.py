# Operator Precedence => priority of operators in an expression
# Higher precedence operators are evaluated before lower precedence operators
# If operators have the same precedence, they are evaluated from left to right

# From highest to lowest precedence:
# 1. Parentheses ()
# 2. Exponentiation (**)
# 3. Multiplication (*), Division (/), Floor Division (//), Modulus (%)
# 4. Addition (+), Subtraction (-)
# 5. Comparison Operators (==, !=, >, <, >=, <=)
# 6. Logical not
# 7. Logical and
# 8. Logical or

# Example:
result = 3 + 4 * 2 / (1 - 5) ** 2
# Step 1: Parentheses (1 - 5) => -4
# Step 2: Exponentiation (-4) ** 2 => 16
# Step 3: Multiplication and Division 4 * 2 => 8, then 8 / 16 => 0.5
# Step 4: Addition 3 + 0.5 => 3.5
print(result)  # Output: 3.5

# To change the order of evaluation, we can use parentheses:
result = (3 + 4) * 2 / (1 - 5) ** 2
# Step 1: Parentheses (3 + 4) => 7, (1 - 5) => -4
# Step 2: Exponentiation (-4) ** 2 => 16
# Step 3: Multiplication and Division 7 * 2 => 14, then 14 / 16 => 0.875
print(result)  # Output: 0.875

# Example with comparison and logical operators:
x = 5
y = 10
result = x < y and (x + 2) > 6
# Step 1: Parentheses (x + 2) => 7
# Step 2: Comparison x < y => True, (x + 2) > 6 => True
# Step 3: Logical and True and True => True
print(result)  # Output: True

# Example with all logical operators:
a = True
b = False
c = True
result = a and b or c
# Step 1: Logical and a and b => True and False => False
# Step 2: Logical or False or True => True
print(result)  # Output: True

