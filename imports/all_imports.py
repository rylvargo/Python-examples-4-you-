#==============================================================================================================|
# PYTHON SUPER APP
#==============================================================================================================|

# INSTALLATION:
# Open your terminal and run:
# pip install pyglet openpyxl requests opencv-python sounddevice pgzero PySimpleGUI
#
# Tkinter, socket, pathlib, subprocess, and sys are included with Python.
#
# WHAT THIS PROGRAM DOES:
# Creates a window with buttons that demonstrate different Python libraries.
#
#==============================================================================================================|


import tkinter as tk
from tkinter import messagebox

import socket
import pathlib
import subprocess
import sys
import shutil


#--------------------------------------------------------------------------------------------------------------|
# WINDOW SETTINGS
#--------------------------------------------------------------------------------------------------------------|

root = tk.Tk()

root.title("Python Super App")
root.geometry("600x750")
root.configure(bg="#202030")
root.resizable(False, False)

# Create a folder for saved files
folder = pathlib.Path("SuperAppFiles")
folder.mkdir(exist_ok=True)


#--------------------------------------------------------------------------------------------------------------|
# TITLE
#--------------------------------------------------------------------------------------------------------------|

title = tk.Label(
    root,
    text="PYTHON SUPER APP",
    font=("Arial", 25, "bold"),
    bg="#202030",
    fg="white"
)

title.pack(pady=20)


description = tk.Label(
    root,
    text="Explore 10 different Python libraries!",
    font=("Arial", 12),
    bg="#202030",
    fg="lightgray"
)

description.pack(pady=5)


#--------------------------------------------------------------------------------------------------------------|
# 1. PYGLET
#--------------------------------------------------------------------------------------------------------------|

def open_pyglet():

    try:
        import pyglet

        window = pyglet.window.Window(
            500, 300,
            caption="Pyglet Example"
        )

        label = pyglet.text.Label(
            "Hello from Pyglet!",
            font_size=25,
            x=250,
            y=150,
            anchor_x="center",
            anchor_y="center"
        )

        @window.event
        def on_draw():
            window.clear()
            label.draw()

        pyglet.app.run()

    except ImportError:
        messagebox.showerror("Error", "Install pyglet first!")


#--------------------------------------------------------------------------------------------------------------|
# 2. OPENPYXL
#--------------------------------------------------------------------------------------------------------------|

def save_excel():

    try:
        import openpyxl

        workbook = openpyxl.Workbook()
        sheet = workbook.active

        sheet["A1"] = "Player"
        sheet["B1"] = "Score"

        sheet.append(["Player1", 500])
        sheet.append(["Player2", 1000])
        sheet.append(["Player3", 1500])

        workbook.save(folder / "scores.xlsx")

        messagebox.showinfo(
            "Excel",
            "Scores saved to SuperAppFiles!"
        )

    except ImportError:
        messagebox.showerror("Error", "Install openpyxl first!")


#--------------------------------------------------------------------------------------------------------------|
# 3. REQUESTS
#--------------------------------------------------------------------------------------------------------------|

def website_request():

    try:
        import requests

        response = requests.get(
            "https://example.com",
            timeout=10
        )

        messagebox.showinfo(
            "Website",
            f"Website status: {response.status_code}"
        )

    except Exception as error:
        messagebox.showerror("Website Error", str(error))


#--------------------------------------------------------------------------------------------------------------|
# 4. SOCKET
#--------------------------------------------------------------------------------------------------------------|

def computer_info():

    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except OSError:
        ip = "Unavailable"

    messagebox.showinfo(
        "Computer Information",
        f"Computer: {hostname}\nIP Address: {ip}"
    )


#--------------------------------------------------------------------------------------------------------------|
# 5. TKINTER MESSAGEBOX
#--------------------------------------------------------------------------------------------------------------|

def popup():

    messagebox.showinfo(
        "Python Super App",
        "Hello! This is a popup made with Tkinter!"
    )


#--------------------------------------------------------------------------------------------------------------|
# 6. OPENCV
#--------------------------------------------------------------------------------------------------------------|

def create_image():

    try:
        import cv2
        import numpy as np

        # Create a blank image
        image = np.zeros((400, 400, 3), dtype=np.uint8)

        # Create a blue background
        image[:] = (255, 100, 0)

        # Draw a green rectangle
        cv2.rectangle(
            image,
            (50, 50),
            (350, 350),
            (0, 255, 0),
            -1
        )

        # Save image
        path = folder / "opencv_image.png"

        cv2.imwrite(str(path), image)

        messagebox.showinfo(
            "OpenCV",
            f"Image created!\n{path}"
        )

    except ImportError:
        messagebox.showerror("Error", "Install opencv-python and numpy!")


#--------------------------------------------------------------------------------------------------------------|
# 7. PYSIMPLEGUI
#--------------------------------------------------------------------------------------------------------------|

def open_simplegui():

    try:
        import PySimpleGUI as sg

        layout = [
            [sg.Text("Hello from PySimpleGUI!")],
            [sg.Button("Click Me"), sg.Button("Exit")]
        ]

        window = sg.Window("Simple GUI", layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Exit"):
                break

            if event == "Click Me":
                sg.popup("You clicked the button!")

        window.close()

    except ImportError:
        messagebox.showerror(
            "Error",
            "Install PySimpleGUI using its current official instructions."
        )
    except Exception as error:
        messagebox.showerror("PySimpleGUI Error", str(error))


#--------------------------------------------------------------------------------------------------------------|
# 8. SOUNDDEVICE
#--------------------------------------------------------------------------------------------------------------|

def record_audio():

    try:
        import sounddevice as sd

        messagebox.showinfo(
            "Recording",
            "Recording will begin for 3 seconds."
        )

        recording = sd.rec(
            int(3 * 44100),
            samplerate=44100,
            channels=1
        )

        sd.wait()

        sd.play(recording, 44100)
        sd.wait()

        messagebox.showinfo(
            "Audio",
            "Recording finished and played!"
        )

    except Exception as error:
        messagebox.showerror("Audio Error", str(error))


#--------------------------------------------------------------------------------------------------------------|
# 9. PYGAME ZERO
#--------------------------------------------------------------------------------------------------------------|

def open_pygame_zero():

    # Create a separate game file
    game_code = '''
import pgzrun

WIDTH = 600
HEIGHT = 400

player_x = 300
player_y = 200

def draw():
    screen.fill("lightblue")
    screen.draw.filled_circle((player_x, player_y), 30, "red")
    screen.draw.text("Use arrow keys to move!", (180, 30))

def update():
    global player_x, player_y

    if keyboard.left:
        player_x -= 3
    if keyboard.right:
        player_x += 3
    if keyboard.up:
        player_y -= 3
    if keyboard.down:
        player_y += 3

pgzrun.go()
'''

    game_file = folder / "my_game.py"
    game_file.write_text(game_code)

    runner = shutil.which("pgzrun")

    if runner:
        subprocess.Popen([runner, str(game_file)])
        messagebox.showinfo("Game", "Game launched!")
    else:
        messagebox.showerror(
            "Error",
            "Could not find pgzrun. Install pgzero and check your PATH."
        )


#--------------------------------------------------------------------------------------------------------------|
# 10. PATHLIB
#--------------------------------------------------------------------------------------------------------------|

def create_file():

    # Create a folder
    new_folder = folder / "PlayerData"
    new_folder.mkdir(exist_ok=True)

    # Create a save file
    save_file = new_folder / "player.txt"

    # Write information
    save_file.write_text(
        "Player: Player1\nScore: 500\nLevel: 5"
    )

    # Read information
    data = save_file.read_text()

    messagebox.showinfo(
        "Player Save",
        data
    )


#--------------------------------------------------------------------------------------------------------------|
# BUTTON CREATION
#--------------------------------------------------------------------------------------------------------------|

def make_button(text, command):

    button = tk.Button(
        root,
        text=text,
        font=("Arial", 12, "bold"),
        width=30,
        height=2,
        bg="#444466",
        fg="white",
        activebackground="#666699",
        activeforeground="white",
        command=command
    )

    button.pack(pady=5)


#--------------------------------------------------------------------------------------------------------------|
# APP BUTTONS
#--------------------------------------------------------------------------------------------------------------|

make_button("1. Open Pyglet Window", open_pyglet)

make_button("2. Save Excel Scores", save_excel)

make_button("3. Connect to Website", website_request)

make_button("4. Computer Information", computer_info)

make_button("5. Show Popup", popup)

make_button("6. Create OpenCV Image", create_image)

make_button("7. Open PySimpleGUI", open_simplegui)

make_button("8. Record Audio", record_audio)

make_button("9. Start Pygame Zero Game", open_pygame_zero)

make_button("10. Create Player Save", create_file)


#--------------------------------------------------------------------------------------------------------------|
# EXIT BUTTON
#--------------------------------------------------------------------------------------------------------------|

exit_button = tk.Button(
    root,
    text="EXIT APP",
    font=("Arial", 14, "bold"),
    bg="#aa3333",
    fg="white",
    width=20,
    command=root.destroy
)

exit_button.pack(pady=20)


#--------------------------------------------------------------------------------------------------------------|
# START PROGRAM
#--------------------------------------------------------------------------------------------------------------|

root.mainloop()