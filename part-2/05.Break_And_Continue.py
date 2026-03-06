'''
Break and Continue Statements

In Python, the `break` and `continue` statements are used to control the flow of loops.
- The `break` statement is used to exit a loop prematurely. When the `break` statement is executed, the loop is immediately terminated, and the program continues with the next statement after the loop.
- The `continue` statement is used to skip the current iteration of a loop and move on to the next iteration. When the `continue` statement is executed, the rest of the code inside the loop for that iteration is skipped, and the loop proceeds to the next iteration.
'''
# Example of break statement
while True:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # Exit the loop when the user types 'exit'
    else:
        print(f"You entered: {user_input}")

# Example of continue statement
multiples_of_num = int(input("Enter a number to find its multiples: "))
print(f"Multiples of {multiples_of_num} from 1 to 100:")
i = 1
while i <= 100:
    if i % multiples_of_num != 0:
        i += 1
        continue  # Skip the current iteration if i is not a multiple of multiples_of_num
    print(i, end=' ')
    i += 1