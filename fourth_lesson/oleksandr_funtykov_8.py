import requests

response = requests.get('https://ithillel.ua/').text
print(response)