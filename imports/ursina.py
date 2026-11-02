#--------------------------------------------------------------------------------------------------------------|
# URSINA IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Open your terminal or command prompt and type:
# pip install ursina

# SMALL EXAMPLE
#--------------------------------------------------------------------------------------------------------------|

from ursina import *  # Imports the Ursina library

app = Ursina()  # Creates the game

cube = Entity(model="cube", color=color.red)  # Creates a red cube

app.run()  # Starts the game


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


from ursina import *

# Create the game
app = Ursina()

# Create a floor
floor = Entity(
    model="plane",
    scale=(20, 1, 20),
    color=color.green,
    collider="box"
)

# Create a player
player = Entity(
    model="cube",
    color=color.orange,
    scale=(1, 2, 1),
    position=(0, 1, 0),
    collider="box"
)

# Create a sky
Sky()

# Move player with WASD
def update():
    player.x += (held_keys["d"] - held_keys["a"]) * time.dt * 5
    player.z += (held_keys["w"] - held_keys["s"]) * time.dt * 5

# Start game
app.run()