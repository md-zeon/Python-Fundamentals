'''
Product store
Design & Create an online store for Products (name, price),
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.
'''

class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        return f"Product Name: {self.name}, Price: ${self.price}"
    
    @classmethod
    def get_count(cls):
        return f"Total products in the store: {cls.count}"
    
    @staticmethod
    def calculate_discount(price, discount_percent):
        discount_amount = price * (discount_percent / 100)
        discounted_price = price - discount_amount
        return discounted_price

p1 = Product("Laptop", 50_000)
p2 = Product("Mobile", 20_000)
p3 = Product("Pen", 15)
print(p1.get_info())
print(p2.get_info())
print(p3.get_info())
print(Product.get_count())
discounted_price = Product.calculate_discount(p1.price, 10)
print(f"Discounted price of {p1.name} after 10% discount: ${discounted_price}")