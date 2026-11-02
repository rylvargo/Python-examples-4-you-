import sys  # Imports the sys library

print(sys.version)  # Shows Python version


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import sys

# Display Python version
print("Python Version:", sys.version)

# Display operating system platform
print("Platform:", sys.platform)

# Ask user a question
answer = input("Type exit to close: ")

# Close program if requested
if answer.lower() == "exit":
    sys.exit()

print("Program is still running!")