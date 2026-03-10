'''
Q1. Ask the user for a string and check whether it is a palindrome or not. 
A palindrome is a string which is same when we read it forward & backward. Eg - 
“madam”, “racecar” etc.

[ Hint- A palindrome string is equal to the reversed version of the string. We can 
use a loop to reverse the string manually. ]
'''
# * Q1 Solution:
def answer_q1():
    # Method 1: Using a loop to reverse the string manually
    string = input("Enter a string: ")
    reversed_string = "";

    for c in string:
        reversed_string = c + reversed_string;

    if (string == reversed_string):
        print("Given String is a palindrome");
    else:
        print("Given String is not a palindrome");

    # Method 2: Using slicing to reverse the string
    string = input("Enter a string: ")
    reversed_string = string[::-1];
    if (string == reversed_string):
        print("Given String is a palindrome");
    else:
        print("Given String is not a palindrome");

    # Method 3: Using two pointers to compare characters from both ends of the string
    string = input("Enter a string: ")
    i = 0;
    j = len(string) - 1;
    is_palindrome = True;
    while (i < j):
        if (string[i] != string[j]):
            is_palindrome = False;
            break;
        i += 1;
        j -= 1;

    if (is_palindrome):
        print("Given String is a palindrome");
    else:
        print("Given String is not a palindrome");

    # Method 4: Using built-in function reversed() to reverse the string
    string = input("Enter a string: ")
    reversed_string = ''.join(reversed(string));
    if (string == reversed_string):
        print("Given String is a palindrome");
    else:
        print("Given String is not a palindrome");


'''
Q2. Given a list of integers compute the average of all numbers in the list.
'''

# * Q2 Solution:
def answer_q2():
    numbers = [1, 2, 3, 4, 5]
    average = sum(numbers) / len(numbers)

    print("Average:", average)

'''
Q3. Input two lists of integers from the user. Merge them into one list and sort the 
result.
Eg -  list1 = [1, 2, 7],  
list2 = [3, 4, 5]
result = [1, 2, 3, 4, 5, 7]
'''

# * Q3 Solution:
def answer_q3():
    # Method 1: Using the + operator to merge and sort() method to sort the list
    list1 = list(map(int, input("Enter the first list of integers (space-separated): ").split()))
    list2 = list(map(int, input("Enter the second list of integers (space-separated): ").split()))
    merged_list = list1 + list2
    merged_list.sort()

    # Method 2: using input() and a loop to take input for both lists, then merging and sorting
    list1 = []
    list2 = []
    n1 = int(input("Enter the number of elements in the first list: "))
    for i in range(n1):
        num = int(input(f"Enter element {i+1} for the first list: "))
        list1.append(num)

    n2 = int(input("Enter the number of elements in the second list: "))
    for i in range(n2):
        num = int(input(f"Enter element {i+1} for the second list: "))
        list2.append(num)

    merged_list = list1 + list2
    merged_list.sort()

    print("Merged and sorted list:", merged_list);

'''
Q4. Given a tuple of integers, create:
• A tuple of all even numbers
• A tuple of all odd numbers
'''
# * Q4 Solution:
def answer_q4():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    even_numbers = ()
    odd_numbers = ()
    for num in numbers:
        if (num % 2 == 0):
            even_numbers += (num,);
        else:
            odd_numbers += (num,);

    print("Even numbers:", even_numbers);
    print("Odd numbers:", odd_numbers);

# answer_q4();

'''
Q5. Create a dictionary where:
• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) 
depending on the operation they want to perform on the dictionary:
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks
'''
def answer_q5():
    students = {}
    while True:
        print("Menu:")
        print("A - Add a student")
        print("B - Update marks")
        print("C - Search for a student")
        print("D - Display all students and marks")
        print("E - Exit")

        choice = input("Enter your choice: ").upper()

        if (choice == 'A'):
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            students[name] = marks
            print(f"Student {name} added with marks {marks}.")

        elif (choice == 'B'):
            name = input("Enter student name to update marks: ")
            if (name in students):
                marks = int(input("Enter new marks: "))
                students[name] = marks
                print(f"Marks for student {name} updated to {marks}.")
            else:
                print(f"Student {name} not found.")

        elif (choice == 'C'):
            name = input("Enter student name to search: ")
            if (name in students):
                print(f"Student {name} has marks {students[name]}.")
            else:
                print(f"Student {name} not found.")

        elif (choice == 'D'):
            if (students):
                print("Students and their marks:")
                for name, marks in students.items():
                    print(f"{name}: {marks}")
            else:
                print("No students found.")

        elif (choice == 'E'):
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# answer_q5();


'''
Q6. Given a list of words:
words = ["apple", "banana", "kiwi", "cherry", "mango"]
Create a dictionary that maps each word to its length.
Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...}
'''
# * Q6 Solution:
def answer_q6():
    words = ["apple", "banana", "kiwi", "cherry", "mango"]
    word_length_dict = {}
    for word in words:
        word_length_dict[word] = len(word)
    print(word_length_dict)

# answer_q6()

'''
Q7. Write a program that takes a string from the user and prints the number of 
spaces in the string.
'''
# * Q7 Solution:
def answer_q7():
    string = input("Enter a string: ")
    space_count = string.count(' ')
    print(f"Number of spaces in the string: {space_count}")

answer_q7()

'''
Q8. Write a program to check whether two lists share no common elements. 
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]
'''

'''
Q9. Given a list, print all elements that appear more than once in the list.
'''

'''
Q10. Ask the user for a string and print:
• All unique characters
• The count of unique characters
'''