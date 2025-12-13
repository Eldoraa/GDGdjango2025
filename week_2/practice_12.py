"""12. A file named numbers.txt contains one number per line.
examples numbers.txt: 
10
20
30
abc
40
Write a program that:
Reads each line
Converts valid numbers to integers
Ignores invalid lines (use try/except)
Prints the sum of all valid integers
Expected output:
Sum = 100 (because "abc" is skipped)
"""
total_sum = 0
numbers = """10
20
30
abc
40
"""

with open("numbers.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip())
            total_sum += number
        except ValueError:
            pass

print("Sum =", total_sum)
