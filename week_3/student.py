"""5. Student Class 
● Create a class Student with private attribute __grade. 
● Add methods set_grade() and get_grade(). 
● Test by setting and getting the grade. 
"""
class Student:
    def __init__(self):
        self.__grade = None

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

s = Student()
s.set_grade(90)
print(s.get_grade())