'''
Q1. Create a BankAccount class
with attributes account_number, owner_name, and balance.
Add methods to deposit, withdraw, and check balance. 
'''
# Q1 Solution:
class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number;
        self.owner_name = owner_name;
        self.balance = balance;

    def deposit(self, amount):
        if (amount >= 0):
            self.balance += amount
            print("Deposit amount:", amount, "New Balance:", self.balance)
        else:
            print("Deposit amount cannot be negative");

    def withdraw(self, amount):
        if (amount >= 0):
            if (self.balance >= amount):
                self.balance -= amount
                print("Withdraw amount:", amount, "New Balance:", self.balance)
            else:
                print("You don't have enough balance.")
        else:
            print("Withdraw amount cannot be negative");

    def check_balance(self):
        print("Current balance:", self.balance)
        return self.balance;

a1 = BankAccount("7323254823", "Zeanur Rahaman Zeon", 30200);
a1.check_balance();
a1.deposit(200)
a1.withdraw(200)
a1.check_balance();


'''
Q2. Create a Book class with the following attributes: 
    • title 
    • author 
    • list of reviews 
And add methods to: 
    • add a new review 
    • count reviews 
    • display all reviews 
'''

'''
Q3. Create a class Student
with private attributes _name, _roll_no, and _marks. 
Provide getter and setter methods with validation (e.g., marks cannot be 
negative, roll number has to be between 1 & 100 & name cannot be empty).
'''

'''
Q4. Create a class Shape with a method area(). 
Create subclasses Circle, Rectangle, and Triangle that override the area() 
method. 
'''

'''
Q5. Create a base class Vehicle with attributes like brand and model. 
Create two subclasses Car and Bike that add extra attributes - seats (in Car) & 
engine_cc (in Bike). 
'''

'''
Q6. Create an abstract class Employee 
with an abstract method calculate_salary(). 
Create subclasses Intern, FullTimeEmployee, and ContractEmployee that
implement the method differently.
'''

'''
Q7. Create a class Person that allows the constructor to work with: 
    • name only 
    • name + age 
    • name + age + address  
As direct constructor overloading (multiple constructors) are not allowed but 
we have to use default parameters to simulate constructor overloading. 
'''

'''
Q8. Create a class Player with:  
    • a class variable player_count 
    • instance variables name and level 
Track how many players were created. 
'''

'''
Q9. Create the following classes: Herbivore , Carnivore , Omnivore
with some attributes & methods. Then create a class Bear that inherits from all the above 
classes to showcase how multiple inheritance works. 
'''

'''
Q10. Mini Project - OOP Chat System 
Let's create a Chat System using OOPs concepts. We have to create classes: 
    • User 
    • Message 
    • ChatRoom 
And we have to implement functions: 
    • sending messages 
    • viewing chat history 
    • user joining and leaving the chatroom
'''