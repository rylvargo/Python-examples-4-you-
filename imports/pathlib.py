#--------------------------------------------------------------------------------------------------------------|
# PATHLIB IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: No installation needed.
# Pathlib is included with standard Python.

from pathlib import Path

folder = Path.cwd()  # Gets current folder

print(folder)


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


from pathlib import Path

# Get current folder
folder = Path.cwd()

# Create a folder
new_folder = folder / "MyGameFiles"
new_folder.mkdir(exist_ok=True)

# Create a text file
save_file = new_folder / "save.txt"

# Write information
save_file.write_text("Player Score: 500")

# Read information
data = save_file.read_text()

print("Saved Game Data:")
print(data)

print("Save location:", save_file)