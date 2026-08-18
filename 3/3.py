import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="college_db"
    )
    if conn.is_connected():
        print("Connected to MySQL database successfully!")
except Exception as e:
    print("Error:", e)
