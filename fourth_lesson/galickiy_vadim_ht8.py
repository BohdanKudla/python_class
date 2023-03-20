import requests

response = requests.get('https://ukr.net/').text
print(response)