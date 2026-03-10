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
for student, course in info:
    unique_courses.add(course)
print(unique_courses)
