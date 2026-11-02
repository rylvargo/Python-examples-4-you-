
import tkinter as tk            #this make it so when you call tkinter you only have to put tk EX : tk.button

BG = "#3b2416"                  # Sets the background color to brown

root = tk.Tk()                  # Creates the main window
root.title("Cookie Clicker")    # Sets the window title
root.geometry("800x850")        # Sets the window size (800 wide, 850 tall)
root.resizable(False, False)    # Prevents the window from being resized
root.configure(bg=BG)           # Changes the window background color

root.mainloop()                 # Keeps the window running until closed


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import tkinter as tk  # Import tkinter

root = tk.Tk()  # Create window

root.title("My First Window")  # Set window title
root.geometry("400x300")  # Set window size
root.configure(bg="lightblue")  # Set background color

# Create a text label
label = tk.Label(root, text="Hello World!", font=("Arial", 20))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me!")
button.pack()

root.mainloop()  # Keep window open


