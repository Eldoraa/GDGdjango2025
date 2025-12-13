"""4.You are building a small student grade system.
    Write a function:
             get_grade(student_grades, student_name)
    It should:
    Try to return the student’s grade from a dictionary
     If the student does not exist, catch the exception and return:
    "Student not found in the system"""
def get_grade(student_grades,student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return "student not found in the system"
grade={"elroe":90}
print(get_grade(grade,"elroe"))