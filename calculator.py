from tkinter import *

root = Tk()

#Change the title
root.title("Calculator")

#Create Entry widget
userEntry = Entry(root, width=35, borderwidth=5)
userEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add():
	return

#Add Button widgets
btn1 = Button(root, text="1", padx=40, pady=20, command=button_add)
btn2 = Button(root, text="2", padx=40, pady=20, command=button_add)
btn3 = Button(root, text="3", padx=40, pady=20, command=button_add)
btn4 = Button(root, text="4", padx=40, pady=20, command=button_add)
btn5 = Button(root, text="5", padx=40, pady=20, command=button_add)
btn6 = Button(root, text="6", padx=40, pady=20, command=button_add)
btn7 = Button(root, text="7", padx=40, pady=20, command=button_add)
btn8 = Button(root, text="8", padx=40, pady=20, command=button_add)
btn9 = Button(root, text="9", padx=40, pady=20, command=button_add)
btn0 = Button(root, text="0", padx=40, pady=20, command=button_add)

btnAdd = Button(root, text="+", padx=40, pady=20, command=button_add)
btnEqual = Button(root, text="=", padx=91, pady=20, command=button_add)
btnClear = Button(root, text="CLEAR", padx=79, pady=20, command=button_add)



#Place buttons on grid in traditional calculator style: (7,8,9) (4,5,6) (1,2,3) (0)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn0.grid(row=4,column=0)

btnClear.grid(row=4, column=1, columnspan=2)
btnAdd.grid(row=5, column=0)
btnEqual.grid(row=5, column=1, columnspan=2)

root.mainloop()