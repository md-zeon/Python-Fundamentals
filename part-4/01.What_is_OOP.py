'''
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior. OOP focuses on the creation of reusable code and the ability to model real-world entities.
The main principles of OOP include:
1. Encapsulation: This principle states that the internal representation of an object should be hidden from the outside. Only the necessary information should be exposed, and the rest should be kept private. This helps to protect the integrity of the data and prevents unintended interference.
2. Inheritance: This allows a new class to inherit properties and behavior from an existing class. The new class, called a subclass, can override or extend the functionality of the parent class. This promotes code reusability and establishes a natural hierarchical relationship between classes.
3. Polymorphism: This principle allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). Polymorphism allows for flexibility and the ability to use objects of different types interchangeably.
4. Abstraction: This principle focuses on hiding the complex implementation details and showing only the necessary features of an object. It allows developers to work with higher-level concepts without needing to understand the intricate details of how they are implemented.
OOP is widely used in software development as it promotes code organization, modularity, and maintainability. It allows developers to create complex systems that are easier to manage and extend over time. Popular programming languages that support OOP include Java, C++, Python, and Ruby.
'''

"""
class: A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. A class can be thought of as a template for creating multiple instances (objects) that share the same structure and behavior.
object: An object is an instance of a class. It is a specific realization of the class, with its own unique state and behavior. An object can have its own values for the attributes defined in the class, and it can call the methods defined in the class to perform actions or manipulate its state. Objects are created from classes and can interact with each other to form complex systems.

We can think of a class as a blueprint for a house, and an object as a specific house built from that blueprint. The class defines the structure and features of the house (e.g., number of rooms, type of roof), while the object represents a particular house with its own unique characteristics (e.g., color, size).

Example:
-------------------------------
|       Class: House          |
-------------------------------
| Attributes:                 |
| - number_of_rooms           |
| - type_of_roof              |
| - color                     |
| - size                      |
| Methods:                    |
| - build()                   |
| - renovate()                |
| - demolish()                |
| - paint()                   |
-------------------------------

Here, the class "House" defines the attributes and methods that any house object will have.
When we create an object from this class, we can assign specific values to the attributes (e.g., number_of_rooms = 3, type_of_roof = "gabled", color = "red", size = "large") and call the methods to perform actions on that particular house object (e.g., my_house.build(), my_house.paint("blue")).

Like this, we can create multiple house objects from the same class, each with its own unique attributes and behavior, while still sharing the common structure defined by the class. This is one of the key advantages of OOP, as it allows for code reusability and modularity.
"""