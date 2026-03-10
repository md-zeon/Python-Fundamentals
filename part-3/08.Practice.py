'''
# Student Enrollments
Given a list of tuples with info (name, subject):
 - list all unique courses
 - list students enrolled in English
 - create a dictionary (student, set of courses)
'''
info = [
    ("Alice", "Math"),
    ("Bob", "English"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Charlie", "English"),
]

# List all unique courses
unique_courses = set()
print("Unique courses:", end=" ")
for student, course in info:
    unique_courses.add(course)
print(unique_courses)

# List students enrolled in English
print("Students enrolled in English: ", end=" ")
for student, course in info:
    if course == "English":
        print("[" + student + "]", end=" ")
print()

# Create a dictionary (student, set of courses)

enrollments = {}

for student, course in info:
    if student not in enrollments:
        enrollments[student] = set()
    enrollments[student].add(course)

print("Enrollments:", enrollments)