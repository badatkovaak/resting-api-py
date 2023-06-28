import requests

endpoint = "https://lichess.org"
endpoint = "http://localhost:8000/api/"


response = requests.get(endpoint, json={'text': 'hi there!'})
print(response.json())
