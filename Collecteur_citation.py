import requests

response = requests.get("http://api.quotable.io/random")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erreur :", response.status_code)