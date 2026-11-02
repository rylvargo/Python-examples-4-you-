#--------------------------------------------------------------------------------------------------------------|
# PYSIMPLEGUI IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Check the current official PySimpleGUI installation instructions.
# Installation availability and terms can change.

import PySimpleGUI as sg

layout = [[sg.Text("Hello World!")]]

window = sg.Window("My App", layout)

event, values = window.read()

window.close()


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import PySimpleGUI as sg

# Create layout
layout = [
    [sg.Text("Welcome to my app!")],
    [sg.Input(key="-NAME-")],
    [sg.Button("Submit"), sg.Button("Exit")]
]

# Create window
window = sg.Window("My App", layout)

# Handle buttons
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Submit":
        sg.popup("Hello", values["-NAME-"])

window.close()