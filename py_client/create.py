import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "SomeTitle to pass data validation",
    "price": 12.69
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

