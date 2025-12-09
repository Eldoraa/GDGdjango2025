def check_pass():
    real_pass="123eldora"
    input_pass=input("enter your password:")
    if input_pass ==real_pass:
            print("logged in suceccfully")
    else:
            print("incorrect password try again")

check_pass()    

#simple calculator 
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operation= input("choose the operation u want(+,-,*,/):")
if operation =="+":
    result=add(num1,num2)
elif operation =="-":
    result= subtract (num1,num2) 
elif operation =="*":
    result=multiply(num1,num2)
elif operation =="/":
    result=divide(num1,num2) 
else:
    result="invalid opertation"

    print(result)
