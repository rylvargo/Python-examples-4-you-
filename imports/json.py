import json  # Imports the JSON library

data = {"name": "Player", "score": 100}

print(json.dumps(data))  # Converts data into JSON text


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import json  # Imports json

# Create player information
player = {
    "name": "Player1",
    "score": 500,
    "level": 3
}

# Convert information into JSON
saved_data = json.dumps(player, indent=4)

print("Saved Player Data:")
print(saved_data)

# Convert JSON back into Python data
loaded_data = json.loads(saved_data)

print("Player name:", loaded_data["name"])
print("Player score:", loaded_data["score"])