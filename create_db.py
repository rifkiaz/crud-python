import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="1521"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_mainan")

print("Database telah dibuat")
