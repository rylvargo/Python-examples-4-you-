#--------------------------------------------------------------------------------------------------------------|
# TKINTER MESSAGEBOX IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: No installation needed with standard desktop Python.
# Tkinter is included with many Python installations.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Hello", "Welcome!")

root.destroy()


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Popup Example")
root.geometry("300x200")

# Create popup function
def show_popup():
    messagebox.showinfo("Game", "Welcome to the game!")

# Create button
button = tk.Button(
    root,
    text="Show Message",
    command=show_popup
)
button.pack(pady=50)

# Run window
root.mainloop()