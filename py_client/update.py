import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Update data with update.py",
    "price": "123.12"
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())

