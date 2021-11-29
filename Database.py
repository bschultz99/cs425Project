from typing import final
import mysql.connector
from mysql.connector import Error

def server_connection_first():
    #input variables later? host_name, user_name, user_password.
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='group1',
        )
        print('Connected to mysql server')
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def server_connection():
    #input variables later? host_name, user_name, user_password, db_name.
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='group1',
            database='DonorSystem'
        )
        print('Connected to mysql server')
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS DonorSystem")
        print('Database Created')
    except Error as e:
        print(f"Error: '{e}'") 

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query successful')
    except Error as e:
        print(f"Error: '{e}'")

def create_tables(connection):
    cursor = connection.cursor()
    donor_table = """
    CREATE TABLE IF NOT EXISTS Donor (
	donor_ID INT AUTO_INCREMENT PRIMARY KEY,
    bloodType VARCHAR(255),
    age INT,
    chronicDisease VARCHAR(255),
    drugUsage VARCHAR(255),
    lastTattooDate DATE,
    medicationHistory VARCHAR(255),
    lastDonaitonTime TIME,
    phoneNumber VARCHAR(10),
    email VARCHAR(255),
    region VARCHAR(255),
    donorType VARCHAR(255)
    );
    """
    patient_table = """
    CREATE TABLE IF NOT EXISTS Patient (
	patient_ID INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(255),
    bloodType VARCHAR(255),
    age INT,
    needs VARCHAR(255),
    region VARCHAR(255),
    phoneNumber VARCHAR(10),
    email VARCHAR(255),
    waitlistPosition INT
    );
    """
    doctor_table = """
    CREATE TABLE IF NOT EXISTS Doctor (
	doctor_ID INT AUTO_INCREMENT PRIMARY KEY,
    doctor_name VARCHAR(255),
    specialization VARCHAR(255),
    fee INT,
    region VARCHAR(255),
    email VARCHAR(255),
    phoneNumber VARCHAR(10)
    );

    """
    organ_table = """
    CREATE TABLE IF NOT EXISTS Organ (
	organ_ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    shelfLife INT,
    availablityDate DATE
    );
    """
    hospital_table = """
    CREATE TABLE IF NOT EXISTS Hospital (
	hospital_ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    region VARCHAR(255),
    cost INT
    );
    """
    execute_query(connection, donor_table)
    execute_query(connection, patient_table)
    execute_query(connection, doctor_table)
    execute_query(connection, organ_table)
    execute_query(connection, hospital_table)

def populate_tables(connection):
    donor_info = """
    INSERT INTO Donor IF DOES NOT EXIST VALUES
    ('A', '21', 'Diabetes', 'Insulin', '', 'Insulin', 08:25:14, '8048040891', 'hh@gmail.com', 'Chicago', 'Blood');
    """
    patient_info = """
    """
    doctor_info = """
    """
    organ_info = """
    """
    hospital_info = """
    INSERT INTO Hospital VALUES
    (NULL, 'Mercy', 'Chicago', '500');
    """
    execute_query(connection, hospital_info)

def drop_tables(connection):
    execute_query(connection, "DROP TABLE Donor")
    execute_query(connection, "DROP TABLE Patient")
    execute_query(connection, "DROP TABLE Doctor")
    execute_query(connection, "DROP TABLE Organ")
    execute_query(connection, "DROP TABLE Hospital")

server_connection_first()
connection = server_connection()
create_database(connection)
create_tables(connection)
#populate_tables(connection)
#drop_tables(connection)