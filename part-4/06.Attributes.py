'''
Attributes:
- Attributes are variables that belong to an object.
- They are used to store information about the object and can be accessed and modified using dot notation.
- There are two types of attributes in Python: instance attributes and class attributes.
- Instance attributes are specific to each instance of a class and are defined in the constructor of the class. They are accessed using the self keyword. For example:
class Student:
    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age   # instance attribute
In this example, name and age are instance attributes of the Student class. Each instance of the Student class will have its own values for these attributes.
- Class attributes, on the other hand, are shared by all instances of a class and are defined outside of any method in the class. They are accessed using the class name. For example:
class Student:
    school = "ABC School" # class attribute
In this example, school is a class attribute of the Student class. All instances of the Student class will share the same value for the school attribute, which is "ABC School".
- Attributes can be defined in the constructor of a class or added to an object after it has been created. For example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Alice", 20)
print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20
In this example, the name and age attributes are defined in the constructor of the Student class and initialized with the values passed as parameters when creating the student1 object. The attributes can be accessed using dot notation (student1.name and student1.age) to retrieve their values.
Attributes can also be added to an object after it has been created. For example:
student1.grade = "A"
print(student1.grade)  # Output: A
In this example, the grade attribute is added to the student1 object after it has been created and assigned the value "A". The grade attribute can then be accessed using dot notation (student1.grade) to retrieve its value.
Attributes can also be modified after they have been created. For example: 
student1.age = 21
print(student1.age)   # Output: 21
In this example, the age attribute of the student1 object is modified from 20 to 21 using dot notation (student1.age = 21). The modified value can then be accessed using dot notation (student1.age) to retrieve the updated value.
Attributes can also be deleted from an object using the del keyword. For example:
del student1.age
print(student1.age)   # Output: AttributeError: 'Student' object has no attribute 'age'
In this example, the age attribute of the student1 object is deleted using the del keyword (del student1.age). Attempting to access the deleted attribute will result in an AttributeError.
In summary, attributes are an essential part of object-oriented programming in Python. They allow us to store and manipulate information about objects, making our code more organized and efficient.
'''

class Student:
    school = "ABC School" # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age   # instance attribute
student1 = Student("Alice", 20)
print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20
student1.grade = "A" # adding a new attribute to the student1 object
print(student1.grade)  # Output: A
student1.age = 21 # modifying the age attribute of the student1 object
print(student1.age)   # Output: 21
del student1.age # deleting the age attribute of the student1 object
try:
    print(student1.age)   # This will raise an AttributeError since age has been deleted
except AttributeError as e:
    print(e)  # Output: 'Student' object has no attribute 'age'


"""
Priority of Attributes:
- When accessing an attribute of an object, Python follows a specific order of priority to determine which attribute to access. The order of priority is as follows:
1. Instance attributes: Python first looks for the attribute in the instance of the object. If the attribute is found in the instance, it is returned.
2. Class attributes: If the attribute is not found in the instance, Python looks for the attribute in the class of the object. If the attribute is found in the class, it is returned.
3. Parent class attributes: If the attribute is not found in the class, Python looks for the attribute in the parent classes of the class. If the attribute is found in any of the parent classes, it is returned.
4. Built-in attributes: If the attribute is not found in the instance, class, or parent classes, Python looks for built-in attributes. Built-in attributes are special attributes that are defined by Python and are available for all objects. Examples of built-in attributes include __class__, __dict__, and __str__.
- If the attribute is not found in any of the above locations, Python raises an AttributeError indicating that the attribute does not exist.
"""
