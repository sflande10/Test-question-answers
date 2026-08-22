def add(a, b):
    print(a+b)

def substract(a, b):
   
    print(a-b)

def division(a, b):
    print(a/b)

def multiplication(a,b):
    print(a*b)
print("Calculator Menu")
choice = int(input("Pick a option. \n1.Addition \n2.Substraction \n3.Division \n4.Multiplication\n"))
a = float(input("What is the first number?"))
b = float(input("What is the second number?"))
if choice ==1:
    add(a,b)
elif choice ==2:
    substract(a,b)
elif choice ==3:
    division(a,b)
elif choice ==4:
    multiplication(a,b)
else:
    print("Invalid choice.")