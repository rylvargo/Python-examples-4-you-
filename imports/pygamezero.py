#--------------------------------------------------------------------------------------------------------------|
# PYGAME ZERO IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Open your terminal and type:
# pip install pgzero

import pgzrun  # Imports Pygame Zero

WIDTH = 600
HEIGHT = 400

def draw():
    screen.fill("blue")

pgzrun.go()  # Starts the game


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import pgzrun

# Game window size
WIDTH = 600
HEIGHT = 400

# Create player
player = Actor("alien")
player.pos = (300, 200)

# Draw game
def draw():
    screen.fill("lightblue")
    player.draw()

# Move player
def update():
    if keyboard.left:
        player.x -= 3

    if keyboard.right:
        player.x += 3

    if keyboard.up:
        player.y -= 3

    if keyboard.down:
        player.y += 3

# Start game
pgzrun.go()