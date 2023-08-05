import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
def call():
    a = mb.askquestion('Exit Application','Do you really want to exit')
    if a == 'yes' :
        root.destroy()
    else :
        mb.showinfo('Return', 'Returning to main application')
def add():
 num1 = float(num1_entry.get())
 num2 = float(num2_entry.get())
 result = str(num1 + num2)
 result_label.config(text="Result: "+ result)
def substract():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = str(num1 - num2)
    result_label.config(text="Result: "+ result)
def multiply():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = str(num1 * num2)
    result_label.config(text="Result: "+ result)
def divide():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result =str( num1 / num2)
    result_label.config(text="Result: "+ result)
root = tk.Tk()
root.title("BASIC CALCULATOR")
num1_label = tk.Label(root, text="Number 1:")
num1_entry = tk.Entry(root)
num2_label = tk.Label(root, text="Number 2:")
num2_entry = tk.Entry(root)
add1 = tk.Button(root, text="Add", command=add)
add2 = tk.Button(root, text="Substract", command=substract)
add3 = tk.Button(root, text="Multiply", command=multiply)
add4 = tk.Button(root, text="Divide", command=divide)
add5 = tk.Button(root, text="Quit", command=call)
result_label = tk.Label(root, text="")
num1_label.grid(row=0, column=0, sticky="e")
num1_entry.grid(row=0, column=1)
num2_label.grid(row=1, column=0, sticky="e")
num2_entry.grid(row=1, column=1)
add1.grid(row=2, column=2, columnspan=2, pady=10)
add2.grid(row=2, column=4, columnspan=2, pady=10)
add3.grid(row=2, column=10, columnspan=2, pady=10)
add4.grid(row=2, column=15, columnspan=2, pady=10)
add5.grid(row=2, column=20, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()