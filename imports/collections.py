import collections  # Imports collections

numbers = collections.Counter([1, 2, 2, 3])
print(numbers)  # Counts repeated numbers


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----| 
#--------------------------------------------------------------------------------------------------------------|


import collections

# Create a list of game items
inventory = ["sword", "potion", "sword", "shield", "potion", "potion"]

# Count each item
item_count = collections.Counter(inventory)

# Display inventory counts
print("Player Inventory:")

for item, amount in item_count.items():
    print(item, ":", amount)