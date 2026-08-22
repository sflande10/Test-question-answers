score = 0
print("Welcome to the Quiz!")
#Question 1
answer = input("1. What is the capital of Canada?")
if answer.lower() == "ottawa":
    score+=1
    print("Correct")
else:
    print("Incorrect")
#Question 2
answer = input("2. What is 5+7?")
if answer.lower() == "12":
    score+=1
    print("Correct")
else:
    print("Incorrect")
#Question3    
answer = input("3. What planet do we live on")
if answer.lower() == "earth":
    score+=1
    print("Correct")
else:
    print("Incorrect")
#Question4
answer = input("4. How many days are in a week??")
if answer.lower() == "7":
    score+=1
    print("Correct")
else:
    print("Incorrect")
#Quesiton5
answer = input("5. What color is the sky?")
if answer.lower() == "blue":
    score+=1
    print("Correct")
else:
    print("Incorrect")
percentage = (score/5)*100
if percentage >=80:
    print("Excellent")
elif percentage>=50:
    print("Good")
elif percentage>50:
    print("Needs work")