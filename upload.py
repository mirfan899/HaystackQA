import requests

headers = {
    'Accept': 'application/json',
}

files = {
    'files': open('code-of-conduct.txt', 'rb'),
}

response = requests.post('http://127.0.0.1:8000/file-upload', headers=headers, files=files)