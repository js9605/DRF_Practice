import requests


endpoint = "http://localhost:8000/api/"
get_response = requests.get(endpoint, json={"product_id": 123})

# print("status code: ", get_response.status_code)
# print(get_response.json())
print(get_response.headers)
print(get_response.text)
