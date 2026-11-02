#--------------------------------------------------------------------------------------------------------------|
# PYGLET IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Open your terminal and type:
# pip install pyglet

import pyglet  # Imports the pyglet library

window = pyglet.window.Window()  # Creates a window

pyglet.app.run()  # Starts the window


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import pyglet

# Create a window
window = pyglet.window.Window(600, 400, caption="My Pyglet App")

# Create text
label = pyglet.text.Label(
    "Hello World!",
    font_size=30,
    x=300,
    y=200,
    anchor_x="center",
    anchor_y="center"
)

# Draw text
@window.event
def on_draw():
    window.clear()
    label.draw()

# Start program
pyglet.app.run()