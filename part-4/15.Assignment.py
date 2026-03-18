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
# Q2 Solution:
class Book:
    def __init__(self, title, author):
        self.title = title;
        self.author = author;
        self.reviews = [];

    def add_review(self, review):
        self.reviews.append(review);
        print("Review added:", review);

    def count_reviews(self):
        print("Total reviews:", len(self.reviews));
        return len(self.reviews);

    def display_reviews(self):
        print("Reviews for", self.title, "by", self.author);
        for review in self.reviews:
            print("-", review);

b1 = Book("The Great Gatsby", "F. Scott Fitzgerald");
b1.add_review("A classic novel.");
b1.add_review("Great character development.");
b1.count_reviews();
b1.display_reviews();


'''
Q3. Create a class Student
with private attributes _name, _roll_no, and _marks. 
Provide getter and setter methods with validation (e.g., marks cannot be 
negative, roll number has to be between 1 & 100 & name cannot be empty).
'''
# Q3 Solution:
class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = None;
        self.__roll_no = None;
        self.__marks = None;
        self.set_name(name);
        self.set_roll_no(roll_no);
        self.set_marks(marks);

    def set_name(self, name):
        if (name.strip() != ""):
            self.__name = name;
            print("Name set to:", name);
        else:
            print("Name cannot be empty.");

    def set_roll_no(self, roll_no):
        if (1 <= roll_no <= 100):
            self.__roll_no = roll_no;
            print("Roll number set to:", roll_no);
        else:
            print("Roll number must be between 1 and 100.");

    def set_marks(self, marks):
        if (marks >= 0):
            self.__marks = marks;
            print("Marks set to:", marks);
        else:
            print("Marks cannot be negative.");

    def get_name(self):
        return self.__name;

    def get_roll_no(self):
        return self.__roll_no;

    def get_marks(self):
        return self.__marks;

s1 = Student("Alice", 10, 85);
s1.set_marks(90);
print("Name:", s1.get_name());
print("Roll Number:", s1.get_roll_no());
print("Marks:", s1.get_marks());

'''
Q4. Create a class Shape with a method area(). 
Create subclasses Circle, Rectangle, and Triangle that override the area() 
method. 
'''
# Q4 Solution:
import math
class Shape:
    def area(self):
        pass;

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius;

    def area(self):
        return round(math.pi * self.radius ** 2, 2);
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width;
        self.height = height;

    def area(self):
        return self.width * self.height;
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base;
        self.height = height;

    def area(self):
        return 0.5 * self.base * self.height;
c1 = Circle(5);
r1 = Rectangle(4, 6);
t1 = Triangle(4, 5);
print("Area of Circle:", c1.area());
print("Area of Rectangle:", r1.area());
print("Area of Triangle:", t1.area());

'''
Q5. Create a base class Vehicle with attributes like brand and model. 
Create two subclasses Car and Bike that add extra attributes - seats (in Car) & 
engine_cc (in Bike). 
'''
# Q5 Solution:
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand;
        self.model = model;

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model);
        self.seats = seats;

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model);
        self.engine_cc = engine_cc;
car1 = Car("Toyota", "Camry", 5);
bike1 = Bike("Yamaha", "R15", 150);
print("Car:", car1.brand, car1.model, "Seats:", car1.seats);
print("Bike:", bike1.brand, bike1.model, "Engine CC:", bike1.engine_cc);

'''
Q6. Create an abstract class Employee 
with an abstract method calculate_salary(). 
Create subclasses Intern, FullTimeEmployee, and ContractEmployee that
implement the method differently.
'''
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass;
class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend;

    def calculate_salary(self):
        return self.stipend;
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary;

    def calculate_salary(self):
        return self.monthly_salary;
class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate;
        self.hours_worked = hours_worked;

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked;
intern1 = Intern(1000);
full_time_employee1 = FullTimeEmployee(3000);
contract_employee1 = ContractEmployee(20, 160);
print("Intern Salary:", intern1.calculate_salary());
print("Full Time Employee Salary:", full_time_employee1.calculate_salary());
print("Contract Employee Salary:", contract_employee1.calculate_salary());

'''
Q7. Create a class Person that allows the constructor to work with: 
    • name only 
    • name + age 
    • name + age + address  
As direct constructor overloading (multiple constructors) are not allowed but 
we have to use default parameters to simulate constructor overloading. 
'''
# Q7 Solution:
class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name;
        self.age = age;
        self.address = address;
p1 = Person("Alice");
p2 = Person("Bob", 30);
p3 = Person("Charlie", 25, "123 Main St");
print("Person 1:", p1.name, p1.age, p1.address);
print("Person 2:", p2.name, p2.age, p2.address);
print("Person 3:", p3.name, p3.age, p3.address);

'''
Q8. Create a class Player with:  
    • a class variable player_count 
    • instance variables name and level 
Track how many players were created. 
'''
# Q8 Solution:
class Player:
    player_count = 0;

    def __init__(self, name, level):
        self.name = name;
        self.level = level;
        Player.player_count += 1;

print("Total Players Created:", Player.player_count);
p1 = Player("Alice", 5);
p2 = Player("Bob", 10);
print("Total Players Created:", Player.player_count);
p3 = Player("Charlie", 15);
print("Total Players Created:", Player.player_count);

'''
Q9. Create the following classes: Herbivore , Carnivore , Omnivore
with some attributes & methods. Then create a class Bear that inherits from all the above 
classes to showcase how multiple inheritance works. 
'''
# Q9 Solution:
class Herbivore:
    def eat_plants(self):
        print("Eating plants...");
class Carnivore:
    def eat_meat(self):
        print("Eating meat...");
class Omnivore:
    def eat_both(self):
        print("Eating both plants and meat...");
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name;
bear1 = Bear("Baloo");
print("Bear Name:", bear1.name);
bear1.eat_plants();
bear1.eat_meat();
bear1.eat_both();

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
# Q10 Solution:
class User:
    def __init__(self, username):
        self.username = username;
class Message:
    def __init__(self, sender, content):
        self.sender = sender;
        self.content = content;
class ChatRoom:
    def __init__(self, name):
        self.name = name;
        self.users = [];
        self.messages = [];
    def join(self, user):
        self.users.append(user);
        print(user.username, "joined the chat room:", self.name);
    def leave(self, user):
        self.users.remove(user);
        print(user.username, "left the chat room:", self.name);
    def send_message(self, sender, content):
        if sender in self.users:
            message = Message(sender, content);
            self.messages.append(message);
            print(sender.username, "sent a message:", content);
        else:
            print(sender.username, "is not in the chat room.");
    def view_chat_history(self):
        print("Chat History for", self.name);
        for message in self.messages:
            print(message.sender.username + ":", message.content);

# Example Usage:
chat_room = ChatRoom("General");
user1 = User("Alice");
user2 = User("Bob");
chat_room.join(user1);
chat_room.join(user2);
chat_room.send_message(user1, "Hello everyone!");
chat_room.send_message(user2, "Hi Alice!");
chat_room.view_chat_history();
chat_room.leave(user1);