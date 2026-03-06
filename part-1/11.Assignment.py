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

'''
Q6. Write a program to swap values of two numbers entered by the user.
'''

'''
Q7. Ask the user for a temperature in Celsius (string input). Convert it to float, 
then calculate and print temperature in Fahrenheit. 
float 
Conversion formula: FahrenheitTemp = (CelsiusTemp * (9/5)) + 32 
'''

'''
Q8. Take the radius (r) as user input and print the area. 
Use the formula:  Area = π * r2   (value of π = 3.14) 
'''

'''
Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and 
compute simple interest: 
SI = (P * R * T )/100 
'''


'''
Q10. Take a decimal number as input (like 45.78) and output its: 
• integer part - 45 
• fractional part - .78
'''