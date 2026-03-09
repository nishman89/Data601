import requests
import json

post_code_response = requests.get("https://api.postcodes.io/postcodes/EC2y5as")
print(post_code_response)
print(post_code_response.status_code)
print(post_code_response.headers)
print(type(post_code_response.headers))
print(post_code_response.content)
print(post_code_response.json())
print(type(post_code_response.json()))

post_multi_response = requests.post(
    "https://api.postcodes.io/postcodes/",
    headers ={'Content-Type': 'application/json'},
    json={'postcodes' : ["PR3 0SG", "M45 6GN", "EX165BL"]}
)

print(post_multi_response)
print(post_multi_response.status_code)
print(post_multi_response.json())