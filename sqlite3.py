import  sqlite3
from sqlite3 import Error
def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return connection

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"DonorSystem.db"
    sql_create_donor_table = """CREATE TABLE IF NOT exists Donor (
	                                donor_ID integer PRIMARY KEY,
                                    bloodType text,
                                    age integer,
                                    chronicDisease text,
                                    drugUsage text,
                                    lastTattooDate text,
                                    medicationHistory text,
                                    lastDonaitonTime text,
                                    phoneNumber text,
                                    email text,
                                    region text,
                                    donorType text,
                                    );"""

    sql_create_patient_table = """CREATE TABLE Patient (
                                    patient_ID integer PRIMARY KEY,
                                    patient_name text,
                                    bloodType text,
                                    age integer,
                                    needs text,
                                    region text,
                                    phoneNumber text,
                                    email text,
                                    waitlistPosition integer,
                                    );"""








#connection = sqlite3.connect('DonorSystem.db')
#cursor = connection.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS Hospital (Hospital_ID INT, Name TEXT, Region TEXT, Cost INT)''')
#cursor.execute('''INSERT INTO Hospital (1, 'Mercy', 'Chicago', 100)''')
#for row in cursor.execute('Select * FROM Hospital ORDER BY Cost'):
#    print(row)
#connection.commit
#connection.close