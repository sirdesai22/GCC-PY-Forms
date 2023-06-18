import tkinter as tk
from tkinter import messagebox

def submit_enquiry():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    course = entry_course.get()
    message = entry_message.get("1.0", tk.END)

    # Validate the inputs (you can add your own valid logic here)

    # Display a confirmation message box
    messagebox.showinfo("Enquiry Submitted", "Thank you for your enquiry!")

    # Save the data to a file or database
    save_enquiry(name, email, phone, course, message)

def save_enquiry(name, email, phone, course, message):
    # Here we can implement the code to save the enquiry data
    # to a file or database
    print("\nEnquiry Details:")
    print("Name:", name)
    print("Email:", email)
    print("Phone number:", phone)
    print("Course of interest:", course)
    print("Message:", message)

# Create the main window
window = tk.Tk()
window.geometry('800x400')
window.title("College Enquiry Form")
window.configure(bg="lavender")
label_name = tk.Label(window, text="COLLEGE ENQUIRY FORM", font='ALGERIAN 30',bg="lavender")
label_name.pack()
# Create labels and entry fields
label_name = tk.Label(window, text="Name:",bg="lavender")
label_name.place(x=10,y=60)
entry_name = tk.Entry(window)
entry_name.place(x=80,y=60)

label_email = tk.Label(window, text="Email:",bg="lavender")
label_email.place(x=10,y=100)
entry_email = tk.Entry(window)
entry_email.place(x=80,y=100)

label_phone = tk.Label(window, text="Phone \nnumber:",bg="lavender")
label_phone.place(x=10,y=135)
entry_phone = tk.Entry(window)
entry_phone.place(x=80,y=150)

label_course = tk.Label(window, text="Course \n of interest:",bg="lavender")
label_course.place(x=10,y=180)
entry_course = tk.Entry(window)
entry_course.place(x=80,y=195)

label_message = tk.Label(window, text="Message:",bg="lavender")
label_message.place(x=10,y=240)
entry_message = tk.Text(window, height=5)
entry_message.place(x=80,y=240)

# Create a submit button
submit_button = tk.Button(window, text="Submit", command=submit_enquiry,font='arial 15')
submit_button.place(x=640,y=350)


window.mainloop()