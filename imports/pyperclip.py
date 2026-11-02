#Requires installation : pip install pyperclip
import pyperclip  # Imports the clipboard library

pyperclip.copy("Hello!")  # Copies text
print(pyperclip.paste())  # Pastes copied text


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import pyperclip

# Ask user for text
text = input("Enter something to copy: ")

# Copy text to clipboard
pyperclip.copy(text)

print("Text copied!")

# Read clipboard
copied_text = pyperclip.paste()

print("Clipboard contains:", copied_text)