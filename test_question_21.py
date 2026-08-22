import sqlite3

conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    score INTEGER
)""")

cur.execute("INSERT INTO students (name, age, course, score) VALUES (?, ?, ?, ?)", ('John', 20, 'Computer Science', 75))
cur.execute("INSERT INTO students (name, age, course, score) VALUES (?, ?, ?, ?)", ('Mary', 22, 'Mathematics', 88))
cur.execute("INSERT INTO students (name, age, course, score) VALUES (?, ?, ?, ?)", ('Peter', 19, 'Physics', 62))

conn.commit()

cur.execute("SELECT * FROM students")
print("All students:")
for row in cur.fetchall():
    print(row)

cur.execute("SELECT * FROM students WHERE score > 70")
print("Students above 70:")
for row in cur.fetchall():
    print(row)

conn.close()