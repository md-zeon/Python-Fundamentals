'''
Types of Constructor:
In Python, there are different types of constructors that can be used to initialize objects of a class. The most common types of constructors are:

1. Default Constructor: A default constructor is a constructor that takes no parameters. It is automatically provided by Python if no constructor is defined in the class. The default constructor initializes the attributes of the object with default values. For example:
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
        self.grade = "N/A"
In this example, the default constructor initializes the name attribute to "Unknown", the age attribute to 0, and the grade attribute to "N/A" when a student object is created without providing any parameters.
'''
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
        self.grade = "N/A"
student1 = Student()
print(student1.name)  # Output: Unknown
print(student1.age)   # Output: 0
print(student1.grade) # Output: N/A

'''
2. Parameterized Constructor: A parameterized constructor is a constructor that takes parameters to initialize the attributes of the object. It allows us to create objects with specific values for their attributes. For example:
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
In this example, the parameterized constructor takes three parameters (name, age, and grade) to initialize the attributes of the student object when it is created.
'''
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
student1 = Student("Alice", 20, "A")
print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20
print(student1.grade) # Output: A
