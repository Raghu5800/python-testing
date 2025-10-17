import requests

url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

response = requests.get(url)

print(response.json(),response.status_code)
assert response.status_code == 200, "Response is not 200"
