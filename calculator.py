# Import necessary components from Tkinter
from tkinter import *
import math
from tkinter import ttk, messagebox
import tkinter
##import tkinter.messagebox

# Initialize the main window for the application
root = Tk()

# Set the title of the window, which appears in the title bar
root.title('Scientific Calculator')

# Configure the background color of the main window to black
root.configure(background='black')

# Prevent the window from being resizable in both width and height
root.resizable(width=False, height=False)

# Define the geometry of the window, i.e., its size and position on the screen
# Format is 'widthxheight+x-offset+y-offset'
root.geometry('480x568+450+90')

# Create a Frame widget, which will act as a container for other widgets like buttons
calc = Frame(root)

# Arrange the frame using the grid geometry manager
# This manager divides the window into a grid for placing widgets
calc.grid()


class Calc():
    def __init__(self):
        # Constructor for Calc class
        # Initializes various attributes used in the calculator operations
        self.total = 0         # Stores the total result of calculations
        self.current = ''      # Stores the current input number or result
        self.input_value = True  # Flag to check if input is being entered
        self.check_sum = False   # Flag to check if a calculation needs to be performed
        self.op = ''            # Stores the operator for calculation
        self.result = False     # Flag to check if the result was just displayed

    def Enter_number(self, num):
        # Method to handle number (and decimal point) input
        self.result = False    # Resets the result flag as new input is being entered
        firstnum = txtDisplay.get()  # Get the current value from the calculator's display
        secondnum = str(num)   # Convert the number input to a string

        if self.input_value:
            # If this is the first number being entered after an operation
            self.current = secondnum
            self.input_value = False
        else:
            # If adding more digits to a number already being entered
            if secondnum == '.':
                # Prevent adding more than one decimal point in a number
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum  # Append the new digit or decimal point

        self.display(self.current)  # Update the display with the new current value

    def sum_of_total(self):
        # Finalizes the total after an operation
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
    # Clears the current content of the calculator's display
        txtDisplay.delete(0, END)

    # Inserts the new value to be displayed at the beginning of the display
        txtDisplay.insert(0, value)


    def valid_function(self):
         # This method checks the operation to perform based on the self.op value
        if self.op == 'add':
            self.total += self.current
        elif self.op == 'sub':
            self.total -= self.current
        elif self.op == 'multi':
            self.total *= self.current
        elif self.op == 'divide':
            self.total /= self.current
        elif self.op == 'mod':
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        #  Sets up the calculator to perform the selected arithmetic operation (like addition, subtraction, etc.) based on the operator passed to it.
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        # Clears the current entry on the calculator, resetting it to zero.
        self.result = False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0
        
    
    # Defining Operations on Scientific calculator
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

# Create an instance of the Calc class to handle the calculator's logic
added_value = Calc()

# Create a text entry widget for displaying calculations and results
txtDisplay = Entry(calc, font=('Arial',20,'bold'),
                   bg='blue', fg='white',
                   bd=30, width=28, justify=RIGHT)

# Position the display at the top of the calculator using grid layout
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
# Initialize the display with '0'
txtDisplay.insert(0, '0')

# Define the sequence of numbers for the number pad buttons
numberpad = '789456123'

# Variable to keep track of the current number button position
i = 0

# Create an empty list to store the button widgets
btn = []

# Loop through rows and columns to place number buttons
for j in range(2, 5):
    for k in range(3):
        # Create a button for each number, set its properties and add it to the btn list
        btn.append(Button(calc, width=6, height=2, bg='blue', fg='white',
                          font=('Arial',20,'bold'), bd=4, text=numberpad[i]))
        # # Increment the position for the next number
        # i += 1
# set buttons in rows & column and separate them with a padding of 1 unit
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]['command'] = lambda x=numberpad[i]: added_value.Enter_number(x)
        i=i+1
# # This section creates buttons for specific functionalities: 'C' for clear entry, 'CE' for clear all entries,
# square root, addition, subtraction, multiplication, division, zero, and decimal point. Each button is configured
# with size, color, font, and bound to respective functions in the Calc class to perform calculator operations.

btnClear = Button(calc, text='C',width=6,height=2,bg='green',font=('Arial',20,'bold'),
                  bd=4, command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text='AC',width=6,height=2,bg='green',font=('Arial',20,'bold'),
                     bd=4, command=added_value.All_Clear_Entry).grid(row=1, column=1, pady=1)

btnsq = Button(calc, text='\u221A',width=6,height=2,bg='green',font=('Arial',20,'bold'),
               bd=4, command=added_value.squared).grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text='+',width=6,height=2,bg='green',font=('Arial',20,'bold'),
                bd=4, command=lambda: added_value.operation('add')).grid(row=1, column=3, pady=1)

btnSub = Button(calc, text='-',width=6,height=2,bg='green',font=('Arial',20,'bold'),
                bd=4, command=lambda: added_value.operation('sub')).grid(row=2, column=3, pady=1)

btnMul = Button(calc, text='x',width=6,height=2,bg='green',font=('Arial',20,'bold'),
                bd=4, command=lambda: added_value.operation('multi')).grid(row=3, column=3, pady=1)

btnDiv = Button(calc, text='/',width=6,height=2,bg='green',font=('Arial',20,'bold'),
                bd=4, command=lambda: added_value.operation('divide')).grid(row=4, column=3, pady=1)

btnZero = Button(calc, text='0',width=6,height=2,bg='red',fg='white',font=('Arial',20,'bold'),
                bd=4, command=lambda: added_value.Enter_number(0)).grid(row=5, column=0, pady=1)

btnDot = Button(calc, text='.',width=6,height=2,bg='green',font=('Arial',20,'bold'),
                bd=4, command=lambda: added_value.Enter_number('.')).grid(row=5, column=1, pady=1)

# Creation of two additional buttons: The '±' button, represented by chr(177), is used to change the sign of the 
# current number, and the '=' button for executing the calculation and displaying the total. Each button is styled 
# and linked to respective functions in the Calc class to handle sign change and final calculation.

btnPM = Button(calc, text=chr(177),width=6,height=2,bg='green',font=('Arial',20,'bold'),
               bd=4, command=added_value.mathPM).grid(row=5, column=2, pady=1)

btnEquals = Button(calc, text='=',width=6,height=2,bg='green',font=('Arial',20,'bold'),
                   bd=4, command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

# Creation of scientific function buttons in multiple rows: 
# Row 1 includes buttons for trigonometric functions (sin, cos, tan).
# Row 2 includes buttons for hyperbolic functions (sinh, cosh, tanh).
# Row 3 includes buttons for mathematical constants and functions (pi, exp, mod).
# Row 4 includes buttons for logarithmic functions and Euler's number (e, log, log10).
# Row 5 includes buttons for degree conversion and inverse hyperbolic functions (deg, acosh, asinh).
# Additionally, a label 'Scientific Calculator' is created and displayed at the top of these buttons.
# Each button is styled consistently and assigned functions to perform specific scientific calculations.

#ROW 1:
btnsin = Button(calc, text='sin',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                bd=4, command=added_value.sin).grid(row=1, column=4, pady=1)

btncos = Button(calc, text='Cos',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                bd=4, command=added_value.cos).grid(row=1, column=5, pady=1)

btntan = Button(calc, text='tan',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                bd=4, command=added_value.tan).grid(row=1, column=6, pady=1)


#ROW 2:

btnsinh=Button(calc, text='sinh',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
               bd=4, command=added_value.sinh).grid(row=2, column=4, pady=1)

btncosh = Button(calc, text='Cosh',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                 bd=4, command=added_value.cosh).grid(row=2, column=5, pady=1)

btntanh = Button(calc, text='tanh',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                 bd=4, command=added_value.tanh).grid(row=2, column=6, pady=1)


#ROW 3:

btnPi = Button(calc, text='π',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                bd=4, command=added_value.pi).grid(row=3, column=4, pady=1)

btnexp = Button(calc, text='exp',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                bd=4, command=added_value.exp).grid(row=3, column=5, pady=1)

btnmod = Button(calc, text='mod',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                bd=4, command=lambda: added_value.operation('mod')).grid(row=3, column=6, pady=1)


#ROW 4:

btne = Button(calc, text='e',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
              bd=4, command=added_value.e).grid(row=4, column=4, pady=1)

btnlog = Button(calc, text='log',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                bd=4, command=added_value.log).grid(row=4, column=5, pady=1)

btnlog10 = Button(calc, text='log10',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                  bd=4, command=added_value.log10).grid(row=4, column=6, pady=1)



#ROW 5:

btndeg = Button(calc, text='deg',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                bd=4, command=added_value.degrees).grid(row=5, column=4, pady=1)

btnacosh = Button(calc, text='acosh',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                  bd=4, command=added_value.acosh).grid(row=5, column=5, pady=1)

btnasinh = Button(calc, text='asinh',width=6,height=2,bg='orange',fg='white',font=('Arial',20,'bold'),
                  bd=4, command=added_value.asinh).grid(row=5, column=6, pady=1)

lblDisplay = Label(calc, text='Scientific Calculator',font=('Georgia',22,'bold'),
                   bg='black',fg='white',justify=CENTER)

lblDisplay.grid(row=0, column=4, columnspan=4)

# This function is used to prompt the user for confirmation before exiting the application.
# It uses the askyesno function from tkinter.messagebox to display a dialog box with the message
def iExit():
    iExit = tkinter.messagbox.askyesno('Scientific Calculator','Do you want to exit ?')
    
    if iExit>0:
        root.destroy()
        return

# These functions are used to switch the calculator's layout between Scientific and Standard modes.
# In both functions, the window's resizable property is set to False to prevent resizing, maintaining a fixed layout.
 
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("830x568+0+0")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

# MENUBAR 1: Standard Calculator
menubar.add_command(label='Standard', command=Standard)

# MENUBAR 2: Scientific Calculator
menubar.add_command(label='Scientific', command=Scientific)

root.config(menu=menubar)
root.mainloop()


  
