'''
Methods in Python
- Methods are functions that are defined within a class and are used to perform specific actions on objects of that class.
- Methods are defined using the def keyword, just like regular functions, but they must be indented within the class definition.
- The first parameter of a method is always self, which refers to the instance of the class that the method is being called on. This allows the method to access and modify the attributes of the instance. For example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

In this example, the display_info method is defined within the Student class and takes self as its first parameter. The method uses self to access the name and age attributes of the instance and prints them out.
- Methods can also take additional parameters besides self, which can be used to perform specific actions on the instance. For example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update_age(self, new_age):
        self.age = new_age
In this example, the update_age method takes an additional parameter new_age, which is used to update the age attribute of the instance.
- Methods can be called on an instance of a class using dot notation. For example:
student1 = Student("Alice", 20)
student1.display_info()  # Output: Name: Alice, Age: 20
student1.update_age(21)
student1.display_info()  # Output: Name: Alice, Age: 21
In this example, the display_info method is called on the student1 instance to display its information, and then the update_age method is called to update the age attribute of the student1 instance. Finally, the display_info method is called again to show the updated information.
- Methods can also return values using the return keyword. For example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
In this example, the get_info method returns a string containing the name and age of the instance. This allows us to retrieve information about the instance without directly accessing its attributes. For example:
student1 = Student("Alice", 20)
info = student1.get_info()
print(info)  # Output: Name: Alice, Age: 20
In summary, methods are an essential part of object-oriented programming in Python. They allow us to define specific actions that can be performed on objects of a class, making our code more organized and efficient.
'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def update_age(self, new_age):
        self.age = new_age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
student1 = Student("Alice", 20)
student1.display_info()  # Output: Name: Alice, Age: 20
student1.update_age(21)
student1.display_info()  # Output: Name: Alice, Age: 21
info = student1.get_info()
print(info)  # Output: Name: Alice, Age: 21


'''
Methods can also be defined as class methods or static methods using the @classmethod and @staticmethod decorators, respectively. 
- Class methods take the class itself as the first parameter (usually named cls) and can be used to access and modify class attributes.
- Static methods do not take any special first parameter and are used for utility functions that do not need to access instance or class attributes. For example:
class Student:
    school_name = "ABC School"

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod
    def is_adult(age):
        return age >= 18
In this example, the get_school_name method is a class method that returns the name of the school, while the is_adult method is a static method that checks if a given age is considered an adult. We can call these methods as follows:
print(Student.get_school_name())  # Output: ABC School
print(Student.is_adult(20))  # Output: True
print(Student.is_adult(15))  # Output: False

Instance vs Class vs Static Methods
- Instance methods are the most common type of method and are defined with self as the first parameter. They can access and modify instance attributes and are called on instances of the class.
- Class methods are defined with cls as the first parameter and can access and modify class attributes. They are called on the class itself rather than on instances.
- Static methods do not take any special first parameter and are used for utility functions that do not need to access instance or class attributes. They can be called on the class itself or on instances of the class, but they do not have access to the instance or class attributes.
In summary, methods in Python are functions that are defined within a class and are used to perform specific actions on objects of that class. They can be instance methods, class methods, or static methods, each serving different purposes in object-oriented programming. Understanding how to define and use methods is essential for writing efficient and organized code in Python.
'''

class Student:
    school_name = "ABC School"

    def __init__(self, name, age): # Instance method
        self.name = name
        self.age = age

    def display_info(self): # Instance method
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def get_school_name(cls): # Class method
        return cls.school_name

    @staticmethod 
    def is_adult(age): # Static method
        return age >= 18
student1 = Student("Alice", 20)
student1.display_info()  # Output: Name: Alice, Age: 20
print(Student.get_school_name())  # Output: ABC School
print(Student.is_adult(20))  # Output: True
print(Student.is_adult(15))  # Output: False
