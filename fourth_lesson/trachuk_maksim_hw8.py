import requests


link_html = requests.get("https://lms.ithillel.ua/").text
print(link_html)

