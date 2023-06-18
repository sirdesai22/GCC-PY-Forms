from tkinter import *
import tkinter as tk
import admission as ad
import enquiry as enq
import marks as mk

def formAdmi():
    ad.run()
def formEnq():
    enq.run()
def formMarks():
    mk.run()
def formFeed():
    pass

root = Tk()
root.geometry('300x250')
root.title('Trial')
root.resizable(False, False)

Button(root, text="Addmission", bd=2, font=30, height=2, command=formAdmi, bg="lightblue").pack(fill=tk.X)
Button(root, text="Enquiry", bd=2, font=30, height=2, command=formEnq, bg="pink").pack(fill=tk.X)
Button(root, text="MarksSheet", bd=2, font=30, height=2, command=formMarks, bg="orange").pack(fill=tk.X)
Button(root, text="Feedback", bd=2, font=30, height=2, command=formFeed, bg="lightgreen").pack(fill=tk.X)


root.mainloop()