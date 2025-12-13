"""1. Person Class 
● Create a class Person with attributes name and age. 
● Make an object and print its attributes. """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Jhon", 25)
print(p.name, p.age)