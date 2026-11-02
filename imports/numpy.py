#--------------------------------------------------------------------------------------------------------------|
# NUMPY IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Open your terminal or command prompt and type:
# pip install numpy

# SMALL EXAMPLE
#--------------------------------------------------------------------------------------------------------------|

import numpy as np  # Imports NumPy

numbers = np.array([10, 20, 30, 40])  # Creates an array

print(numbers * 2)  # Multiplies every number by 2


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import numpy as np

# Create player statistics
scores = np.array([100, 250, 300, 450, 500])

# Calculate average score
average = np.mean(scores)

# Find highest score
highest = np.max(scores)

# Find lowest score
lowest = np.min(scores)

# Add 100 points to every score
new_scores = scores + 100

# Display results
print("Player Scores:", scores)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("New Scores:", new_scores)