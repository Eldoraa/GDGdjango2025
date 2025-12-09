age=int(input("enter your age :"))
current_year =2025
birth_year= current_year-age

print("your birth year is :",birth_year)

#checks if a number is even or odd
num= int(input("enter any number:"))
if num %2==0:
    print(num ,"is even")
else:
    print(num ,"is odd")

    #factorial function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("enter a number: "))
print("the factorial is:", factorial(n))

#Build a program to find the maximum number in a list
numbers = [10, 3, 25, 7, 50, 2]

max_num = numbers[0]#we use this as a starting point,then compare all candidates with the first one ,we can also use[1],[2]...

for n in numbers:
    if n > max_num:
        max_num = n

print("The maximum number is:", max_num)

    
    