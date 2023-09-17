import requests


endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint, json={"title": "SomeTitle", "content": "Hello world", "price": "as123"})

print("status code: ", get_response.status_code)
print("response.json: ", get_response.json())
# print(get_response.headers)
# print(get_response.text)
