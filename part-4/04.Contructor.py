"""

Constructor
In Python, a constructor is a special method that is automatically called when an object of a class is created. The constructor method is named __init__.
The __init__ method is used to initialize the attributes of the object when it is created. It takes at least one parameter, which is usually named self, and can take additional parameters to initialize the object's attributes.
The syntax for defining a constructor in Python is as follows:
class ClassName:
    def __init__(self, parameter1, parameter2, ...):
        # Initialize attributes using the parameters
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        ...
When an object of the class is created, the __init__ method is automatically called, and the parameters passed during object creation are used to initialize the object's attributes.
For example, let's say we have a class called "Student" and we want to initialize the attributes name, age, and grade when we create a student object. We can define the constructor as follows:
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

Now, when we create a student object, we can pass the name, age, and grade as parameters to the constructor:
student1 = Student("Alice", 20, "A")
In this example, the __init__ method is called when we create the student1 object, and the attributes name, age, and grade are initialized with the values "Alice", 20, and "A" respectively.
The constructor allows us to set up the initial state of an object when it is created, making it easier to work with the object and its attributes. It is an essential part of object-oriented programming in Python.

The self parameter in the __init__ method refers to the instance of the class that is being created. It allows us to access and modify the attributes of the object within the constructor. By convention, we use the name self for this parameter, but it can be named anything as long as it is the first parameter of the __init__ method.
for example, in the Student class, we use self to refer to the instance of the Student class that is being created. When we assign values to self.name, self.age, and self.grade, we are setting the attributes of the student object that is being initialized.

The first parameter of the __init__ method is always self, which refers to the instance of the class being created. The other parameters can be used to initialize the attributes of the object. When we create an object of the class, we pass the values for these parameters, and they are used to set up the initial state of the object.

The constructor can also include default values for the parameters. This allows us to create objects without providing all the parameters, and the default values will be used instead. For example:
class Student:
    def __init__(self, name, age=18, grade="A"):
        self.name = name
        self.age = age
        self.grade = grade
In this example, if we create a student object without providing the age and grade parameters, the default values of 18 and "A" will be used:
student2 = Student("Bob")
In this case, student2 will have the name "Bob", age 18, and grade "A" because the default values are used for the age and grade parameters.

In summary, the constructor in Python is a special method that is used to initialize the attributes of an object when it is created. It is defined using the __init__ method and takes parameters to set up the initial state of the object. The self parameter allows us to access and modify the attributes of the object within the constructor. Default values can also be provided for the parameters to allow for more flexible object creation.

"""

class Student:
    def __init__(self, name, age=18, grade="A"):
        self.name = name
        self.age = age
        self.grade = grade
student1 = Student("Alice", 20, "A")
print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20
print(student1.grade) # Output: A
student2 = Student("Bob")
print(student2.name)  # Output: Bob
print(student2.age)   # Output: 18
print(student2.grade) # Output: A
