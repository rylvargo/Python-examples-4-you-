#--------------------------------------------------------------------------------------------------------------|
# PILLOW IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Open your terminal or command prompt and type:
# pip install pillow

# SMALL EXAMPLE
#--------------------------------------------------------------------------------------------------------------|

from PIL import Image  # Imports Pillow's Image tool

image = Image.new("RGB", (200, 200), "blue")  # Creates a blue image

image.save("picture.png")  # Saves the image


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


from PIL import Image, ImageDraw

# Create a new image
image = Image.new("RGB", (500, 400), "lightblue")

# Create a drawing tool
draw = ImageDraw.Draw(image)

# Draw a red rectangle
draw.rectangle((50, 50, 200, 200), fill="red")

# Draw a yellow circle
draw.ellipse((250, 50, 400, 200), fill="yellow")

# Draw a blue line
draw.line((50, 300, 450, 300), fill="blue", width=5)

# Save image
image.save("my_drawing.png")

print("Image saved!")