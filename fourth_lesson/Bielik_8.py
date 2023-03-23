import requests

response = requests.get('https://www.englishdom.com/').text
print(response)