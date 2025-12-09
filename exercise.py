filename="elroe"
try:
    with open(file.name ,"r") as file:
        name =file.read().strip()
    if name =="":
        raise ValueError("name cannot be empty!")
except FileNotFoundError:
    print("file not found. creating new file... ")
    name="guest"        
    with open(file.name,"w") as file:
        file.write(name)
except ValueError as ve:
    print("error:",ve)
    name="guest"
except Exception as e:
    print("unexpected error:",e)
    name ="guest"
finally:
    print(f"welcome,{name}!")