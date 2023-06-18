from tkinter import *
def run():
    # from tkinter.ttk import Combobox
    # from tkinter import messagebox
    #from tkcalendar import Calendar

    #Functions
    def clear():
        name.delete("0", "end")
        dob.delete("0", "end")
        contact.delete("0", "end")
        email.delete("0", "end")

    root = Tk()
    root.title("Admission Form")
    root.geometry('600x400')
    root.resizable(False, False)
    root.configure(bg="#dff2f9")

    #icon
    # icon_image = PhotoImage(file="abc.png")
    # root.iconphoto(False, icon_image)


    #Heading
    Label(root, text="Admission Form", font="arial 30", bg="#dff2f9", fg="#000000").place(x=150, y=20)

    #Label
    Label(root, text="Full Name:", font=20, bg="#dff2f9", fg="#000000").place(x= 10, y=100)
    Label(root, text="DOB:", font=20, bg="#dff2f9", fg="#000000").place(x= 10, y=150)
    Label(root, text="Gender:", font=20, bg="#dff2f9", fg="#000000").place(x= 280, y=150)
    Label(root, text="Contact:", font=20, bg="#dff2f9", fg="#000000").place(x= 10, y=200)
    Label(root, text="Email:", font=20, bg="#dff2f9", fg="#000000").place(x= 10, y=250)

    #Entry
    name = Entry(root, width=40, font=20)
    dob = Entry(root, width=15, font=20)
    Radiobutton(root, text="Male", font=20, bg="#dff2f9", fg="#000000", value=1).place(x=380, y=147)  
    Radiobutton(root, text="Female", font=20, bg="#dff2f9", fg="#000000", value=2).place(x=480, y=147)  
    contact = Entry(root, width=20, font=20)
    email = Entry(root, width=30, font=20)

    #Entry Place
    name.place(x=130, y=100)
    dob.place(x=90, y=150)
    contact.place(x=100, y=200)
    email.place(x=100, y=250)

    #Buttons
    Button(root, text="Submit", bd=2, font=20, command=clear).place(x=150, y=300)
    Button(root, text="Clear", bd=2, font=20, command=clear).place(x=350, y=300)

    root.mainloop()