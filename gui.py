from tkinter import* 
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
    if (verify_user(connection, user) != []):
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

    Label(frameLog, text='Illinois Tech Medicine: Save A Life inc.').grid(row=0, columnspan=3)
    Label(frameLog, text='Name: ').grid(row=1, sticky='w')
    Label(frameLog, text='Role').grid(row=2, sticky='w')

    b0 = Button(root, text='Patient Information', command=lambda:patientInfo(root)).grid(row=3, column=2)

    b1 = Button(root, text='Blood Donor List', command=lambda:bloodDonorList(root)).grid(row=4, column=1)
    b2 = Button(root, text='Organ Donor List', command=lambda:organDonorList(root)).grid(row=4, column=2)
    b3 = Button(root, text='Add New Donor', command=lambda:addNewDonor(root)).grid(row=4, column=3)

    b4 = Button(root, text='Add Organ to Donor', command=lambda:addOrganToDonor(root)).grid(row=5, column=1)
    b5 = Button(root, text='Donor Match List', command=lambda:donorMatchList(root)).grid(row=5, column=2)
    b6 = Button(root, text='Income Report', command=lambda:incomeReport(root)).grid(row=5, column=3)

    b7 = Button(root, text='Opperation Report', command=lambda:opperationReport(root)).grid(row=6, column=1)
    b8 = Button(root, text='Create Patient User', command=lambda:addNewPatient(root)).grid(row=6, column=2)
    b9 = Button(root, text='Create Doctor User', command=lambda:addNewDoctor(root)).grid(row=6, column=3)



def patientInfo(root):
    global privs
    if privs<2:
        return
    root.destroy()
    root=Tk()

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)

def bloodDonorList(root):
    root.destroy()
    root=Tk()

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)

def organDonorList(root):
    root.destroy()
    root=Tk()

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)

def addNewDonor(root):
    global privs
    if privs<2:
        return
    root.destroy()
    root=Tk()

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)

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

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)

def incomeReport(root):
    global privs
    if privs<3:
        return
    root.destroy()
    root=Tk()

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)

def opperationReport(root):
    global privs
    if privs<3:
        return
    root.destroy()
    root=Tk()

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)

def addNewPatient(root):
    global privs
    if privs<2:
        return
    root.destroy()
    root=Tk()

    patientName = str
    patientBloodType = str
    patientAge = int
    patientNeeds = str
    patientRegion = str
    patientPhoneNo = str
    patientEmail = str
    patientUsername = str
    patientPassword = str
    patientConfirmPassword = str

    Label(root, text='Add new Patient').grid(columnspan=2, row=0)
    Label(root, text='Name ').grid(row=1, column=0, sticky='e')
    Label(root, text='Blood Type ').grid(row=2, column=0, sticky='e')
    Label(root, text='Age ').grid(row=3, column=0, sticky='e')
    Label(root, text='Organ/Blood Needed ').grid(row=4, column=0, sticky='e')
    Label(root, text='Region ').grid(row=5, column=0, sticky='e')
    Label(root, text='Phone Number ').grid(row=6, column=0, sticky='e')
    Label(root, text='Email ').grid(row=7, column=0, sticky='e')
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
    entryUsername = Entry(root, textvariable=patientUsername).grid(row=9, column=1)
    entryPassword = Entry(root, textvariable=patientPassword, show="*").grid(row=10, column=1)
    entryConfirmPassword = Entry(root, textvariable=patientConfirmPassword, show="*").grid(row=11, column=1)

    # get the newest waitlist position and add 1 to get the new patient's position
    patientWaitlistPos = waitlist_position(connection)[0][0] + 1

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=8,column=0)

    submit = Button(root, text="Submit", command=lambda:submitNewPatient(root, patientName, patientBloodType, patientAge, patientNeeds, patientRegion, patientPhoneNo, patientEmail, patientWaitlistPos)).grid(row=8,column=1)

def submitNewPatient(root, patientName, patientBloodType, patientAge, patientNeeds, patientRegion, patientPhoneNo, patientEmail, patientWaitlistPos):
    add_patient(connection, patientName, patientBloodType, patientAge, patientNeeds, patientRegion, patientPhoneNo, patientEmail, patientWaitlistPos)
    openHome(root)


def addNewDoctor(root):
    global privs
    if privs<3:
        return
    root.destroy()
    root=Tk()

    # Back Button
    back = Button(root, text="Back", command=lambda:openHome(root)).grid(row=0,column=0)


    
# ---------------------------------Keep At End---------------------------
if __name__ == '__main__':
    main(root)
    root.mainloop()
