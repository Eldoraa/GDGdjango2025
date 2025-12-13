"""9. Vehicle → Car (Method Overriding) 
● Create a base class Vehicle with brand and year. 
● Create a child class Car that adds model. 
● Override a method info() in Car. 
● Test info() for both classes."""
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

v = Vehicle("mercedes")
print(v.info())

c = Car("BMW", "X5")
print(c.info())