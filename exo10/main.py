# Écrivez votre code ici !

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"name: {self.name} age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        print(f"name: {self.name} age: {self.age} salary: {self.salary}")


toto = Person("toto", 32)
toto.display_details()

bubu = Employee("bubu", 32, 100000)
bubu.display_details()