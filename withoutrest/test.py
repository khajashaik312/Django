import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='cbvresponse/'
response=requests.get(BASE_URL+ENDPOINT)
#response is indexable
print(response) #<Response [200]>
#response is not indexable
data=response.json()
print(data)