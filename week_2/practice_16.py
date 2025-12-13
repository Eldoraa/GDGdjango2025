"""16. Create a new dictionary where the keys become values and 
values become keys.
Example: 
                 Input: grades = {"John": "A", "Sara": "B", "Musa": "A"}
output:  {"A": ["John", "Musa"], "B": ["Sara"]"""
grades = {"John": "A", "Sara": "B", "Musa": "A"}

inverted = {}

for student, grade in grades.items():
    if grade not in inverted:
        inverted[grade] = []
    inverted[grade].append(student)

print(inverted)
