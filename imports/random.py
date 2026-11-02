
import random  # Imports the random library

number = random.randint(1, 10)  # Picks a random number from 1 to 10

print(number)  # Prints the random number


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import random

# Generate a random number
number = random.randint(1, 100)

# Ask the user to guess
guess = int(input("Guess a number (1-100): "))

# Check the answer
if guess == number:
    print("You got it!")
else:
    print("Wrong! The number was", number)







