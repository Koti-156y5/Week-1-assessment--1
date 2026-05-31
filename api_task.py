import requests

response = requests.get("https://catfact.ninja/fact")

data = response.json()

print("Random Cat Fact:")
print(data["fact"])