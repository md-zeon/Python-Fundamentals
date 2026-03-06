# Calculate the average of 2 numbers
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit() # Exit the program if the input is invalid
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()
average = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is:", average)
