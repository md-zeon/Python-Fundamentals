'''
Q1. Ask the user for a string and check whether it is a palindrome or not. 
A palindrome is a string which is same when we read it forward & backward. Eg - 
“madam”, “racecar” etc.

[ Hint- A palindrome string is equal to the reversed version of the string. We can 
use a loop to reverse the string manually. ]
'''
# * Q1 Solution:
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
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)

print("Average:", average)

'''
Q3. Input two lists of integers from the user. Merge them into one list and sort the 
result.
Eg -  list1 = [1, 2, 7],  
list2 = [2, 4, 5]
result = [1, 2, 3, 54, 5, 7]
'''

'''
Q4. Given a tuple of integers, create:
• A tuple of all even numbers
• A tuple of all odd numbers
'''


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


'''
Q6. Given a list of words:
words = ["apple", "banana", "kiwi", "cherry", "mango"]
Create a dictionary that maps each word to its length.
Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...}
'''

'''
Q7. Write a program that takes a string from the user and prints the number of 
spaces in the string.
'''

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