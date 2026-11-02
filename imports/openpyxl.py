#--------------------------------------------------------------------------------------------------------------|
# OPENPYXL IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Open your terminal and type:
# pip install openpyxl

import openpyxl  # Imports openpyxl

workbook = openpyxl.Workbook()  # Creates an Excel workbook

workbook.save("test.xlsx")  # Saves the workbook


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import openpyxl

# Create workbook
workbook = openpyxl.Workbook()

# Select worksheet
sheet = workbook.active

# Add column names
sheet["A1"] = "Player"
sheet["B1"] = "Score"

# Add player information
sheet.append(["Player1", 500])
sheet.append(["Player2", 750])
sheet.append(["Player3", 1000])

# Save Excel file
workbook.save("players.xlsx")

print("Player scores saved!")