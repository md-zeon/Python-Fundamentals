'''
Polymorphism in Python
Poly => many
morph => form

Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying data types or classes. In Python, polymorphism can be achieved through method overriding and duck typing.

many forms => same name but different forms

There are two main types of polymorphism in Python:
1. Method Overriding: This occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass overrides the method in the superclass, allowing for different behavior while maintaining the same interface.
2. Duck Typing: This is a dynamic typing feature in Python where the type of an object is determined by its behavior (methods and properties) rather than its class. If an object implements the required methods, it can be used in place of another object, regardless of their class.

Operator Overloding (Polymorphism example)
In Python, operators can be overloaded to perform different operations based on the types of operands. For example, the '+' operator can be used to add two numbers or concatenate two strings, demonstrating polymorphism in action.

1. Function Overriding (inheritence): defining parent class method in child class
2. Duck Typing (Works on the idea: “If it looks like a duck and quacks like a duck, it must be a duck.”)

'''

# Function Overriding
class Employee:
    def get_designation(self):
        print("designation = Employee");

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher");

t1 = Teacher()
t1.get_designation()


# Duck Typing
class Dog:  
    def speak(self):  
        print("Bark")  
class Cat:  
    def speak(self): 
        print("Meow")  
class Robot:  
    def speak(self):  
        print("Beep Boop")  
def make_it_speak(entity):  
    entity.speak()  # doesn’t care about type  

d = Dog()  
c = Cat()  
r = Robot()  
for e in [d, c, r]:  
    make_it_speak(e)

# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses the overloaded + operator
print(p3)  # Output: (4, 6)

str1 = p1.__str__()  # Uses the __str__ method to convert to string
print(str1)  # Output: (1, 2)