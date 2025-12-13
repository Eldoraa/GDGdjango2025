""" 3, Write a script that logs user activity.
     When the program runs
     Write "User logged in" to a file called log.txt.
     Then read the file and print the full log history"""

with open("log.txt", "a") as file:   # "a" (append)
    file.write("User logged in\n")

with open("log.txt", "r") as file:
    log_history = file.read()
    print("Log History:")
    print(log_history)