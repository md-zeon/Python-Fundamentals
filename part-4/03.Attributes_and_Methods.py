'''
Attributes and Methods
In Python, attributes are variables that belong to an object, while methods are functions that belong to an object.
Attributes can be accessed and modified using dot notation. For example, if we have a class called "Person" with an attribute called "name", we can create an instance of the class and access the attribute like this:
class Person:
    name = "John" # This is an attribute
    __init__(self, name, age):
        self.name = name # This is an instance attribute
        self.age = age # This is another instance attribute

person1 = Person("Alice", 30) # Create an instance of the Person class
print(person1.name) # Access the attribute using dot notation
print(person1.age) # Access the age attribute using dot notation

Methods are functions that belong to an object and can be called using dot notation. For example, if we have a method called "greet" in the "Person" class, we can call it like this:
class Person:
    name = "John" # This is an attribute
    __init__(self, name, age):
        self.name = name # This is an instance attribute
        self.age = age # This is another instance attribute

    def greet(self): # This is a method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person1 = Person("Alice", 30) # Create an instance of the Person class
person1.greet() # Call the greet method using dot notation
'''

class Person:
    name = "John" # This is an attribute
    def __init__(self, name, age):
        self.name = name # This is an instance attribute
        self.age = age # This is another instance attribute

    def greet(self): # This is a method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person1 = Person("Alice", 30) # Create an instance of the Person class
print(person1.name) # Access the attribute using dot notation
print(person1.age) # Access the age attribute using dot notation
person1.greet() # Call the greet method using dot notation
