# CS 425 Final Project
# By Bryant Schultz, Jared Wagler, and Sean Graney
#
# Contributions:
# Bryant Schultz - Backend MySQL Server and Database.py Python - SQL interfacing library
# Jared Wagler - Front-end GUI design (gui.py) (Add Donor, Doctor, and Patient forms and SQL additions)
# Sean Graney - Front-end GUI design (gui.py) (Blood Donor, Organ Donor, and Donor Match Lists; Patient Information, Operation, and Income Report; Login GUI)
#
# SQL module used: MySQL
# Language used: Python
# Front-end GUI library: Tkinter

from tkinter import*
from typing import List
from tkcalendar import*
from Database import*

# Database Connection
connection = server_connection_first()
create_database(connection)
connection = server_connection()
create_tables(connection)
#populate_tables(connection)

# Adding example Users
doctor_user(connection)
patient_user(connection)
admin_user(connection)

# Create Root Window
root = Tk()
privs = 1


def main(root):
    # Create login screen
    login(root)
    

# ----------------login screen-------------------
def login(root):
    # Open window with dimension AxA
    root.geometry('250x100')

    # declaring string variable
    # for storing name and password
    name_var=StringVar()
    passw_var=StringVar()

    frameLog = Frame(root)
    frameLog.grid(row=0, column=2) 

    Label(frameLog, text='Login').grid(row=0)
    Label(root, text='Username').grid(row=1)
    Label(root, text='Password').grid(row=2)

    username = Entry(root, textvariable=name_var)
    password = Entry(root, textvariable=passw_var, show="*")
    username.grid(row=1, column=2)
    password.grid(row=2, column=2)

    loginButton = Button(root, text='Login', command=lambda : checkLogin(name_var, passw_var, root))
    loginButton.grid(row=3, column=2)



# Checks login status
def checkLogin(username, password, root):
    global privs
    user = username.get()
    passw = password.get()

    print("The name is: " + user)
    print("The password is: " + passw)

    # login success
    if (verify_user(connection, user) != [] and passw!=""):
        # set privileges
        role = len(verify_privileges(connection, user))   
        if role==6:
            privs=3
        elif role==4:
            privs=2
        
        openHome(root)

    # login fail
    username.set("")
    password.set("")


# Create Home
def openHome(root):
    root.destroy()
    root = Tk()

    # root.geometry('800x600')
    
    frameLog = Frame(root)
    frameLog.grid(row=0, column=2) 

    Label(frameLog, text='Illinois Tech Medicine: Save A Life inc.', bg="red", height="2", font=('Arial',12,'bold')).grid(row=0, columnspan=3)

    b0 = Button(root, text='Patient Information', width="30", command=lambda:patientInfo(root)).grid(row=5, column=1)

    b1 = Button(root, text='Blood Donor List', width='30', command=lambda:bloodDonorList(root)).grid(row=4, column=1)
    b2 = Button(root, text='Organ Donor List', width='30', command=lambda:organDonorList(root)).grid(row=4, column=2)
    b3 = Button(root, text='Add New Donor', width='30', command=lambda:addNewDonor(root)).grid(row=4, column=3)

    b4 = Button(root, text='----------------------------------------------------------------------------------------------------------------------------------------------', width="105").grid(row=3, column=1, columnspan=3)
    b5 = Button(root, text='Donor Match List', width='30', command=lambda:donorMatchList(root)).grid(row=5, column=2)
    b6 = Button(root, text='Income Report', width='30', command=lambda:incomeReport(root)).grid(row=5, column=3)

    b7 = Button(root, text='Operation Report', width='30', command=lambda:operationReport(root)).grid(row=6, column=1)
    b8 = Button(root, text='Create Patient User', width='30', command=lambda:addNewPatient(root)).grid(row=6, column=2)
    b9 = Button(root, text='Create Doctor User', width='30', command=lambda:addNewDoctor(root)).grid(row=6, column=3)



def patientInfo(root):
    global privs
    if privs<2:
        return
    root.destroy()
    root=Tk()


    patientName = StringVar()
    patientBloodType = StringVar()
    patientAge = StringVar()
    patientNeeds = StringVar()
    patientRegion = StringVar()
    patientPhoneNo = StringVar()
    patientEmail = StringVar()
    patientWaitPos = StringVar()



    Label(root, text='Patient Info Lookup').grid(columnspan=2, row=0)
    Label(root, text='Name ').grid(row=1, column=0, sticky='e')
    Label(root, text='Blood Type ').grid(row=2, column=0, sticky='e')
    Label(root, text='Age ').grid(row=3, column=0, sticky='e')
    Label(root, text='Organ/Blood Needed ').grid(row=4, column=0, sticky='e')
    Label(root, text='Region ').grid(row=5, column=0, sticky='e')
    Label(root, text='Phone Number ').grid(row=6, column=0, sticky='e')
    Label(root, text='Email ').grid(row=7, column=0, sticky='e')
    Label(root, text='Waitlist Position ').grid(row=8, column=0, sticky='e')

    entryName = Entry(root, textvariable=patientName)
    entryBloodType = Entry(root, textvariable=patientBloodType)
    entryAge = Entry(root, textvariable=patientAge)
    entryNeeds = Entry(root, textvariable=patientNeeds)
    entryRegion = Entry(root, textvariable=patientRegion)
    entryPhoneNo = Entry(root, textvariable=patientPhoneNo)
    entryEmail = Entry(root, textvariable=patientEmail)
    entryWaitPos = Entry(root, textvariable=patientWaitPos)

    entryName.grid(row=1, column=1)
    entryBloodType.grid(row=2, column=1)
    entryAge.grid(row=3, column=1)
    entryNeeds.grid(row=4, column=1)
    entryRegion.grid(row=5, column=1)
    entryPhoneNo.grid(row=6, column=1)
    entryEmail.grid(row=7, column=1)
    entryWaitPos.grid(row=8, column=1)

    ret = [patientName, patientBloodType, patientAge, patientNeeds, patientRegion, patientPhoneNo, patientEmail, patientWaitPos]

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=9,column=0)
    submit = Button(root, text="Submit", command=lambda:patientFilter(root, ret)).grid(row=9,column=1)

class Table:
      
    def __init__(self,root, total_rows, total_columns, lst, color):
        color = color
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = Entry(root, width=12, fg=color,
                               font=('Arial',12,'bold'))
                  
                self.e.grid(row=i, column=j)
                if not lst[i][j]:
                    self.e.insert(END, "None")
                else:
                    self.e.insert(END, lst[i][j])
            color="black"
                
        back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=total_rows+1,columnspan=total_columns)


def patientFilter(root, lst):
    root.destroy()
    root = Tk()

    query = """SELECT * FROM Patient"""
    filter = []
    empty = 0

    for x in lst:
        if len(x.get())==0:
            filter.append("*")
            empty+=1
        else:
            filter.append(x.get())
    keys = ['patient_name', 'bloodType', 'age', 'needs', 'region', 'phoneNumber', 'email', 'waitlistPosition']
    map = dict(zip(keys, filter))
    print(map)

    # query creation
    if empty==len(keys):
        query+=""";"""
        keys.insert(0,"patient_ID")
        buildTable(root, keys, read_query(connection, query), "blue")
    else:
        query+=""" WHERE """
        for x in map.items():
            if (x[1]=="*" or x[1]==0):
                continue
            else:
                query=query+x[0]+"""='"""+x[1]+"""' AND """
        
        if query[-4:]=="""AND """:
            query=query[:-5]
        query+=";"
        keys.insert(0,"patient_ID")
        buildTable(root, keys, read_query(connection, query), "blue")


def buildTable(root, keys, query, color):
    query.insert(0,keys)
    lst = query
    
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    
    # create root window
    t = Table(root, total_rows, total_columns, lst, color)
    


def bloodDonorList(root):
    root.destroy()
    root=Tk()

    bloodType = StringVar()
    organs = StringVar()
    age = StringVar()
    chronicDisease = StringVar()
    drugUsage = StringVar()
    lastTattooDate = StringVar()
    medicationHistory = StringVar()
    lastDonationTime = StringVar()
    phoneNumber = StringVar()
    email = StringVar()
    region = StringVar()
    


    Label(root, text='Blood Donor List').grid(columnspan=2, row=0)
    Label(root, text='Blood Type ').grid(row=1, column=0, sticky='e')
    Label(root, text='Organs ').grid(row=2, column=0, sticky='e')
    Label(root, text='Age ').grid(row=3, column=0, sticky='e')
    Label(root, text='Chronic Disease ').grid(row=4, column=0, sticky='e')
    Label(root, text='Drug Usage ').grid(row=5, column=0, sticky='e')
    Label(root, text='last Tattoo Date ').grid(row=6, column=0, sticky='e')
    Label(root, text='Medication History ').grid(row=7, column=0, sticky='e')
    Label(root, text='Last Donation Date ').grid(row=8, column=0, sticky='e')
    Label(root, text='Phone Number ').grid(row=9, column=0, sticky='e')
    Label(root, text='Email ').grid(row=10, column=0, sticky='e')
    Label(root, text='Region ').grid(row=11, column=0, sticky='e')


    entryName = Entry(root, textvariable=bloodType)
    entryBloodType = Entry(root, textvariable=organs)
    entryAge = Entry(root, textvariable=age)
    entryNeeds = Entry(root, textvariable=chronicDisease)
    entryRegion = Entry(root, textvariable=drugUsage)
    entryPhoneNo = Entry(root, textvariable=lastTattooDate)
    entryEmail = Entry(root, textvariable=medicationHistory)
    entryWaitPos = Entry(root, textvariable=lastDonationTime)
    entry1 = Entry(root, textvariable=phoneNumber)
    entry2 = Entry(root, textvariable=email)
    entry3 = Entry(root, textvariable=region)

    entryName.grid(row=1, column=1)
    entryBloodType.grid(row=2, column=1)
    entryAge.grid(row=3, column=1)
    entryNeeds.grid(row=4, column=1)
    entryRegion.grid(row=5, column=1)
    entryPhoneNo.grid(row=6, column=1)
    entryEmail.grid(row=7, column=1)
    entryWaitPos.grid(row=8, column=1)
    entry1.grid(row=9, column=1)
    entry2.grid(row=10, column=1)
    entry3.grid(row=11, column=1)


    ret = [bloodType, organs, age, chronicDisease, drugUsage, lastTattooDate, medicationHistory, lastDonationTime, phoneNumber, email, region]

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=12,column=0)
    submit = Button(root, text="Submit", command=lambda:donorFilter(root, ret)).grid(row=12,column=1)


def organDonorList(root):
    root.destroy()
    root=Tk()

    bloodType = StringVar()
    organs = StringVar()
    age = StringVar()
    chronicDisease = StringVar()
    drugUsage = StringVar()
    lastTattooDate = StringVar()
    medicationHistory = StringVar()
    lastDonationTime = StringVar()
    phoneNumber = StringVar()
    email = StringVar()
    region = StringVar()
    


    Label(root, text="Organ Donor List").grid(columnspan=2, row=0)
    Label(root, text='Blood Type ').grid(row=1, column=0, sticky='e')
    Label(root, text='Organs ').grid(row=2, column=0, sticky='e')
    Label(root, text='Age ').grid(row=3, column=0, sticky='e')
    Label(root, text='Chronic Disease ').grid(row=4, column=0, sticky='e')
    Label(root, text='Drug Usage ').grid(row=5, column=0, sticky='e')
    Label(root, text='last Tattoo Date ').grid(row=6, column=0, sticky='e')
    Label(root, text='Medication History ').grid(row=7, column=0, sticky='e')
    Label(root, text='Last Donation Date ').grid(row=8, column=0, sticky='e')
    Label(root, text='Phone Number ').grid(row=9, column=0, sticky='e')
    Label(root, text='Email ').grid(row=10, column=0, sticky='e')
    Label(root, text='Region ').grid(row=11, column=0, sticky='e')


    entryName = Entry(root, textvariable=bloodType)
    entryBloodType = Entry(root, textvariable=organs)
    entryAge = Entry(root, textvariable=age)
    entryNeeds = Entry(root, textvariable=chronicDisease)
    entryRegion = Entry(root, textvariable=drugUsage)
    entryPhoneNo = Entry(root, textvariable=lastTattooDate)
    entryEmail = Entry(root, textvariable=medicationHistory)
    entryWaitPos = Entry(root, textvariable=lastDonationTime)
    entry1 = Entry(root, textvariable=phoneNumber)
    entry2 = Entry(root, textvariable=email)
    entry3 = Entry(root, textvariable=region)

    entryName.grid(row=1, column=1)
    entryBloodType.grid(row=2, column=1)
    entryAge.grid(row=3, column=1)
    entryNeeds.grid(row=4, column=1)
    entryRegion.grid(row=5, column=1)
    entryPhoneNo.grid(row=6, column=1)
    entryEmail.grid(row=7, column=1)
    entryWaitPos.grid(row=8, column=1)
    entry1.grid(row=9, column=1)
    entry2.grid(row=10, column=1)
    entry3.grid(row=11, column=1)


    ret = [bloodType, organs, age, chronicDisease, drugUsage, lastTattooDate, medicationHistory, lastDonationTime, phoneNumber, email, region]

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=12,column=0)
    submit = Button(root, text="Submit", command=lambda:donorFilter2(root, ret)).grid(row=12,column=1)


def donorFilter(root, lst):
    root.destroy()
    root = Tk()

    query = """SELECT * FROM Donor WHERE (donorType = 'Organ' OR donorType = 'Both')"""
    filter = []
    empty = 0

    for x in lst:
        if len(x.get())==0:
            filter.append("*")
            empty+=1
        else:
            filter.append(x.get())

    keys = ['bloodType', 'organs', 'age', 'chronicDisease', 'drugUsage', 'lastTattooDate', 'medicationHistory', 'lastDonationTime', 'phoneNumber', 'email', 'region', 'donorType']
    map = dict(zip(keys, filter))

    # query creation
    if empty==len(keys):
        query+=""";"""
        keys.insert(0,"donor_ID")
        buildTable(root, keys, read_query(connection, query), "red")
    else:
        for x in map.items():
            if (x[1]=="*" or x[1]==0):
                continue
            else:
                if not x[1]:
                    x[1]= "None"
                query=query+""" AND """+x[0]+"""='"""+x[1]+"""' AND """
        
        if query[-4:]=="""AND """:
            query=query[:-5]
        query+=";"
        keys.insert(0,"donor_ID")
        print(query)
        buildTable(root, keys, read_query(connection, query), "red")


def donorFilter2(root, lst):
    root.destroy()
    root = Tk()

    query = """SELECT * FROM Donor WHERE (donorType = 'Blood' OR donorType = 'Both')"""
    filter = []
    empty = 0

    for x in lst:
        if len(x.get())==0:
            filter.append("*")
            empty+=1
        else:
            filter.append(x.get())

    keys = ['bloodType', 'organs', 'age', 'chronicDisease', 'drugUsage', 'lastTattooDate', 'medicationHistory', 'lastDonationTime', 'phoneNumber', 'email', 'region', 'donorType']
    map = dict(zip(keys, filter))

    # query creation
    if empty==len(keys):
        query+=""";"""
        keys.insert(0,"donor_ID")
        buildTable(root, keys, read_query(connection, query), "green")
    else:
        for x in map.items():
            if (x[1]=="*" or x[1]==0):
                continue
            else:
                if not x[1]:
                    x[1]= "None"
                query=query+""" AND """+x[0]+"""='"""+x[1]+"""' AND """
        
        if query[-4:]=="""AND """:
            query=query[:-5]
        query+=";"
        keys.insert(0,"donor_ID")
        print(query)
        buildTable(root, keys, read_query(connection, query), "green")


def addOrganToDonor(root):
    global privs
    if privs<2:
        return
    root.destroy()
    root=Tk()

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)

def donorMatchList(root):
    global privs
    if privs<2:
        return
    root.destroy()
    root=Tk()

    Label(root, text='Donor Matching List').grid(row=0, columnspan=2)

    v = StringVar(root, "1")

    values = {"Organ Match" : "1",
        "Blood Match" : "2"}

    count=1
    for (text, value) in values.items():
        Radiobutton(root, text = text, variable = v,
            value = value).grid(row=count, columnspan=2)
        count+=1

    submit = Button(root, text="Submit", command=lambda:matchList(root, v.get())).grid(row=3,column=1)


    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=3,column=0)

def matchList(root, v):
    root.destroy()
    root=Tk()
    
    print(v)
    if v=='1':
        lst = organdonor_matchlist(connection)
        lst.insert(0, ("Donor_ID", "Blood Type", "Organ", "Region", "Patient ID", "Patient Name"))

        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])
        
        # create root window
        r = Table(root, total_rows, total_columns, lst, 'red')
    else:
        lst = blooddonor_matchlist(connection)
        lst.insert(0, ("Donor_ID", "Blood Type", "Region", "Patient ID", "Patient Name"))

        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])
        
        # create root window
        t = Table(root, total_rows, total_columns, lst, 'purple')

def incomeReport(root):
    global privs
    if privs<3:
        return
    root.destroy()
    root=Tk()

    lst = all_hospitals(connection)
    lst.insert(0, ("ID", "Hospital", "Region", "Income"))

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    
    # create root window
    t = Table(root, total_rows, total_columns, lst, 'purple')

def operationReport(root):
    global privs
    if privs<3:
        return
    root.destroy()
    root=Tk()
    
    lst = operations_report(connection)
    lst.insert(0, ("Doctor", "Location", "Total"))

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    
    # create root window
    t = Table(root, total_rows, total_columns, lst, 'orange')

def addNewPatient(root):
    global privs
    if privs<2:
        return
    root.destroy()
    root=Tk()

    patientName = StringVar()
    patientBloodType = StringVar()
    patientAge = IntVar()
    patientNeeds = StringVar()
    patientRegion = StringVar()
    patientPhoneNo = StringVar()
    patientEmail = StringVar()
    patientUsername = StringVar()
    patientPassword = StringVar()
    patientConfirmPassword = StringVar()

    Label(root, text='Add new Patient').grid(columnspan=2, row=0)
    Label(root, text='Name ').grid(row=1, column=0, sticky='e')
    Label(root, text='Blood Type ').grid(row=2, column=0, sticky='e')
    Label(root, text='Age ').grid(row=3, column=0, sticky='e')
    Label(root, text='Organ/Blood Needed ').grid(row=4, column=0, sticky='e')
    Label(root, text='Region ').grid(row=5, column=0, sticky='e')
    Label(root, text='Phone Number ').grid(row=6, column=0, sticky='e')
    Label(root, text='Email ').grid(row=7, column=0, sticky='e')
    Label(root, text='Create a Username and Password').grid(columnspan=2, row=8)
    Label(root, text='Username ').grid(row=9, column=0, sticky='e')
    Label(root, text='Password ').grid(row=10, column=0, sticky='e')
    Label(root, text='Confirm Password ').grid(row=11, column=0, sticky='e')

    entryName = Entry(root, textvariable=patientName).grid(row=1, column=1)
    entryBloodType = Entry(root, textvariable=patientBloodType).grid(row=2, column=1)
    entryAge = Entry(root, textvariable=patientAge).grid(row=3, column=1)
    entryNeeds = Entry(root, textvariable=patientNeeds).grid(row=4, column=1)
    entryRegion = Entry(root, textvariable=patientRegion).grid(row=5, column=1)
    entryPhoneNo = Entry(root, textvariable=patientPhoneNo).grid(row=6, column=1)
    entryEmail = Entry(root, textvariable=patientEmail).grid(row=7, column=1)
    entryUsername = Entry(root, textvariable=patientUsername)
    entryPassword = Entry(root, textvariable=patientPassword, show="*")
    entryConfirmPassword = Entry(root, textvariable=patientConfirmPassword, show="*")

    entryUsername.grid(row=9, column=1)
    entryPassword.grid(row=10, column=1)
    entryConfirmPassword.grid(row=11, column=1)

    # get the newest waitlist position and add 1 to get the new patient's position
    patientWaitlistPos = waitlist_position(connection)[0][0] + 1

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=12,column=0)

    submit = Button(root, text="Submit", command=lambda:submitNewPatient(root, patientName.get(), patientBloodType.get(), patientAge.get(), patientNeeds.get(), patientRegion.get(), patientPhoneNo.get(), patientEmail.get(), patientWaitlistPos, patientUsername.get(), patientPassword.get(), patientConfirmPassword.get(), entryUsername, entryPassword, entryConfirmPassword)).grid(row=12,column=1)

def submitNewPatient(root, patientName, patientBloodType, patientAge, patientNeeds, patientRegion, patientPhoneNo, patientEmail, patientWaitlistPos, patientUsername, patientPassword, patientConfirmPassword, entryUsername, entryPassword, entryConfirmPassword):
    if(patientPassword == patientConfirmPassword):
        add_patient(connection, patientName, patientBloodType, patientAge, patientNeeds, patientRegion, patientPhoneNo, patientEmail, patientWaitlistPos)
        input_user(connection, patientUsername, patientPassword)
        input_donor_privilege(connection, patientUsername)
        openHome(root)
    else:
        Label(root, text='Passwords Do Not Match. Try Again').grid(columnspan=2, row=8)
        entryUsername.delete(0, END)
        entryPassword.delete(0, END)
        entryConfirmPassword.delete(0, END)

def addNewDoctor(root):
    global privs
    if privs<3:
        return
    root.destroy()
    root=Tk()

    doctorName = StringVar()
    doctorSpec = StringVar()
    doctorFee = IntVar()
    doctorRegion = StringVar()
    doctorEmail = StringVar()
    doctorPhoneNo = StringVar()
    doctorOperations = 0
    doctorUsername = StringVar()
    doctorPassword = StringVar()
    doctorConfirmPassword = StringVar()

    Label(root, text='Add new Doctor').grid(columnspan=2, row=0)
    Label(root, text='Name ').grid(row=1, column=0, sticky='e')
    Label(root, text='Specialization ').grid(row=2, column=0, sticky='e')
    Label(root, text='Fee ').grid(row=3, column=0, sticky='e')
    Label(root, text='Region ').grid(row=4, column=0, sticky='e')
    Label(root, text='Email ').grid(row=5, column=0, sticky='e')
    Label(root, text='Phone Number ').grid(row=6, column=0, sticky='e')
    Label(root, text='Create a Username and Password').grid(columnspan=2, row=7)
    Label(root, text='Username ').grid(row=8, column=0, sticky='e')
    Label(root, text='Password ').grid(row=9, column=0, sticky='e')
    Label(root, text='Confirm Password ').grid(row=10, column=0, sticky='e')
    
    entryName = Entry(root, textvariable=doctorName).grid(row=1, column=1)
    entrySpec = Entry(root, textvariable=doctorSpec).grid(row=2, column=1)
    entryFee = Entry(root, textvariable=doctorFee).grid(row=3, column=1)
    entryRegion = Entry(root, textvariable=doctorRegion).grid(row=4, column=1)
    entryEmail = Entry(root, textvariable=doctorEmail).grid(row=5, column=1)
    entryPhoneNo = Entry(root, textvariable=doctorPhoneNo).grid(row=6, column=1)
    entryUsername = Entry(root, textvariable=doctorUsername)
    entryPassword = Entry(root, textvariable=doctorPassword, show="*")
    entryConfirmPassword = Entry(root, textvariable=doctorConfirmPassword, show="*")

    entryUsername.grid(row=8, column=1)
    entryPassword.grid(row=9, column=1)
    entryConfirmPassword.grid(row=10, column=1)

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=11,column=0)

    submit = Button(root, text="Submit", command=lambda:submitNewDoctor(root, doctorName.get(), doctorSpec.get(), doctorFee.get(), doctorRegion.get(), doctorEmail.get(), doctorPhoneNo.get(), doctorOperations, doctorUsername.get(), doctorPassword.get(), doctorConfirmPassword.get(), entryUsername, entryPassword, entryConfirmPassword)).grid(row=11,column=1)


def submitNewDoctor(root, doctorName, doctorSpec, doctorFee, doctorRegion, doctorEmail, doctorPhoneNo, doctorOperations, doctorUsername, doctorPassword, doctorConfirmPassword, entryUsername, entryPassword, entryConfirmPassword):
    if(doctorPassword == doctorConfirmPassword):
        add_doctor(connection, doctorName, doctorSpec, doctorFee, doctorRegion, doctorEmail, doctorPhoneNo, doctorOperations)
        input_user(connection, doctorUsername, doctorPassword)
        input_donor_privilege(connection, doctorUsername)
        input_patient_privilege(connection, doctorUsername)
        input_organ_privilege(connection, doctorUsername)
        openHome(root)
    else:
        Label(root, text='Passwords Do Not Match. Try Again').grid(columnspan=2, row=7)
        entryUsername.delete(0, END)
        entryPassword.delete(0, END)
        entryConfirmPassword.delete(0, END)

def addNewDonor(root, initialFlag = FALSE):
    global privs
    if privs<2:
        return
    root.destroy()
    root=Tk()

    donorBloodType = StringVar()
    donorRadioSelection = StringVar()
    donorOrgans = StringVar()
    donorAge = IntVar()
    donorDisease = StringVar()
    donorDrugs = StringVar()
    donorLastTattoo = StringVar()
    donorMedication = StringVar()
    donorLastDonated = StringVar()
    donorPhoneNo = StringVar()
    donorEmail = StringVar()
    donorRegion = StringVar()
    donorFlag1 = BooleanVar()
    donorFlag2 = BooleanVar()

    labelOrgans = Label(root, text='Organ ')
    entryOrgans = Entry(root, textvariable=donorOrgans)
    
    def hideDates():
        if donorFlag1.get():
            entryLastTattoo.grid_remove()
        else:
            entryLastTattoo.grid(row=9, column=1)

        if donorFlag2.get():
            entryLastDonated.grid_remove()
        else:
            entryLastDonated.grid(row=12, column=1)

    entryLastTattoo = DateEntry(root, selectmode='day', textvariable=donorLastTattoo, date_pattern="yyyy-MM-dd")
    entryLastDonated = DateEntry(root, selectmode='day', textvariable=donorLastDonated, date_pattern="yyyy-MM-dd")
    entryTattooBox = Checkbutton(root, text="No Tattoos", variable=donorFlag1, command=hideDates)
    entryDonatedBox = Checkbutton(root, text="No Prior Donation", variable=donorFlag2, command=hideDates)

    if(initialFlag == FALSE):
        entryLastTattoo.grid(row=9, column=1)
        entryLastDonated.grid(row=12, column=1)
        entryTattooBox.grid(row=10, column=1)
        entryDonatedBox.grid(row=13, column=1)
        tattooDate = TRUE
        donatedDate = TRUE
        initialFlag = TRUE
        donorDonationType = "Blood"

    def expandForm():
        if(donorRadioSelection.get() == "organs"):
            labelOrgans.grid(row=4, column=0, sticky='e')
            entryOrgans.grid(row=4, column=1)
            donorDonationType = "Organ"
        elif(donorRadioSelection.get() == "both"):
            labelOrgans.grid(row=4, column=0, sticky='e')
            entryOrgans.grid(row=4, column=1)
            donorDonationType = "Both"
        else:
            labelOrgans.grid_remove()
            entryOrgans.grid_remove()
            donorDonationType = "Blood"
        
    Label(root, text='Add new Donor').grid(columnspan=2, row=0)
    Label(root, text='Donor Type ').grid(row=1, column=0, sticky='e')
    Label(root, text='Blood Type ').grid(row=5, column=0, sticky='e')
    Label(root, text='Age ').grid(row=6, column=0, sticky='e')
    Label(root, text='Disease(s) ').grid(row=7, column=0, sticky='e')
    Label(root, text='Drug(s) Used ').grid(row=8, column=0, sticky='e')
    Label(root, text='Date of Last Tattoo ').grid(row=9, column=0, sticky='e')
    Label(root, text='Medication(s) Used ').grid(row=11, column=0, sticky='e')
    Label(root, text='Date of Last Donation ').grid(row=12, column=0, sticky='e')
    Label(root, text='Phone Number ').grid(row=14, column=0, sticky='e')
    Label(root, text='Email ').grid(row=15, column=0, sticky='e')
    Label(root, text='Region ').grid(row=16, column=0, sticky='e')

    entryBloodType = Entry(root, textvariable=donorBloodType).grid(row=5, column=1)
    entryAge = Entry(root, textvariable=donorAge).grid(row=6, column=1)
    entryDisease = Entry(root, textvariable=donorDisease).grid(row=7, column=1)
    entryDrugs = Entry(root, textvariable=donorDrugs).grid(row=8, column=1)
    entryMedication = Entry(root, textvariable=donorMedication).grid(row=11, column=1)
    entryPhoneNo = Entry(root, textvariable=donorPhoneNo).grid(row=14, column=1)
    entryEmail = Entry(root, textvariable=donorEmail).grid(row=15, column=1)
    entryRegion = Entry(root, textvariable=donorRegion).grid(row=16, column=1)

    entryRadioBlood = Radiobutton(root, text="Blood", variable=donorRadioSelection, value="blood", command=expandForm).grid(row=1, column=1, sticky='w')
    entryRadioOrgan = Radiobutton(root, text="Organs", variable=donorRadioSelection, value="organs", command=expandForm).grid(row=2, column=1, sticky='w')
    entryRadioOrgan = Radiobutton(root, text="Both", variable=donorRadioSelection, value="both", command=expandForm).grid(row=3, column=1, sticky='w')

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=17, column=0)

    submit = Button(root, text="Submit", command=lambda:exportList(root, donorBloodType.get(), donorOrgans.get(), donorAge.get(), donorDisease.get(), donorDrugs.get(), donorLastTattoo.get(), donorFlag1.get(), donorMedication.get(), donorLastDonated.get(), donorFlag2.get(), donorPhoneNo.get(), donorEmail.get(), donorRegion.get(), donorDonationType)).grid(row=17, column=1)

def submitNewDonor(root, list):
    add_donor(connection, list[0], list[1], list[2], list[3], list[4], list[5],
              list[6], list[7], list[8], list[9], list[10], list[11])
    print(all_donors(connection))
    openHome(root)

def exportList(root, donorBloodType, donorOrgans, donorAge, donorDisease, donorDrugs, donorLastTattoo, tattooDate,
               donorMedication, donorLastDonated, donatedDate, donorPhoneNo, donorEmail, donorRegion, donorDonationType):
    returnList = []
    print(tattooDate)
    returnList.append(donorBloodType)
    if(donorDonationType == "Blood"):
        returnList.append(None)
    else:
        returnList.append(donorOrgans)
    returnList.append(donorAge)
    returnList.append(donorDisease)
    returnList.append(donorDrugs)
    if tattooDate:
        returnList.append("")
    else:
        returnList.append(donorLastTattoo)
    returnList.append(donorMedication)
    if donatedDate:
        returnList.append("")
    else:
        returnList.append(donorLastDonated)
    returnList.append(donorPhoneNo)
    returnList.append(donorEmail)
    returnList.append(donorRegion)
    returnList.append(donorDonationType)

    for listItem in range(len(returnList)):
        if(returnList[listItem] == ""):
            returnList[listItem] = "NULL"
    print(returnList)
    
    submitNewDonor(root, returnList)

# ---------------------------------Keep At End---------------------------
if __name__ == '__main__':
    main(root)
    root.mainloop()
