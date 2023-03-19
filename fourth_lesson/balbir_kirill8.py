import requests

response = requests.get('https://lalafo.kg/bishkek/ads/prodau-neobycnye-tagi-barhatnye-id-106754729').text
print(response)