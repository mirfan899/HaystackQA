import requests

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Accept': 'application/json',
}

json_data = {
    'query': 'Permanent Ban?',
}

response = requests.post('http://127.0.0.1:8000/query', headers=headers, json=json_data)
print(response.text)
