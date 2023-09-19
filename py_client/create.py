import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Title for testing mixins",
    "content": "Testing mixins create"
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

