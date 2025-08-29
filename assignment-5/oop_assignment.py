# PLP
# Week 5
# Assignment 5: OOP practice
# OOP Assignment

# ------------------------------
# Assignment 1: Smartphone Class
# ------------------------------

# Base class (Parent)
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        """Return device info"""
        return f"{self.brand} {self.model}"


# Child class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
        self.__battery = 100  # Private attribute (Encapsulation)

    def use(self, hours):
        """Simulate phone usage by decreasing battery"""
        self.__battery -= hours * 10
        if self.__battery < 0:
            self.__battery = 0
        return f"Battery now at {self.__battery}%"

    def charge(self):
        """Fully charge the phone"""
        self.__battery = 100
        return "Phone fully charged 🔋"

    def get_battery(self):
        """Check battery level (controlled access)"""
        return f"Battery level: {self.__battery}%"


def run_assignment1():
    """Test the Smartphone class"""
    print("\n=== Assignment 1: Smartphone Class ===")
    phone1 = Smartphone("Apple", "iPhone 14", "iOS", "128GB")
    phone2 = Smartphone("Samsung", "Galaxy S23", "Android", "256GB")

    print(phone1.info())            # Apple iPhone 14
    print(phone1.get_battery())     # Battery level: 100%
    print(phone1.use(3))            # Battery now at 70%
    print(phone1.charge())          # Phone fully charged 🔋
    print(phone2.info())            # Samsung Galaxy S23
    print(phone2.get_battery())     # Battery level: 100%


# ------------------------------
# Activity 2: Polymorphism
# ------------------------------

class Animal:
    def move(self):
        print("This animal moves somehow...")

class Dog(Animal):
    def move(self):
        print("Dog runs 🐕")

class Fish(Animal):
    def move(self):
        print("Fish swims 🐟")

class Bird(Animal):
    def move(self):
        print("Bird flies 🕊️")


def run_activity2():
    """Test polymorphism with animals"""
    print("\n=== Activity 2: Polymorphism Challenge ===")
    animals = [Dog(), Fish(), Bird()]

    for animal in animals:
        animal.move()


# ------------------------------
# Program Menu
# ------------------------------

def main():
    while True:
        print("\n====== OOP Assignment Menu ======")
        print("1. Run Assignment 1 (Smartphone Class)")
        print("2. Run Activity 2 (Polymorphism Challenge)")
        print("3. Run Both")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_assignment1()
        elif choice == "2":
            run_activity2()
        elif choice == "3":
            run_assignment1()
            run_activity2()
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")


# Entry point
if __name__ == "__main__":
    main()
