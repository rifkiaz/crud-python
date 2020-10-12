import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="tehanget"
)
if db.is_connected():
    print("Yey berhasil terhubung")
