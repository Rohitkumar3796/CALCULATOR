from tkinter import *
root=Tk()
# THIS FUNCTION FOR PRESS THE NUMBER
def press_number(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# THIS FUNCTION FOR CLEAR THE SCREEN
def bt_clear():
    global expression
    expression = ""
    input_text.set("")

# THIS FUNCTION FOR TOTAL
def bt_equal():
    global expression
    result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""


expression = ""

# 'StringVar()' :It is used to get the input from user of input field
input_text = StringVar()

# ENTRY BOX
E1=Entry(root,borderwidth=10,font=("arial",8,'bold'),  textvariable=input_text,justify=RIGHT)
E1.grid(row=0,column=0,columnspan=4,sticky=NE)
# ________________________________________________________________________________________________________________
# _______________________BUTTONS___________________________________________________________________________________
B9=Button(root,text="7",height=2, width=5,command=lambda:press_number(7)).grid(sticky=E,columnspan=1,row=2,column=0)
B8=Button(root,text="8",height=2, width=5,command=lambda:press_number(8)).grid(row=2,column=1)
B7=Button(root,text="9",height=2, width=5,command=lambda:press_number(9)).grid(row=2,column=2)

B6=Button(root,text="4",height=2, width=5,command=lambda:press_number(4)).grid(sticky=E,columnspan=1,row=3,column=0)
B5=Button(root,text="5",height=2, width=5,command=lambda:press_number(5)).grid(row=3,column=1)
B4=Button(root,text="6",height=2, width=5,command=lambda:press_number(6)).grid(row=3,column=2)

B3=Button(root,text="1",height=2, width=5,command=lambda:press_number(1)).grid(sticky=E,columnspan=1,row=4,column=0)
B2=Button(root,text="2",height=2, width=5,command=lambda:press_number(2)).grid(row=4,column=1)
B1=Button(root,text="3",height=2, width=5,command=lambda:press_number(3)).grid(row=4,column=2)

PLUS=Button(root,text="+",height=2, width=5,command=lambda:press_number("+")).grid(sticky=E,columnspan=1,row=5,column=0)
ZERO=Button(root,text="0",height=2, width=5,command=lambda:press_number(0)).grid(row=5,column=1)
MULT=Button(root,text="*",height=2, width=5,command=lambda:press_number("*")).grid(row=5,column=2)

DIVISION=Button(root,text="/",height=2, width=5,command= lambda :press_number("/")).grid(sticky=E,columnspan=1,row=6,column=0)
MINUS=Button(root,text="-",height=2, width=5, command=lambda :press_number("-")).grid(row=6,column=1)
EQUAL=Button(root,text="=",height=2, width=5,command=lambda:bt_equal()).grid(row=6,column=2)

DOT=Button(root,text=".",height=2, width=5,command=lambda:press_number(".")).grid(row=6,column=1)
CLEAR=Button(root,text="CLEAR",height=2,width=19,command=lambda:bt_clear()).grid(row=7, column=0, columnspan=3, padx=1, pady=1)
# ________________________________________________________________________________________________________________
# _______________________BUTTONS END___________________________________________________________________________________

root.title("CALCULATOR")
root.geometry("145x285")
root.mainloop()