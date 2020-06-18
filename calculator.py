from tkinter import *

root = Tk()

#Change the title
root.title("LaCroixSlayer Calculator")


#Create Entry widget
userEntry = Entry(root, width=35, borderwidth=5)
userEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Global Variables



def buttonClick(number):
	currentNum = userEntry.get()
	userEntry.delete(0, END)
	#Insert lambda number into the Entry widget
	#We want to concatenate two values and NOT add so we use str().
	userEntry.insert(0, str(currentNum) + str(number))
	return

def buttonClear():
	userEntry.delete(0,END)

def buttonAdd():
	userNum = userEntry.get()
	global firstNum
	global operator
	operator = "+"
	firstNum = int(userNum)
	userEntry.delete(0,END)

def buttonSubtract():
	userNum = userEntry.get()
	global firstNum
	global operator
	operator = "-"
	firstNum = int(userNum)
	userEntry.delete(0,END)

def buttonDivide():
	userNum = userEntry.get()
	global firstNum
	global operator
	operator = "/"
	firstNum = int(userNum)
	userEntry.delete(0,END)

def buttonMultiply():
	userNum = userEntry.get()
	global firstNum
	global operator
	operator = "*"
	firstNum = int(userNum)
	userEntry.delete(0,END)

def buttonEqual():
	secondNum = userEntry.get()
	userEntry.delete(0,END)

	if operand == "+":
		userEntry.insert(0, firstNum + int(secondNum))

	if operand == "-":
		userEntry.insert(0, firstNum - int(secondNum))

	if operand == "*":
		userEntry.insert(0, firstNum * int(secondNum))
		
	if operand == "/":
		userEntry.insert(0, firstNum / int(secondNum))	

#Add Button widgets
btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))

btnAdd = Button(root, text="+", padx=40, pady=20, command=buttonAdd)
btnEqual = Button(root, text="=", padx=99, pady=20, command=buttonEqual)
btnClear = Button(root, text="CLEAR", padx=83, pady=20, command=buttonClear)

btnSubtract = Button(root, text="-", padx=41, pady=20, command=buttonSubtract)
btnMultiply = Button(root, text="*", padx=42, pady=20, command=buttonMultiply)
btnDivide = Button(root, text="/", padx=42, pady=20, command=buttonDivide)



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

btnSubtract.grid(row=6, column=0)
btnMultiply.grid(row=6, column=1)
btnDivide.grid(row=6, column=2)



root.mainloop()