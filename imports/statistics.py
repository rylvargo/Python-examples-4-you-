import statistics  # Imports statistics

numbers = [10, 20, 30, 40, 50]
print(statistics.mean(numbers))  # Finds average


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----| 
#--------------------------------------------------------------------------------------------------------------|


import statistics

# Player scores
scores = [100, 250, 300, 150, 500]

# Calculate average
average = statistics.mean(scores)

# Find highest and lowest scores
highest = max(scores)
lowest = min(scores)

# Display results
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)