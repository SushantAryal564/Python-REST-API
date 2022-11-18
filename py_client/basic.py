import requests

get_response = requests.get("http://httpbin.org/anything", json={"query":"Hello World"}) #API 
#REST API => Web API
print(get_response.text);
print(get_response.json())
# REST API HTTP Request => JSON
# HTTP REQUEST => HTML
