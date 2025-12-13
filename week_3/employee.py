"""6. Employee Class 
● Create a class Employee with attributes name and salary. 
● Add a method annual_salary() that calculates yearly salary. """
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

e = Employee("dora", 300000)
print(e.annual_salary())