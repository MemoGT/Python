# Este programa en python pide en dos textbox dos numeros y los suma con el boton

import tkinter as tk

def add_numbers():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    sum = num1 + num2
    result_label.config(text=f"La suma de  {num1} y {num2} es: {sum}")

root = tk.Tk()
num1_label = tk.Label(root, text="Ingresar numero 1:")
num1_label.pack()
num1_entry = tk.Entry(root)
num1_entry.pack()
num2_label = tk.Label(root, text="Ingresar numero 2:")
num2_label.pack()
num2_entry = tk.Entry(root)
num2_entry.pack()
add_button = tk.Button(root, text="Sumar numero", command=add_numbers)
add_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()


"""
This script is a simple Python program that uses the tkinter library to create a GUI (graphical user interface) that allows the user to add two numbers. Here is a breakdown of what the script does, line by line:

import tkinter as tk: This line imports the tkinter library, which is used for creating GUI applications in Python. The as tk part allows the library to be referred to as just tk in the rest of the script.

def add_numbers():: This line defines a function called add_numbers, which will be called when the user clicks the "Add" button.

num1 = float(num1_entry.get()): Inside the add_numbers function, this line retrieves the value from the first textbox (num1_entry) and converts it to a floating-point number, which is assigned to the variable num1.

num2 = float(num2_entry.get()): This line is similar to the previous line, but it retrieves the value from the second textbox (num2_entry) and assigns it to the variable num2.

sum = num1 + num2: This line performs the addition of the two numbers and assigns the result to the variable sum.

result_label.config(text=f"The sum of {num1} and {num2} is {sum}"): This line sets the text of the result_label to a string that displays the sum of the two numbers.

root = tk.Tk(): This line creates the main window for the GUI application.

num1_label = tk.Label(root, text="Enter a number:"): This line creates a label widget with the text "Enter a number:" and associates it with the main window (root).

num1_label.pack(): This line packs the label widget so that it is displayed in the main window.

num1_entry = tk.Entry(root): This line creates a textbox widget and associates it with the main window.

num1_entry.pack(): This line packs the textbox widget so that it is displayed in the main window.

num2_label = tk.Label(root, text="Enter another number:"): This line creates a label widget with the text "Enter another number:" and associates it with the main window.

num2_label.pack(): This line packs the label widget so that it is displayed in the main window.

num2_entry = tk.Entry(root): This line creates a textbox widget and associates it with the main window.

num2_entry.pack(): This line packs the textbox widget so that it is displayed in the main window.

add_button = tk.Button(root, text="Add", command=add_numbers): This line creates a button widget with the label "Add" and associates it with the main window. The command=add_numbers part specifies that the add_numbers function should be called when the button is clicked.

add_button.pack()
"""


