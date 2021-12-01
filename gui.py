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

    frameLog = Frame(root)
    frameLog.grid(row=0, column=2) 

    Label(frameLog, text='Add new Patient').grid(row=0)





    
# ---------------------------------Keep At End---------------------------
if __name__ == '__main__':
    main()
    root.mainloop()
