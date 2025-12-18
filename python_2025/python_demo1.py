import requests
api_url='https://fakestoreapi.com/products/'
out = requests.get(api_url)
print(out)

#Output:<Response [200]>

import requests
api_url='https://fakestoreapi.com/products/'
out = requests.get(api_url)
print(out.text)

#output

import requests
api_url='https://fakestoreapi.com/products/'
out = requests.get(api_url)
print(type(out.text))
#output:<class 'str'>

import requests
api_url='https://fakestoreapi.com/products/'
out = requests.get(api_url)
data = out.text
print(data[0])
#output: [

import requests
api_url='https://fakestoreapi.com/products/'
out = requests.get(api_url)
data = out.json()
print(len(data))
#output:20

import requests
api_url='https://fakestoreapi.com/products/'
out = requests.get(api_url)
data = out.json()
print(type(data))
#output: <class 'list'>

import requests
api_url='https://fakestoreapi.com/products/'
out = requests.get(api_url)
data = out.text
print(len(data))
#output: 10634