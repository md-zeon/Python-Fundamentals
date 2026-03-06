# Conditional Statements (Match-Case) in Python
# Match-case statement (introduced in Python 3.10)

# Example of match-case statement
traffic_light = "red"
match traffic_light:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid traffic light color")

'''
Match-case statements provide a more elegant and readable way to handle multiple conditions
compared to traditional if-elif-else statements. They allow you to match patterns and execute code
based on the structure of the data, making it easier to write complex conditional logic.
In the example above, we use a match-case statement to determine the action based on the color of the traffic light.
The underscore (_) is used as a wildcard to catch any cases that do not match the specified patterns, similar to the else statement in an if-elif-else structure.
'''