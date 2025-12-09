try:
    age= int(input("enter your age:"))
    print("after 10 years u are",age +10)
except ValueError:#if it is other than numbers
    print("please enter only number!")
else:
    print("u dont have time , hurry up")
    
    """ ValueError: Wrong value type
FileNotFoundError: File doesn’t exist
KeyError: Missing dictionary key
TypeError: Wrong operation on a type 
ZeroDivisionError: """


#raise
def divide(a,b):
    if b==0 :
        raise ZeroDivisionError("you cannot a number by zero")
    return a/b
print(divide(20,0))


#writing to a file
file= open("data.text","w")
file.write ("hello world")
file.close
#reading a file
file=open("data.txt","r")
content=file.read()
print(content)
file.close()
#appending to a file
file=open("data.txt","a")
file.write("\nNew line added.")
file.close()
#using "with" to open and close the file automatially
try:
    with open ("names.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("the file does not exist") 