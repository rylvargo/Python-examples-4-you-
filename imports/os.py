import os  # Imports the operating system library

print(os.getcwd())  # Shows the current folder


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import os  # Imports os

# Show current folder
print("Current folder:", os.getcwd())

# Show files in current folder
print("Files in folder:")

for file in os.listdir():
    print(file)

# Check if a folder exists
print("Does Downloads exist?", os.path.exists("Downloads"))