import pygame  # Imports the pygame library

pygame.init()  # Starts pygame
pygame.quit()  # Closes pygame


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import pygame

# Start pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game")

# Set background color
screen.fill((0, 150, 255))

# Update display
pygame.display.flip()

# Keep window open
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Close pygame
pygame.quit()