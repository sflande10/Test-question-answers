import sqlite3
import pandas as pd

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT,
    score INTEGER
)""")
conn.commit()

def add_student():
    sid = input("Enter ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    score = input("Enter score: ")

    cur.execute("INSERT INTO students (id, name, age, course, score) VALUES (?, ?, ?, ?, ?)",
                (sid, name, int(age), course, int(score)))
    conn.commit()
    print("Student added.")

def view_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    if not rows:
        print("No students found.")
        return
    for r in rows:
        print(r)

def search_student():
    query = input("Enter name or ID to search: ")
    cur.execute("SELECT * FROM students WHERE id = ? OR LOWER(name) = LOWER(?)", (query, query))
    rows = cur.fetchall()
    if not rows:
        print("No matching student found.")
        return
    for r in rows:
        print(r)

def update_student():
    sid = input("Enter ID of student to update: ")
    cur.execute("SELECT * FROM students WHERE id = ?", (sid,))
    if not cur.fetchone():
        print("Student not found.")
        return

    name = input("New name: ")
    age = input("New age: ")
    course = input("New course: ")
    score = input("New score: ")

    cur.execute("UPDATE students SET name=?, age=?, course=?, score=? WHERE id=?",
                (name, int(age), course, int(score), sid))
    conn.commit()
    print("Student updated.")

def delete_student():
    sid = input("Enter ID of student to delete: ")
    cur.execute("SELECT * FROM students WHERE id = ?", (sid,))
    if not cur.fetchone():
        print("Student not found.")
        return
    cur.execute("DELETE FROM students WHERE id = ?", (sid,))
    conn.commit()
    print("Student deleted.")

def save_data():
    conn.commit()
    print("Data saved to students.db")

def generate_report():
    df = pd.read_sql_query("SELECT * FROM students", conn)
    if df.empty:
        print("No data to report on.")
        return
    print("Total students:", len(df))
    print("Average score:", round(df['score'].mean(), 2))
    print("Highest score:", df['score'].max())
    print("Lowest score:", df['score'].min())
    print("Students above 70:", len(df[df['score'] > 70]))

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Exit")
    print("8. Generate Report")

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
        conn.close()
        print("Goodbye.")
        break
    elif choice == "8":
        generate_report()
    else:
        print("Invalid choice, try again.")