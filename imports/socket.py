#--------------------------------------------------------------------------------------------------------------|
# SOCKET IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: No installation needed.
# Socket is included with standard Python.

import socket  # Imports socket

print(socket.gethostname())  # Displays computer name


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import socket

# Get computer information
hostname = socket.gethostname()

# Get computer IP address
ip_address = socket.gethostbyname(hostname)

# Display information
print("Computer Name:", hostname)
print("IP Address:", ip_address)