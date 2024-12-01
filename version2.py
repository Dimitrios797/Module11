import requests
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print('Response JSON:', response.json())