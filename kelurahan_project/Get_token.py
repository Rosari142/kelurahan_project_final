import requests

url = 'http://127.0.0.1:8000/api/auth/token/'  # URL token sesuai urls.py

data = {
    "username": "aku",          # ganti dengan superusermu
    "password": "1234"    # ganti dengan passwordmu
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
