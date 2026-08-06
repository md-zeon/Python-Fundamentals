'''
Q1. Create a program that:
1. Opens a file "names.txt" in write mode
2. Writes 5 names (one per line) entered by the user
3. Then opens the same file in read mode and prints all names
'''
# Step 1: Open the file in write mode and write names
with open("names.txt", "w") as file:
    for i in range(5):
        name = input("Enter a name: ")
        file.write(name + "\n")

# Step 2: Open the file in read mode and print all names
with open("names.txt", "r") as file:
    print("Names in the file:")
    for line in file:
        print(line.strip())