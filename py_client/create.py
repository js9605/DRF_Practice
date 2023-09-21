import requests


headers = {'Authorization': 'Bearer 5ecfb9c73e915f01cb343ebd35d2d2074d13dfa5'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Title for testing mixins",
    "content": "Testing mixins create"
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())

