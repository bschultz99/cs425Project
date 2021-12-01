from tkinter import*  

# Create Root Window
root = Tk()

login = False


def main():
    
    # ----------------login screen-------------------
    if(not login):
        # Open window with dimension AxA
        root.geometry('250x100')

        frameLog = Frame(root)
        frameLog.grid(row=0, column=2) 

        Label(frameLog, text='Login').grid(row=0)
        Label(root, text='Username').grid(row=1)
        Label(root, text='Password').grid(row=2)

        e1 = Entry(root)
        e2 = Entry(root)
        e1.grid(row=1, column=2)
        e2.grid(row=2, column=2)

        loginButton = Button(root, text='Login')
        loginButton.grid(row=3, column=2)
        

# Create login window

# creates new window
def create_window():
    window = Toplevel(root)

# ---------------------------------Keep At End---------------------------
if __name__ == '__main__':
    main()
    root.mainloop()
