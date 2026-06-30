import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='data_storage'
)

cursor = conn.cursor()
