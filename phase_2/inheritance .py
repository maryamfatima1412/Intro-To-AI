class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Team Size: {self.team_size}")

manager = Manager("Ali", 90000, 12)
manager.show_details()