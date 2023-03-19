import requests

response = requests.get('https://lms.ithillel.ua/').text
print(response)