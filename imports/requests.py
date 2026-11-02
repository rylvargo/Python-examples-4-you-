#--------------------------------------------------------------------------------------------------------------|
# REQUESTS IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Open your terminal and type:
# pip install requests

import requests  # Imports requests

response = requests.get("https://example.com")

print(response.status_code)  # Shows website response


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import requests

# Website to visit
url = "https://api.github.com"

# Send request
response = requests.get(url, timeout=10)

# Check response
if response.status_code == 200:
    print("Website connected!")
    print(response.json())
else:
    print("Connection failed:", response.status_code)