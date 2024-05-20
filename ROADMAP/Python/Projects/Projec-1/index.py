# Conversor de monedas

import requests

api_key = 'e278246514e613608d97c59f'
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
print(url)
response = requests.get(url)
data = response.json()


print(response)
print(data)