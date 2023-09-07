# Python program to create a simple GUI
# calculator using Tkinter
 
# import everything from tkinter module
from tkinter import *
import tkinter.font as font
 
# globally declare the expression variable
expression = ""
 
 
# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
 
 
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

   # p1=PhotoImage(file="icon.png")
   # gui.iconphoto(False, p1)
    
    # set the background colour of GUI window
    gui.configure(background="#343434")
 
    # set the title of GUI window
    gui.title("CALCULATOR")
 
    # set the configuration of GUI window
    gui.geometry("360x550")
    
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)
    f = font.Font(size=18)
    expression_field['font'] = f
    
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=20, ipadx=30,ipady=20)

    gui.columnconfigure(0, pad=3)
    gui.columnconfigure(1, pad=3)
    gui.columnconfigure(2, pad=3)
    gui.columnconfigure(3, pad=3)

    gui.rowconfigure(0, pad=150)
    gui.rowconfigure(1, pad=8)
    gui.rowconfigure(2, pad=8)
    gui.rowconfigure(3, pad=8)
    gui.rowconfigure(4, pad=8)
    gui.rowconfigure(5, pad=8)
    gui.rowconfigure(6, pad=8)
 

 
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='#707070',
                    command=lambda: press(1), height=3, width=11)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black',bg='#707070',
                    command=lambda: press(2), height=3, width=11)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='#707070',
                    command=lambda: press(3), height=3, width=11)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black',bg='#707070',
                    command=lambda: press(4), height=3, width=11)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='#707070',
                    command=lambda: press(5), height=3, width=11)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='#707070',
                    command=lambda: press(6), height=3, width=11)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='#707070',
                    command=lambda: press(7), height=3, width=11)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='#707070',
                    command=lambda: press(8), height=3, width=11)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='#707070',
                    command=lambda: press(9), height=3, width=11)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black',bg='#707070',
                    command=lambda: press(0), height=3, width=11)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='#707070',
                command=lambda: press("+"), height=3, width=11)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='#707070',
                command=lambda: press("-"), height=3, width=11)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='#707070',
                    command=lambda: press("*"), height=3, width=11)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black',bg='#707070',
                    command=lambda: press("/"), height=3, width=11)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='#707070',
                command=equalpress, height=3, width=11)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black',bg='#707070',
                command=clear, height=3, width=11)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='#707070',
                    command=lambda: press('.'), height=3, width=11)
    Decimal.grid(row=6, column=0)
    
    # start the GUI
    gui.mainloop()
