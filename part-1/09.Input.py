# Taking User Input in Python
#* In Python, you can take user input using the built-in input() function. The input() function reads a line of text from the user and returns it as a string.

# Taking input from the user
name = input("Enter your name: ")
print("Hello, " + name + "!")

# You can also take numerical input from the user, but since input() returns a string, you need to convert it to the appropriate data type (like int or float) using type conversion functions.
age = int(input("Enter your age: ")) # Convert the input string to an integer
# print("You are " + age + " years old.") # This will raise a TypeError because age is an integer and cannot be concatenated with a string. To fix this, we need to convert age back to a string when printing.
print("You are " + str(age) + " years old.") # Convert age back to a string
height = float(input("Enter your height in meters: ")) # Convert the input string to a float
print("Your height is " + str(height) + " meters.")

#! Note: When taking input, it's important to handle exceptions that may arise from invalid input (e.g., entering a non-numeric value when expecting a number). You can use try-except blocks to catch these exceptions and provide feedback to the user.
try:
    age = int(input("Enter your age: "))
    print("You are " + str(age) + " years old.")
except ValueError:
    print("Invalid input. Please enter a valid age.")
try:
    height = float(input("Enter your height in meters: "))
    print("Your height is " + str(height) + " meters.")
except ValueError:
    print("Invalid input. Please enter a valid height.")
