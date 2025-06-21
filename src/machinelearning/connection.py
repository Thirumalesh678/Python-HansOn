import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="thiru",
    password="12345",
    database="thiru",
    port=1521 
)
print(mydb)