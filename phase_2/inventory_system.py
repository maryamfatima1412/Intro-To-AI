from abc import ABC, abstractmethod


class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, price):
        pass


class PercentageDiscount(DiscountStrategy):

    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price - (price * self.percentage / 100)


class FixedDiscount(DiscountStrategy):

    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):
        if self.amount > price:
            return 0
        return price - self.amount


class Product:

    store_name = "ABC Store"

    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Invalid Price")

    def update_quantity(self, quantity):
        self.quantity = quantity

    @staticmethod
    def is_valid_quantity(quantity):
        return quantity >= 0

    @classmethod
    def default_product(cls):
        return cls("Unknown", 0, 0)

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Quantity: {self.quantity}"


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} removed successfully.")
                return
        print("Product not found.")

    def update_product(self, name, price, quantity):
        for product in self.products:
            if product.name == name:
                product.price = price
                product.update_quantity(quantity)
                print("Product updated successfully.")
                return
        print("Product not found.")

    def apply_discount(self, name, strategy):
        for product in self.products:
            if product.name == name:
                new_price = strategy.apply_discount(product.price)
                product.price = new_price
                print(f"Discount applied to {name}.")
                return
        print("Product not found.")

    def display_products(self):
        print("\nInventory:")
        for product in self.products:
            print(product)

    def __getitem__(self, index):
        return self.products[index]

    def __len__(self):
        return len(self.products)


inventory = Inventory()

product1 = Product("Laptop", 120000, 5)
product2 = Product("Mouse", 2000, 20)
product3 = Product("Keyboard", 4500, 15)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

inventory.display_products()

print("\nTotal Products:", len(inventory))

inventory.update_product("Mouse", 1800, 25)

percentage = PercentageDiscount(10)
inventory.apply_discount("Laptop", percentage)

fixed = FixedDiscount(500)
inventory.apply_discount("Keyboard", fixed)

inventory.display_products()

inventory.remove_product("Mouse")

inventory.display_products()

print("\nFirst Product:")
print(inventory[0])

default = Product.default_product()

print("\nDefault Product:")
print(default)

print("\nValid Quantity:", Product.is_valid_quantity(10))
print("Valid Quantity:", Product.is_valid_quantity(-5))