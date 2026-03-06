'''
Assignment Problems 
Q1. Write a program that asks the user for their name and age, then prints a 
sentence like: 
Hello Shradha, you are 21 years old! 
'''
# * Q1 Solution:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name + ",", "you are", age, "years old!")


'''
Q2. Take two numbers as input from the user and print their sum, difference, 
product, and quotient. 
'''
# * Q2 Solution:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

'''
Q3. Ask the user to enter two integers and one float. Convert them all to floats 
and print their average. 
'''
# * Q3 Solution:
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
float_num = float(input("Enter a float: "))

average = (float(int1) + float(int2) + float_num) / 3
print("The average is:", average)

'''
Q4. The user enters a string containing a number (e.g., "45"). Convert it to: 
• an integer 
• a float 
• a string again 
Print all three values with their types.
'''
# * Q4 Solution:
num = input("Enter a number: ")
num = int(num)  # Convert to integer
print("Integer:", num, "Type:", type(num))
num = float(num)  # Convert to float
print("Float:", num, "Type:", type(num))
num = str(num)  # Convert back to string
print("String:", num, "Type:", type(num))


'''
Q5. Evaluate and print the result of the following expression: 
x = 10 + 3 * 2 ** 2 
Based on what you learnt in the lecture explain why the output is what it is. 
'''
# * Q5 Solution:
x = 10 + 3 * 2 ** 2
print("Result:", x)
# * Explanation:
# The expression is evaluated based on the order of operations (PEMDAS/BODMAS):
# 1. Parentheses: There are no parentheses to evaluate first.
# 2. Exponents: 2 ** 2 = 4
# 3. Multiplication: 3 * 4 = 12
# 4. Addition: 10 + 12 = 22

'''
Q6. Write a program to swap values of two numbers entered by the user.
'''
# * Q6 Solution:
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# * Swapping the values (using a temporary variable)
temp = num1
num1 = num2
num2 = temp
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

# * Alternative swapping without a temporary variable:
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1, num2 = num2, num1  # Swapping using tuple unpacking
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

# * Alternative swapping using arithmetic operations (only works for numbers):
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num1 = num1 + num2  # Step 1: num1 now holds the sum of num1 and num2
num2 = num1 - num2  # Step 2: num2 now holds the original value of num1
num1 = num1 - num2  # Step 3: num1 now holds the original value of num2
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

# ! Note: The arithmetic swapping method can lead to issues with floating-point precision and is not recommended for large numbers or non-numeric inputs.

# * Alternative swapping using XOR (only works for integers):
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num1 = num1 ^ num2  # Step 1: num1 now holds the result of num1 XOR num2
num2 = num1 ^ num2  # Step 2: num2 now holds the original value of num1
num1 = num1 ^ num2  # Step 3: num1 now holds the original value of num2
print("After swapping:")
print("First integer:", num1)
print("Second integer:", num2)


# ! Note: The XOR swapping method is a bitwise operation and can be less intuitive than using a temporary variable or tuple unpacking. It also only works for integers.
'''
Q7. Ask the user for a temperature in Celsius (string input). Convert it to float, 
then calculate and print temperature in Fahrenheit. 
 
Conversion formula: FahrenheitTemp = (CelsiusTemp * (9/5)) + 32 
'''
# * Q7 Solution:
celsius_temp = input("Enter temperature in Celsius: ")
fahrenheit_temp = (float(celsius_temp) * (9/5)) + 32
print("Temperature in Fahrenheit:", fahrenheit_temp)


'''
Q8. Take the radius (r) as user input and print the area. 
Use the formula:  Area = π * r2   (value of π = 3.14) 
'''
# * Q8 Solution:
radius = input("Enter the radius: ")
area = 3.14 * (float(radius) ** 2)
print("Area of the circle:", area)

'''
Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and 
compute simple interest: 
SI = (P * R * T )/100 
'''
# * Q9 Solution:
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

'''
Q10. Take a decimal number as input (like 45.78) and output its: 
• integer part - 45 
• fractional part - .78
'''