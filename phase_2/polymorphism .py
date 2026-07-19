class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

class Cow:
    def sound(self):
        print("Moo")

animals = [Cat(), Dog(), Cow()]

for animal in animals:
    animal.sound()