from tkinter import *

root = Tk()

#Change the title
root.title("Calculator")

#Create Entry widget
userEntry = Entry(root, width=35, borderwidth=5)
userEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()