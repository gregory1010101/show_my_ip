import requests
response = requests.get('https://api64.ipify.org?format=json').json()
print(response["ip"])