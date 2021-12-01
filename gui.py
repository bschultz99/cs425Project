from tkinter import* 
from Database import*

connection = server_connection_first()
create_database(connection)
connection = server_connection()
create_tables(connection)
#populate_tables(connection)

# Create Root Window
root = Tk()
logged = False


def main():
    # Create login screen
    login()
    
        
# ----------------login screen-------------------
def login():
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
    user = username.get()
    passw = password.get()

    print("The name is: " + user)
    print("The password is: " + passw)

    #read_query(connection)

    username.set("")
    password.set("")

    addNewPatient(root)

# Requirement 1
# Add new users
# Add a patient or doctor
def addNewPatient(root):
    root.destroy()
    root = Tk()

    root.geometry('250x500')

    patientName = StringVar()
    patientBloodType = StringVar()
    patientAge = StringVar()
    patientNeeds = StringVar()
    patientRegion = StringVar()
    patientPhoneNo = StringVar()
    patientEmail = StringVar()
    patientWaitPos = StringVar()



    Label(root, text='Add new Patient').grid(columnspan=2, row=0)
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

    
# ---------------------------------Keep At End---------------------------
if __name__ == '__main__':
    main()
    root.mainloop()
