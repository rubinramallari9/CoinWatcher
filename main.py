import requests



response = requests.get("https://api.coincap.io/v2/assets/bitcoin").json()
price = response["data"]["priceUsd"].split(".")[0]
print(price)