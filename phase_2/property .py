class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            print("Invalid age")

p = Person(20)

print(p.age)

p.age = 25
print(p.age)

p.age = -5