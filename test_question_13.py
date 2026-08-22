try:
    first = float(input("Enter the first number"))
    second = float(input("Enter the second number"))
    result = first/second
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("You cannot divide by zero")
