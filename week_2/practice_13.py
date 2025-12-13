"""13. Read File and Convert All Text to Uppercase
Write a program that:
Reads a file
Converts all text to uppercase
Displays it on the screen
Uses try/except to handle missing file errors
Input: message.txt:  
Hello World
  Python is fun
output:
HELLO WORLD
PYTHON IS FUN
"""
file_content = """Hello World
Python is fun
"""

with open("message.txt", "w") as f:
    f.write(file_content)
try:
    with open("message.txt", "r") as file:
        for line in file:
            print(line.strip().upper())
except FileNotFoundError:
    print("Error: The file 'message.txt' was not found.")
