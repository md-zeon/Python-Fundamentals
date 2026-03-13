'''
Encapsulation in OOP:
Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP) that focuses on bundling data and methods that operate on that data within a single unit, typically a class. It also restricts direct access to some of an object's components, which can prevent the accidental modification of data.
- In Python, encapsulation is achieved through the use of access modifiers. The most common access modifiers are:
1. Public: Members (attributes and methods) that are accessible from anywhere. In Python, all members are public by default.
2. Protected: Members that are intended to be accessed only within the class and its subclasses. In Python, this is indicated by a single underscore prefix (e.g., _protected_member).
3. Private: Members that are intended to be accessed only within the class itself. In Python, this is indicated by a double underscore prefix (e.g., __private_member). Private members are name-mangled to prevent accidental access from outside the class.
- Encapsulation helps in:
1. Data Hiding: It hides the internal state of the object and only exposes a controlled interface to the outside world.
2. Modularity: It allows the internal implementation of a class to be changed without affecting the code that uses the class.
3. Maintenance: It makes it easier to maintain and modify code since the internal workings of a class are hidden from the outside, reducing the chances of unintended interference.
'''
class BankAccount:
    def __init__(self, owner, balance=0, account_number=None):
        self.owner = owner  # Public attribute
        self._balance = balance  # Protected attribute
        self.__account_number = account_number  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number
# Example usage
account = BankAccount("Alice", 1000, "123456789")
account.deposit(500)  # Deposited 500. New balance: 1500
account.withdraw(200)  # Withdrew 200. New balance: 1300
print(account.get_balance())  # 1300
print(account.get_account_number())  # 123456789
# Attempting to access protected attributes directly will result in an error
# print(account._balance)  # AttributeError: 'BankAccount' object has no attribute '_balance'
# However, you can access protected attributes using name mangling
print(account._BankAccount__account_number)  # 123456789
print(account._balance)  # 1300
# protected attributes can be accessed but are intended to be used within the class and its subclasses