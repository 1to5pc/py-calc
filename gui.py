import tkinter as tk
from tkinter import *

# Global variable to store the expression
expression = ""

# Function to handle button press events
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the expression and display the result
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" Error ")
        expression = ""
        #TODO clear error message after approx 1s

# Function to clear the expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Main function
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()
    gui.title("Python GUI Calculator")

    # Set the configuration of GUI window
    gui.geometry("465x440")
    gui.configure(background="black")

    # Create a StringVar to store the expression
    equation = StringVar()

    # Create an Entry widget to display the expression
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 18), bd=10, insertwidth=3, width=14, bg="white", fg="black", justify="right")
    expression_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    expression_field.configure(state= 'readonly')


    # Define button dimensions and styles
    button_style = {"fg": "white", "bg": "black", "font": ("Arial", 14), "height": 2, "width": 7, "bd": 5}
    button_style2 = {"fg": "white", "bg": "black", "font": ("Arial", 14), "height": 2, "width": 14, "bd": 5}

    # Create buttons for digits and operators
    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        (".", 4, 2), ("+", 4, 3)
    ]

    # Create buttons and attach press function
    for (text, row, col) in buttons:
        btn = Button(gui, text=text, command=lambda t=text: press(t), **button_style)
        btn.grid(row=row, column=col, padx=5, pady=5)

    #Isolate button for '0' ##TODO: change button width to cover width of 2 buttons
    btn = Button(gui, text=0, command=lambda t=0: press(t), **button_style2)
    btn.grid(row=4, column=0, padx=5, pady=5)

    # Create Clear button
    clear_button = Button(gui, text="Clear", command=clear, **button_style)
    clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    # Create Equal button
    equal_button = Button(gui, text="=", command=equalpress, **button_style)
    equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

    # Start the GUI event loop
    gui.mainloop()
