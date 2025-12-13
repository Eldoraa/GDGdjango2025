"""5.You receive a file called sales.txt where each line should contain a
sales number.
Example:
 200
 450
 abc
 700
Write a program that:
a, Reads every line in sales.txt
b, Converts valid lines into integers
c, Skips invalid lines (like "abc") using exception handling
d, Stores the valid numbers in a list
e, Calculates and prints the total sales
"""
sales = []

with open("sales.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip())
            sales.append(number)
        except ValueError:
            pass

total_sales = sum(sales)
print("Total sales:", total_sales)

           
           
           