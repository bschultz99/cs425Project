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
      
    def __init__(self,root, total_rows, total_columns, lst):
        color = 'blue'
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = Entry(root, width=15, fg=color,
                               font=('Arial',12,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
            color="black"
                
        back = Button(root, text="Back", command=lambda:patientInfo(root)).grid(row=total_rows+1,columnspan=total_columns)


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
        buildTable(root, keys, read_query(connection, query))
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
    
        buildTable(root, keys, read_query(connection, query))


def buildTable(root, keys, query):
    keys.insert(0,"patient_ID")
    query.insert(0,keys)
    lst = query
    
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    
    # create root window
    t = Table(root, total_rows, total_columns, lst)
    





    
            





    


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
    
# ---------------------------------Keep At End---------------------------
if __name__ == '__main__':
    main(root)
    root.mainloop()
