# Conditional Statements in Python

# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# if-elif-else statement
z = 7
if z < 5:
    print("z is less than 5")
elif z == 5:
    print("z is equal to 5")
else:
    print("z is greater than 5")

# Nested if statements
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")
    else:
        print("a is greater than or equal to 20")

# Traffic light example
traffic_light = "red"
if traffic_light == "red":
    print("Stop")
elif traffic_light == "yellow":
    print("Get ready")
elif traffic_light == "green":
    print("Go")
else:
    print("Invalid traffic light color")

# Check if a number is even or odd
number = 8
if number % 2 == 0:
    print(f"{number} is even") # f-string for formatted string literals
else:
    print(f"{number} is odd") # f-string for formatted string literals

# Login system example
username = "admin"
password = "password123"
input_username = input("Enter username: ")
input_password = input("Enter password: ")
if input_username == username and input_password == password:
    print("Login successful")
else:
    print("Login failed")

