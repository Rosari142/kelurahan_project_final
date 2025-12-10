import requests

url = "http://127.0.0.1:8000/api/warga/"
token = "528fddbf88804180dfd7fbbb7afded6b877de5e8"  # token yang kamu dapatkan

headers = {
    "Authorization": f"Token {token}"
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
