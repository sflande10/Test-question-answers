students = ["Ada", "John", "Mary", "Peter", "Ada"] 
students_set = set(students)
print(students_set)
students.sort()
for student in students:
    print(student)
students.append("Joe")
print("First student:", students[0])
print("Last student:", students[-1])

students_dict = {
    "Name": "Ada",
    "age": "20",
    "Course": "Python",
    "Score": "99"

}
print(students_dict)

programming_languages = ("Python", "Javascript", "C++", "Scratch", "C")
print(programming_languages[1])
print(programming_languages[3])