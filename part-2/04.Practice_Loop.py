# Print numbers from 5 to 1
i = 5
while i >= 1:
    print(i, end=' ')
    i -= 1

# Multiplication Table
num = int(input("\nEnter a number: "))
print(f"Multiplication Table of {num}:")

i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

