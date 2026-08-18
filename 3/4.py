import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="college_db"
)

cursor = conn.cursor()
cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)",
               ("Harsha", 20, "Computer Engineering", 85))
conn.commit()
print("One student record inserted!")

conn.close()
