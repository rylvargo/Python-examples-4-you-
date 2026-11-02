import datetime  # Imports the datetime library

print(datetime.datetime.now())  # Displays current date and time


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import datetime  # Imports datetime

# Get current date and time
now = datetime.datetime.now()

print("Current date:", now.strftime("%m/%d/%Y"))
print("Current time:", now.strftime("%I:%M %p"))
print("Current year:", now.year)