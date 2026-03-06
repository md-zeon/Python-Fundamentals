'''
While Loop
A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The loop will continue to execute as long as the condition evaluates to true. Once the condition becomes false, the loop will stop executing.
Syntax:
while condition:
    # code to be executed
'''

# * Example of a while loop that prints numbers from 1 to 5

count = 1 # counter variable for tracking the current count of the loop
while count <= 5:
    print(count, end=' ')  # Print the current count followed by a space
    count += 1  # Increment the count to avoid an infinite loop

# ! Caution: Be careful with while loops, as they can lead to infinite loops if the condition never becomes false. Always ensure that there is a way for the loop to terminate.

# * Example of an infinite loop (do not run this code)
# while True:
#     print("This will run forever!")

# * To break out of an infinite loop, you can use the 'break' statement we will learn about in the next section.