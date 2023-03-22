import requests

response = requests.get("https://www.ua-football.com/").text

print(response)