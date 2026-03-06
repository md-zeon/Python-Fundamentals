'''
Lambda Functions:
Lambda functions, also known as anonymous functions, are a concise way to create small, one-line functions without needing to define a full function using the `def` keyword. They are defined using the `lambda` keyword followed by a list of parameters, a colon, and an expression. The expression is evaluated and returned when the lambda function is called.

Syntax:
lambda arguments: expression

Example:
add = lambda x, y: x + y
'''

sum = lambda a, b: a + b

print(sum(5, 3))  # Output: 8

avg = lambda a, b, c: (a + b + c) / 3
print(avg(10, 20, 30))  # Output: 20.0

'''
Higher-Order Functions:
Lambda functions are often used in conjunction with higher-order functions like `map()`, `filter()`, and `reduce()` to perform operations on collections of data.
Example with map():
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
'''