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

    def numberEnter(self, num):
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
            self.Logic_valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
    # Clears the current content of the calculator's display
        txtDisplay.delete(0, END)

    # Inserts the new value to be displayed at the beginning of the display
        txtDisplay.insert(0, value)


    def Logic_valid_function(self):
         # This method checks the operation to perform based on the self.op value
        if self.op == 'addition':
            self.total += self.current
        elif self.op == 'subtraction':
            self.total -= self.current
        elif self.op == 'multiplication':
            self.total *= self.current
        elif self.op == 'division':
            self.total /= self.current
        elif self.op == 'Modulus':
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)


 

    def operation(self, op):
        #  Sets up the calculator to perform the selected arithmetic operation (like addition, subtraction, etc.) based on the operator passed to it.
        self.current = float(self.current)
        if self.check_sum:
            self.Logic_valid_function()
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

        
    
##############################################################################################
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


root.mainloop()


  
