import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="college_db"
)

cursor = conn.cursor()
students = [
    ("Ravi", 21, "IT", 78),
    ("Sita", 22, "CSE", 90),
    ("Arjun", 20, "ECE", 65),
    ("Meena", 23, "CSE", 88),
    ("Kiran", 21, "IT", 72)
]

cursor.executemany("INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)", students)
conn.commit()
print("Five student records inserted!")

conn.close()
