'''
Inheritance in OOP:
Inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass).
This promotes code reusability and establishes a natural hierarchical relationship between classes.

- it is used for reusing attributes and methods of an existing class.
- it is used to add more features to a class without modifying it.
- it is used to create a relationship between different classes.

Syntax:
class ParentClass:
    # parent class code
class ChildClass(ParentClass):
    # child class code

In Python, inheritance is implemented by defining a new class that takes the name of the parent class in parentheses. The child class can override or extend the functionality of the parent class by defining its own methods or attributes.
The `super()` function is often used in the child class to call the constructor of the parent class, allowing the child class to initialize attributes defined in the parent class.

Syntax for using super():
class ChildClass(ParentClass):
    def __init__(self, args):
        super().__init__(args)  # Call the parent class constructor
        # Additional initialization for the child class

'''

class Employee:
    start_time = "9:00 AM"
    end_time = "5:00 PM"

    def change_start_time(self, new_start_time):
        self.start_time = new_start_time
    
    def change_end_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class Manager(Employee):
    def __init__(self, department):
        self.department = department

t1 = Teacher("Math")
m1 = Manager("HR")
print("Teacher", t1.subject, t1.start_time, t1.end_time)  # Teacher Math 9:00 AM 5:00 PM
print("Manager", m1.department, m1.start_time, m1.end_time)  # Manager HR 9:00 AM 5:00 PM

# In this example, we have a parent class `Employee` with attributes `start_time` and `end_time`, and methods to change these times. The `Teacher` and `Manager` classes inherit from the `Employee` class, allowing them to access the attributes and methods of the parent class while also adding their own specific attributes (`subject` for `Teacher` and `department` for `Manager`).


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color

    def make_sound(self):
        return "Meow!"

# Example usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.name)  # Buddy
print(dog.species)  # Canine
print(dog.breed)  # Golden Retriever
print(dog.make_sound())  # Woof!

print(cat.name)  # Whiskers
print(cat.species)  # Feline
print(cat.color)  # Orange
print(cat.make_sound())  # Meow!

# In this example, we have a parent class `Animal` with attributes `name` and `species`, and a method `make_sound()`. The `Dog` and `Cat` classes inherit from the `Animal` class, allowing them to reuse the attributes and methods defined in the parent class while also adding their own specific attributes and overriding the `make_sound()` method to provide different sounds for dogs and cats.