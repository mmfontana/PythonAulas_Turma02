import requests

response = requests.get('https://www.globo.com/')

status_code = response.status_code

text = response.text

print(text)

