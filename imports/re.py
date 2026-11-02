import re  # Imports the regular expressions library

text = "Hello 123"
print(re.findall(r"\d", text))  # Finds numbers


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import re

# Ask user for a username
username = input("Enter a username: ")

# Check if username contains only letters and numbers
if re.fullmatch(r"[A-Za-z0-9]+", username):
    print("Valid username!")
else:
    print("Only letters and numbers are allowed.")