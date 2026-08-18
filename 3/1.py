import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="password" 
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE college_db")
print("Database 'college_db' created successfully!")

conn.close()
