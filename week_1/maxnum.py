#Build a program to find the maximum number in a list
numbers = [10, 3, 25, 7, 50, 2]

max_num = numbers[0]#we use this as a starting point,then compare all candidates with the first one ,we can also use[1],[2]...

for n in numbers:
    if n > max_num:
        max_num = n

print("The maximum number is:", max_num)
