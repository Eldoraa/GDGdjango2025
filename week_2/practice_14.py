"""14. You are given a dictionary storing student scores:
scores = {"John": 85, "Sara": 92, "Fraol": 78}
Write a program that:
1.Asks the user to enter a student name.
2. Tries to print the student’s score from the dictionary.
3.If the key does not exist, catch the exception and print:
"Student not found!"
Example:
Input: Mark
 Output: Student not found!"""
scores = {"John": 85, "Sara": 92, "Fraol": 78}


name = input("Enter student name: ")

try:
    print(f"{name}'s score is {scores[name]}")
except KeyError:
    print("Student not found!")
