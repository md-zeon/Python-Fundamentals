'''
Types of Inheritance in Python:
1. Single Inheritance: A child class inherits from a single parent class.
2. Multiple Inheritance: A child class inherits from multiple parent classes.
3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.

Theory:
1. Single Inheritance:
   - In single inheritance, a child class inherits properties and behaviors from a single parent class. This allows for code reusability and the creation of a hierarchical relationship between classes.
2. Multiple Inheritance:
   - In multiple inheritance, a child class can inherit from more than one parent class. This allows for the combination of features from multiple classes, but it can also lead to ambiguity if there are conflicting attributes or methods.
3. Multilevel Inheritance:
   - In multilevel inheritance, a child class inherits from a parent class, which in turn inherits from another parent class. This creates a chain of inheritance, allowing for the reuse of code across multiple levels of the class hierarchy.
4. Hierarchical Inheritance:
   - In hierarchical inheritance, multiple child classes inherit from a single parent class. This allows for the creation of a tree-like structure of classes, where each child class can have its own unique properties and behaviors while still inheriting from the common parent class.
5. Hybrid Inheritance:
   - In hybrid inheritance, a combination of two or more types of inheritance is used. This allows for more complex and flexible class designs, but can also lead to increased complexity in managing and maintaining the code.
'''

"""
1. Single Inheritance:
   class ParentClass:
       # parent class code

   class ChildClass(ParentClass):
       # child class code
"""

# Example of Single Inheritance
class Employee:
    start_time = "9:00 AM"
    end_time = "5:00 PM"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

admin = AdminStaff("HR Manager")
print(admin.role, admin.start_time, admin.end_time) # Output: HR Manager 9:00 AM 5:00 PM

# In this example, the AdminStaff class inherits from the Employee class, allowing it to access the start_time and end_time attributes defined in the Employee class.

'''
2. Multiple Inheritance:
   class ParentClass1:
       # parent class 1 code

   class ParentClass2:
       # parent class 2 code

   class ChildClass(ParentClass1, ParentClass2):
       # child class code
'''
# Example of Multiple Inheritance
class Teacher:
    def __init__(self, subject, salary):
        self.subject = subject
        self.salary = salary

class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class TeachingAssistant(Teacher, Student):
    def __init__(self, subject, salary, name, cgpa):
        Teacher.__init__(self, subject, salary) # Initialize Teacher class attributes
        Student.__init__(self, cgpa) # Initialize Student class attributes
        self.name = name
ta = TeachingAssistant("Math", 30000, "Alice", 3.8)

print(ta.name, ta.subject, ta.salary, ta.cgpa) # Output: Alice Math 30000 3.8

# In this example, the TeachingAssistant class inherits from both the Teacher and Student classes, allowing it to access attributes from both parent classes.

'''
3. Multilevel Inheritance:
   class ParentClass:
       # parent class code

   class ChildClass(ParentClass):
       # child class code

   class GrandChildClass(ChildClass):
       # grandchild class code
'''

# Example of Multilevel Inheritance
class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role) # Call the constructor of the parent class (AdminStaff) to initialize the role
        self.salary = salary
accountant = Accountant(50000, "Accountant")
print(accountant.role, accountant.salary, accountant.start_time) # Output: Accountant 50000 9:00 AM

# In this example, the Accountant class inherits from the AdminStaff class, which in turn inherits from the Employee class. This allows the Accountant class to access attributes from both the AdminStaff and Employee classes.

'''
4. Hierarchical Inheritance:
   class ParentClass:
       # parent class code

   class ChildClass1(ParentClass):
       # child class 1 code

   class ChildClass2(ParentClass):
       # child class 2 code
'''
# Example of Hierarchical Inheritance
class Developer(Employee):
    def __init__(self, programming_language):
        self.programming_language = programming_language

class Designer(Employee):
    def __init__(self, design_tool):
        self.design_tool = design_tool
developer = Developer("Python")
designer = Designer("Adobe Photoshop")
print(developer.programming_language, developer.start_time) # Output: Python 9:00 AM
print(designer.design_tool, designer.start_time) # Output: Adobe Photoshop 9:00 AM

# In this example, both the Developer and Designer classes inherit from the Employee class, allowing them to access the start_time attribute defined in the Employee class while also having their own unique attributes (programming_language and design_tool).

'''
5. Hybrid Inheritance:
   class ParentClass1:
       # parent class 1 code

   class ParentClass2:
       # parent class 2 code

   class ChildClass(ParentClass1, ParentClass2):
       # child class code
'''
# Example of Hybrid Inheritance
class Manager(Employee):
    def __init__(self, department):
        self.department = department
class TeamLead(Manager):
    def __init__(self, department, team_size):
        super().__init__(department) # Call the constructor of the parent class (Manager) to initialize the department
        self.team_size = team_size
team_lead = TeamLead("IT", 5)
print(team_lead.department, team_lead.team_size, team_lead.start_time) # Output: IT 5 9:00 AM

# In this example, the TeamLead class inherits from the Manager class, which in turn inherits from the Employee class. This allows the TeamLead class to access attributes from both the Manager and Employee classes while also having its own unique attribute (team_size).
# In this case, the TeamLead class is an example of hybrid inheritance because it combines features of both multilevel and single inheritance.