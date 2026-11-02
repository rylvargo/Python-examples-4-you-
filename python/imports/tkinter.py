
import tkinter as tk            #this make it so when you call tkinter you only have to put tk EX : tk.button

BG = "#3b2416"                  # Sets the background color to brown

root = tk.Tk()                  # Creates the main window
root.title("Cookie Clicker")    # Sets the window title
root.geometry("800x850")        # Sets the window size (800 wide, 850 tall)
root.resizable(False, False)    # Prevents the window from being resized
root.configure(bg=BG)           # Changes the window background color

root.mainloop()                 # Keeps the window running until closed

