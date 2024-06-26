# Conversor de monedas

import requests

API_KEY = 'e278246514e613608d97c59f'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
print(url)
response = requests.get(url)
data = response.json()


print(response)
print(data)