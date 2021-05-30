import requests
import json

baseUrl = 'https://openapi.biki.com/'
url = baseUrl + 'open/api/get_ticker?symbol=xqcbtc'

response = requests.get(url)

print(response.text)

resJson = json.loads(response.text)
print(resJson['data']['last'])
# print(response.text)
# <Response [200]> 200は成功

print(type(response))
# <class 'requests.models.Response'>