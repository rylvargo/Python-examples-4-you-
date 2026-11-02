import csv  # Imports the CSV library

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Score"])


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----| 
#--------------------------------------------------------------------------------------------------------------|


import csv

# Create a CSV file
with open("players.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Add column names
    writer.writerow(["Player", "Score"])

    # Add player information
    writer.writerow(["Player1", 500])
    writer.writerow(["Player2", 750])
    writer.writerow(["Player3", 1000])

print("Player scores saved!")

# Read the CSV file
with open("players.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)