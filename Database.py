import mysql.connector
from mysql.connector import Error
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="group1"
)
mycursor = mydb.cursor()
mycursor.exectue("DonorSystem.db")