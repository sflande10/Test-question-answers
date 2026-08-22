try:
    name = input("Enter your name")
    age = input("Enter your age")
    email=input("Enter your email")
    course=input("Enter your course")
    with open("student.txt", "w") as file:
        file.write(f"Name:{name}\n")
        file.write(f"Age:{age}\n")
        file.write(f"Email:{email}\n")
        file.write(f"Course:{course}\n")
    with open("student.txt", "r") as file:
        info=file.read()
        print(info)
except FileNotFoundError:
    print("The file could not be found.")
except PermissionError:
    print("You do not have acess to the file")
except OSError:
    print("An error occured while working with the file.")