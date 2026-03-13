'''
Classes and Objects in Python
class: A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. A class can be thought of as a template for creating multiple instances (objects) that share the same structure and behavior.
object: An object is an instance of a class. It is a specific realization of the class, with its own unique state and behavior. An object can have its own values for the attributes defined in the class, and it can call the methods defined in the class to perform actions or manipulate its state. Objects are created from classes and can interact with each other to form complex systems.

class does not consume any memory, but when we create an object from a class, it allocates memory to store the attributes and methods defined in the class. Each object can have its own unique values for the attributes, allowing for flexibility and customization.
Example:
-------------------------------
|       Class: Student        |
-------------------------------
| Attributes:                 |
| - name                      |
| - age                       |
| - grade                     |
| - school_name               |
| Methods:                    |
| - study()                   |
| - take_exam()               |
| - get_grade()               |
-------------------------------
Here, the class "Student" defines the attributes and methods that any student object will have.
When we create an object from this class, we can assign specific values to the attributes (e.g., name = "Alice", age = 20, grade = "A", school_name = "ABC High School") and call the methods to perform actions on that particular student object (e.g., student1.study(), student1.take_exam(), student1.get_grade()).

Like this, we can create multiple student objects from the same class, each with its own unique attributes and behavior, while still sharing the common structure defined by the class. This is one of the key advantages of OOP, as it allows for code reusability and modularity.
'''


'''
Syntax for defining a class in Python:
class ClassName:
    # class body
    # attributes and methods
'''

class Student:
    # class attributes (shared by all instances)
    school_name = "ABC High School"
    name = ""
    age = 0
    grade = ""

    # method to simulate studying
    def study(self):
        print(f"{self.name} is studying.")

    # method to simulate taking an exam
    def take_exam(self):
        print(f"{self.name} is taking an exam.")

    # method to get the student's grade
    def get_grade(self):
        return self.grade
    

'''
Syntax for creating an object (instance) of a class in Python:
object_name = ClassName()
'''

# Creating an object (instance) of the Student class
student1 = Student()
student1.name = "Alice"
student1.age = 20
student1.grade = "A"
# Accessing attributes and calling methods on the student1 object
print(f"Student Name: {student1.name}")
print(f"Student Age: {student1.age}")
print(f"Student Grade: {student1.get_grade()}")
student1.study()
student1.take_exam()

# Creating another object (instance) of the Student class
student2 = Student()
student2.name = "Bob"
student2.age = 22
student2.grade = "B"
# Accessing attributes and calling methods on the student2 object
print(f"Student Name: {student2.name}")
print(f"Student Age: {student2.age}")
print(f"Student Grade: {student2.get_grade()}")
student2.study()
student2.take_exam()

print(student1) # <__main__.Student object at 0x000001F5870786E0>
print(student2) # <__main__.Student object at 0x000001F58707C550>
