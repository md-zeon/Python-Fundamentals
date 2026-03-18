'''
Abstraction is the process of hiding the implementation details and showing only the functionality to the user. It is one of the fundamental principles of object-oriented programming (OOP) that allows us to focus on what an object does rather than how it does it.
In Python, abstraction can be achieved using abstract classes and interfaces. An abstract class is a class that cannot be instantiated and is meant to be subclassed. It can contain abstract methods, which are methods that are declared but not implemented in the abstract class. Subclasses of the abstract class must provide an implementation for the abstract methods.
To create an abstract class in Python, we can use the `abc` module, which provides the `ABC` class and the `abstractmethod` decorator. Here's an example of how to create an abstract class and use it:
'''
# Start by importing the necessary components from the `abc` module:
from abc import ABC, abstractmethod
# Here abc is the module that provides the infrastructure for defining abstract base classes in Python. ABC stands for Abstract Base Class, and it is a class that cannot be instantiated and is meant to be subclassed. 
# The abstractmethod decorator is used to declare a method as abstract, which means that it must be implemented by any subclass of the abstract class.

# Next, we can define an abstract class by inheriting from the ABC class:
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
# In this example, we have defined an abstract class called Shape that has an abstract method called area. The area method is declared as abstract using the @abstractmethod decorator, which means that any subclass of Shape must provide an implementation for the area method.

# Now, we can create a subclass of the Shape class and provide an implementation for the area method:
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
# In this example, we have created a subclass called Circle that inherits from the Shape class. We have implemented the area method to calculate the area of a circle using the formula A = πr^2.

# Finally, we can create an instance of the Circle class and call the area method:
circle = Circle(5)
print(circle.area()) # Output: 78.5
# In this example, we have created an instance of the Circle class with a radius of 5 and called the area method to calculate and print the area of the circle. The output will be: 78.5
# In summary, abstraction allows us to hide the implementation details of a class and focus on the functionality it provides. By using abstract classes and methods, we can create a clear and organized structure for our code, making it easier to maintain and extend in the future.