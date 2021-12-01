from os import read
from typing import final
import mysql.connector
from mysql.connector import Error

#Server connection if the database has not been created yet
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

#server connection if the database has already been created
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

#Creates the overall database
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS DonorSystem")
        print('Database Created')
    except Error as e:
        print(f"Error: '{e}'") 

#Any execute queries are passed through this
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query successful')
    except Error as e:
        print(f"Error: '{e}'")

#Creates the five tables
def create_tables(connection):
    cursor = connection.cursor()
    donor_table = """
    CREATE TABLE IF NOT EXISTS Donor (
	donor_ID INT AUTO_INCREMENT PRIMARY KEY,
    bloodType VARCHAR(255),
    organs VARCHAR(255),
    age INT,
    chronicDisease VARCHAR(255),
    drugUsage VARCHAR(255),
    lastTattooDate DATE,
    medicationHistory VARCHAR(255),
    lastDonaitonTime DATE,
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
    phoneNumber VARCHAR(10),
    operations INT
    );

    """
    organ_table = """
    CREATE TABLE IF NOT EXISTS Organ (
	organ_ID INT AUTO_INCREMENT PRIMARY KEY,
    organ_name VARCHAR(255),
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

#Populate the tables with some random data
def populate_tables(connection):
    donor_info = """
    INSERT INTO Donor VALUES
    ( NULL, 'AB', NULL , '21', 'Diabetes', 'Insulin', NULL, 'Insulin', '2021-11-29', '8048040891', 'hh@gmail.com', 'Chicago', 'Blood'),
    ( NULL, 'A', 'Heart' , '44', NULL, NULL, NULL, 'Vitamins', '2021-10-29', '8036040214', 'gg@gmail.com', 'Detroit', 'Both'),
    ( NULL, 'B', 'Brain' , '32', 'Cancer', NULL, '2020-10-30', 'Adderall', NULL, '8084670891', 'ii@gmail.com', 'Chicago', 'Organ'),
    ( NULL, 'O', 'Liver' , '25', 'Seizures', 'Heroin', NULL, 'Vicadin', '2010-07-19', '8042349021', 'kk@gmail.com', 'Richmond', 'Both'),
    ( NULL, 'A', NULL , '23', NULL, NULL, NULL, NULL, '2020-02-29', '800982932', 'll@gmail.com', 'Chicago', 'Blood');
    """
    # (Donor_ID, BloodType, Organs, Age, Disease, Drug Usage, lastTattooDate, MedicationHistory, LastDonation, phoneNumber, email, region, donortype)
    patient_info = """
    INSERT INTO Patient VALUES
    ( NULL, 'Jimmy', 'A', '21', 'Heart', 'Detroit', '0976232892', 'aa@gmail.com', '1'),
    ( NULL, 'Billy', 'AB', '42', 'Blood', 'Chicago', '9098128921', 'bb@gmail.com', '2'),
    ( NULL, 'Susan', 'O', '64', 'Brain', 'Richmond', '1837282392', 'cc@gmail.com', '3'),
    ( NULL, 'Mary', 'B', '13', 'Liver', 'Chicago', '0893412892', 'dd@gmail.com', '4'),
    ( NULL, 'James', 'A', '54', 'Blood', 'Chicago', '8093412892', 'ee@gmail.com', '5');
    """
    # (Patient_ID, name, bloodtype, age, needs, region, phonenumber, email, waitlistposition)
    doctor_info = """
    INSERT INTO Doctor VALUES
    (NULL, 'Dave', 'Heart', '200', 'Detroit', 'dave@doctor.com', '1230984758', 10),
    (NULL, 'John', 'Brain', '300', 'Chicago', 'john@doctor.com', '4530837158', 5),
    (NULL, 'Jill', 'Heart', '400', 'Richmond', 'jill@doctor.com', '8935984758', 17),
    (NULL, 'Bill', 'Liver', '150', 'Chicago', 'bill@doctor.com', '9835684758', 18),
    (NULL, 'Mary', 'Eye', '700', 'Chicago', 'mary@doctor.com', '9823784758', 12);
    """
    # (Doctor_ID, name, specialization, fee, region, email, phonenumber)
    organ_info = """
    INSERT INTO Organ VALUES
    (NULL, 'Heart', 130, '2021-12-02'),
    (NULL, 'Brain', 32, '2021-12-07'),
    (NULL, 'Liver', 114, '2021-12-12'),
    (NULL, 'Heart', 120, '2021-12-11'),
    (NULL, 'Eye', 23, '2021-01-15');
    """
    # (Organ_ID, name, shelflife, availbilitydate)
    hospital_info = """
    INSERT INTO Hospital VALUES
    (NULL, 'Mercy', 'Chicago', '300'),
    (NULL, 'Rush', 'Chicago', '5000'),
    (NULL, 'Healing', 'Seatle', '4000'),
    (NULL, 'Stacies', 'Detroit', '450'),
    (NULL, 'St. James', 'Richmond', '9040');
    """
    # (Hospital_ID, name, region, cost)
    execute_query(connection, donor_info)
    execute_query(connection, patient_info)
    execute_query(connection, doctor_info)
    execute_query(connection, organ_info)
    execute_query(connection, hospital_info)

#Used to delete all the tables
def drop_tables(connection):
    execute_query(connection, "DROP TABLE Donor")
    execute_query(connection, "DROP TABLE Patient")
    execute_query(connection, "DROP TABLE Doctor")
    execute_query(connection, "DROP TABLE Organ")
    execute_query(connection, "DROP TABLE Hospital")

#Any read queries are passed through this
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: '{e}'")

#Delete from a table based on the ID
def delete_from_table(connection, table, id):
    deleting = """
    DELETE FROM {} WHERE {}_ID = {};
    """.format(table, table.lower(), id)
    execute_query(connection, deleting)

#Add a new entry to any of the tables
def add_donor(connection, blood_type, organs, age, chronice_disease, drug_usage, last_tattoo_date, medication_history, last_donation, phone_number, email, region, donor_type):
    donor_insertion = """
    INSERT INTO Donor VALUES
    (NULL, '{}', '{}', {}, '{}', '{}', {}, '{}', {}, '{}', '{}', '{}', '{}');
    """.format(blood_type, organs, age, chronice_disease, drug_usage, last_tattoo_date, medication_history, last_donation, phone_number, email, region, donor_type)
    execute_query(connection, donor_insertion)

def add_hospital(connection, hospital_name, region, cost):
    hospital_insertion = """
    INSERT INTO Hospital VALUES
    (NULL, '{}', '{}', {});
    """.format(hospital_name, region, cost)
    execute_query(connection, hospital_insertion)

def add_patient(connection, patient_name, blood_type, age, needs, region, phone_number, email, waitlist_position):
    patient_insertion = """
    INSERT INTO Patient VALUES
    (NULL, '{}', '{}', {}, '{}', '{}', '{}', '{}', {});
    """.format(patient_name, blood_type, age, needs, region, phone_number, email, waitlist_position)
    execute_query(connection, patient_insertion)

def add_doctor(connection, doctor_name, specialization, fee, region, email, phone_number, operations):
    doctor_insertion = """
    INSERT INTO Doctor VALUES
    (NULL, '{}', '{}', {}, '{}', '{}', '{}', {});
    """.format(doctor_name, specialization, fee, region, email, phone_number, operations)
    execute_query(connection, doctor_insertion)

def add_organ(connection, organ_name, shelf_life, availablity_date):
    organ_insertion = """
    INSERT INTO Organ VALUES
    (NULL, '{}', {}, {});
    """.format(organ_name, shelf_life, availablity_date)
    execute_query(connection, organ_insertion)

#Returns the list of all the various tables.
def all_patients(connection):
    patients_info = """
    SELECT * FROM Patient;
    """
    return read_query(connection, patients_info)

def all_donors(connection):
    donors_info = """
    SELECT * FROM Donor;
    """
    return read_query(connection, donors_info)

def all_hospitals(connection):
    hospitals_info = """
    SELECT * FROM Hospital;
    """
    return read_query(connection, hospitals_info)

def all_doctors(connection):
    doctors_info = """
    SELECT * FROM Doctor;
    """
    return read_query(connection, doctors_info)

def all_organs(connection):
    organs_info = """
    SELECT * FROM Organ;
    """
    return read_query(connection, organs_info)

# 1. Organ Donor Lists Functions
def organ_region(connection, region):
    organ_region_query = """
    SELECT * FROM Donor WHERE region = '{}' AND (donorType = 'Organ' OR donorType = 'Both');
    """.format(region)
    return read_query(connection, organ_region_query)

def organ_organ(connection, organ):
    organ_organ_query = """
    SELECT * FROM Donor WHERE organ = '{}' AND (donorType = 'Organ' or donorType = 'both');
    """.format(organ)
    return read_query(connection, organ_organ_query)

def organ_specalized_doctor(connection, organ):
    organ_specalized_doctor_query = """
    SELECT * FROM Doctor WHERE specialization = '{}';  
    """.format(organ)
    return read_query(connection, organ_specalized_doctor_query)

#2. Blood Donor List
def blood_region(connection, region):
    blood_region_query = """
    SELECT * FROM Donor WHERE region = '{}' AND (donorType = 'Blood' OR donorType = 'Both');
    """.format(region)
    return read_query(connection, blood_region_query)

def blood_bloodtype(connection, bloodtype):
    blood_bloodtype_query = """
    SELECT * FROM Donor WHERE blood_type = '{}' AND (donorType = 'Blood' OR donorType = 'Both');
    """.format(bloodtype)
    return read_query(connection, blood_bloodtype_query)

def blood_bloodtype(connection):
    blood_availability_query = """
    SELECT * FROM Donor WHERE lastDonaitonTime < CURRENT_DATE() - INTERVAL 6 MONTH;
    """
    return read_query(connection, blood_availability_query)

def blood_age(connection, min, max):
    blood_age_query = """
    SELECT * FROM Donor WHERE age < {} AND age > {};
    """.format(max, min)
    return read_query(connection, blood_age_query)

#3. Donor Match List
#Organ matching between patient and donor based on requirements
def organdonor_matchlist(connection):
    matchlist_query = """
    SELECT Donor.donor_ID as donorID, Donor.bloodType as bloodType, Donor.organs as organs, Donor.region as region, Patient.patient_ID as patientID, Patient.patient_name as patientName
    FROM Donor
    INNER JOIN Patient on (Donor.bloodType = Patient.bloodType OR Donor.bloodType = "O" OR Patient.bloodType = "AB") AND (Donor.organs = Patient.needs) AND (Donor.region = Patient.region)
    ORDER BY region;
    """
    return read_query(connection, matchlist_query)
#Blood matching between patient and donor based on requirements
def blooddonor_matchlist(connection):
    matchlist_query = """
    SELECT Donor.donor_ID as donorID, Donor.bloodType as bloodType, Donor.region as region, Patient.patient_ID as patientID, Patient.patient_name as patientName
    FROM Donor
    INNER JOIN Patient on (Donor.bloodType = Patient.bloodType OR Donor.bloodType = "O" OR Patient.bloodType = "AB") AND (Donor.region = Patient.region)
    ORDER BY region;
    """
    return read_query(connection, matchlist_query)

#4. Income Report
#Just use the all_hospitals(connection) as it will return all the information on the hospital

def hospital_update_income(connection, id, amount):
    update = """
    UPDATE hospital SET cost = {} WHERE hospital_id = {};
    """.format(amount, id)
    cursor = connection.cursor()
    try:
        cursor.execute(update)
        connection.commit()
        print('Query successful')
    except Error as e:
        print(f"Error: '{e}'")

#5. Operations Report
def operations_report(connection):
    operations_report = """
    SELECT doctor_name, region, operations FROM Doctor
    ORDER BY region ASC, operations DESC;
    """
    return read_query(connection, operations_report)

#User Creation and Privileges
def doctor_user (connection):
    user_query="""
    CREATE USER IF NOT EXISTS 'doctor'@'localhost' IDENTIFIED BY 'doctorPassword';
    """
    privone_query="""
    GRANT ALL PRIVILEGES ON Donor TO doctor@localhost;
    """
    privtwo_query="""
    GRANT ALL PRIVILEGES ON Patient TO doctor@localhost;
    """
    privthree_query="""
    GRANT ALL PRIVILEGES ON Organ TO doctor@localhost;
    """
    execute_query(connection, user_query)
    execute_query(connection, privone_query)
    execute_query(connection, privtwo_query)
    execute_query(connection, privthree_query)

def patient_user (connection):
    user_query="""
    CREATE USER IF NOT EXISTS 'patient'@'localhost' IDENTIFIED BY 'patientPassword';
    """
    privone_query="""
    GRANT ALL PRIVILEGES ON Donor TO patient@localhost;
    """
    execute_query(connection, user_query)
    execute_query(connection, privone_query)

def admin_user (connection):
    user_query="""
    CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'adminPassword';
    """
    privone_query="""
    GRANT ALL PRIVILEGES ON Donor TO admin@localhost;
    """
    privtwo_query="""
    GRANT ALL PRIVILEGES ON Patient TO admin@localhost;
    """
    privthree_query="""
    GRANT ALL PRIVILEGES ON Organ TO admin@localhost;
    """
    privfour_query="""
    GRANT ALL PRIVILEGES ON Doctor TO admin@localhost;
    """
    privfive_query="""
    GRANT ALL PRIVILEGES ON Hospital TO admin@localhost;
    """
    execute_query(connection, user_query)
    execute_query(connection, privone_query)
    execute_query(connection, privtwo_query)
    execute_query(connection, privthree_query)
    execute_query(connection, privfour_query)
    execute_query(connection, privfive_query)

def input_user (connection, username, password):
    user_query="""
    CREATE USER IF NOT EXISTS '{}'@'localhost' IDENTIFIED BY '{}';
    """.format(username, password)
    execute_query(connection, user_query)   

def input_doctor_privilege (connection, username):
    priv_query="""
    GRANT ALL PRIVILEGES ON Doctor TO {}@localhost;
    """.format(username)
    execute_query(connection, priv_query)

def input_donor_privilege (connection, username):
    priv_query="""
    GRANT ALL PRIVILEGES ON Donor TO {}@localhost;
    """.format(username)
    execute_query(connection, priv_query)

def input_hospital_privilege (connection, username):
    priv_query="""
    GRANT ALL PRIVILEGES ON Hospital TO {}@localhost;
    """.format(username)
    execute_query(connection, priv_query)    

def input_organ_privilege (connection, username):
    priv_query="""
    GRANT ALL PRIVILEGES ON Organ TO {}@localhost;
    """.format(username)
    execute_query(connection, priv_query)

def input_patient_privilege (connection, username):
    priv_query="""
    GRANT ALL PRIVILEGES ON Patient TO {}@localhost;
    """.format(username)
    execute_query(connection, priv_query)

#can only verify off of username
def verify_user(connection, username):
    verify_query ="""
    SELECT user FROM mysql.user WHERE user = '{}';
    """.format(username)
    return read_query(connection, verify_query)

def verify_privileges(connection, username):
    priv_query="""
    SHOW GRANTS FOR '{}'@'localhost';
    """.format(username)
    return read_query(connection, priv_query)

def waitlist_position(connection):
    wait_query="""
    SELECT waitlistPosition FROM Patient ORDER BY waitlistPosition DESC LIMIT 1;
    """
    return read_query(connection, wait_query)

#server_connection_first()
#connection = server_connection()
#create_database(connection)
#create_tables(connection)
#populate_tables(connection)
#doctor_user(connection)
#patient_user(connection)
#admin_user(connection)
#results = verify_privileges
#(connection, 'doctor')
#print (results)
#drop_tables(connection)