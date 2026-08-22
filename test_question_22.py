import json
import os

students = []
filename = "students_data.json"

if os.path.exists(filename):
    with open(filename, 'r') as f:
        students = json.load(f)

def add_student():
    sid = input("Enter ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    score = input("Enter score: ")

    student = {
        "id": sid,
        "name": name,
        "age": int(age),
        "course": course,
        "score": int(score)
    }
    students.append(student)
    print("Student added.")

def view_students():
    if not students:
        print("No students found.")
        return
    for s in students:
        print(s["id"], "-", s["name"], "-", s["age"], "-", s["course"], "-", s["score"])

def search_student():
    query = input("Enter name or ID to search: ")
    found = False
    for s in students:
        if s["id"] == query or s["name"].lower() == query.lower():
            print(s["id"], "-", s["name"], "-", s["age"], "-", s["course"], "-", s["score"])
            found = True
    if not found:
        print("No matching student found.")

def update_student():
    sid = input("Enter ID of student to update: ")
    for s in students:
        if s["id"] == sid:
            s["name"] = input("New name: ")
            s["age"] = int(input("New age: "))
            s["course"] = input("New course: ")
            s["score"] = int(input("New score: "))
            print("Student updated.")
            return
    print("Student not found.")

def delete_student():
    sid = input("Enter ID of student to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted.")
            return
    print("Student not found.")

def save_data():
    with open(filename, 'w') as f:
        json.dump(students, f, indent=4)
    print("Data saved to", filename)

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        save_data()
    elif choice == "7":
        save_data()
        print("Goodbye.")
        break
    else:
        print("Invalid choice, try again.")