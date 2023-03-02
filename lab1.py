import requests
from datetime import datetime, timedelta

url = input("Enter the URL: ")

# Send HTTP GET request
response = requests.get(url)

# Print HTTP response headers
print("HTTP response headers:")
print("-------------------------")
for header, value in response.headers.items():
    print(header + ": " + value)
print("-------------------------")

# Server info and cookies
print("\nServer info and cookies:")
print("--------------------------------------------")
server_info = response.headers.get('Server')
if server_info:
    print("Server is running on software: " + server_info)

cookies = response.cookies
if cookies:
    print("\nThe page uses the following cookies:")
    for cookie in cookies:
        cookie_name = cookie.name
        cookie_expiration = datetime.now() + timedelta(seconds=cookie.expires) if cookie.expires else None
        if cookie_expiration:
            print(cookie_name + " (expires on " + str(cookie_expiration) + ")")
        else:
            print(cookie_name + " (expires at end of session)")
print("--------------------------------------------")
